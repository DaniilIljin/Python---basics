"""EX13 Board Games."""
import re


class Statistics:
    """Statistics class."""

    def __init__(self, filename):
        """Initiate this class."""
        with open(filename, 'r') as file_content:
            content = file_content.read()
        matches = re.findall(r'.+[^\n]', content)
        self.data_ready_to_use = [match.split(';') for match in matches]
        self.games = [Game(data) for data in self.data_ready_to_use]
        self.all_players = []
        self.creating_real_players()

    def creating_real_players(self):
        """Create real objects Players() from their data."""
        for game in self.games:
            for player_data in game.players_data:
                name = player_data[0]
                if name in [player.name for player in self.all_players]:
                    for player in self.all_players:
                        if name == player.name:
                            self.adding_data_to_player(player, player_data, game.name)
                            player.setting_player_status(game.name, player_data[3])
                            player.played(game.name)
                            game.players.append(player)
                else:
                    new_player = Player(name)
                    self.adding_data_to_player(new_player, player_data, game.name)
                    new_player.played(game.name)
                    new_player.setting_player_status(game.name, player_data[3])
                    self.all_players.append(new_player)
                    game.players.append(new_player)
            if game.points:
                for player in game.players:
                    if game.name in player.games_and_wins:
                        game.set_record_holder(player, player.games_and_points[game.name][-1])

    def adding_data_to_player(self, player, his_data, game_name):
        """Add data to objekt Player() if hi played a game with points or places."""
        if his_data[1]:
            player.set_by_points(game_name, his_data[1])
        elif his_data[2]:
            player.set_by_place(game_name, his_data[2])

    def find_player(self, player_name):
        """I created this to simplify my life and functions."""
        for player in self.all_players:
            if player.name == player_name:
                return player

    def get(self, path: str):
        """Get smth."""
        if self.games:
            if path[:7] == "/player":
                return self.players_info(path)
            elif path[:5] == "/game":
                return self.games_info(path)
            elif path[:6] == "/total":
                return self.total_info(path)

    def players_info(self, path):
        """If is needed info about players."""
        if path == '/players':
            return [player.name for player in self.all_players]
        elif path.split('/')[2] in [player.name for player in self.all_players]:
            player = self.find_player(path.split('/')[2])
            if path.split('/')[3] == 'amount':
                return sum([player.frequency[game] for game in player.frequency])
            elif path.split('/')[3] == 'favourite':
                return max(player.frequency, key=lambda game: player.frequency[game])
            elif path.split('/')[3] == 'won':
                return sum([player.games_and_wins[game] for game in player.games_and_wins])

    def games_info(self, path):
        """If needed info about games."""
        if path == "/games":
            return list(set([game.name for game in self.games]))
        elif path.split('/')[2] in [game.name for game in self.games]:
            game_name = path.split('/')[2]
            needed_players1 = [player for player in self.all_players if game_name in player.games_and_wins]
            needed_players2 = [player for player in self.all_players if game_name in player.games_and_looses]
            if path.split('/')[3] == 'amount':
                return [game.name for game in self.games].count(game_name)
            elif path.split('/')[3] == 'player-amount':
                list_of_game_players = [len(game.players) for game in self.games if game.name == game_name]
                return max(list_of_game_players, key=lambda element: list_of_game_players.count(element))
            elif path.split('/')[3] == 'most-wins':
                return sorted(needed_players1, key=lambda player: player.games_and_wins[game_name])[-1].name
            elif path.split('/')[3] == 'most-frequent-winner':
                return sorted(needed_players1, key=lambda player: player.games_and_wins[game_name] / player.frequency[game_name])[-1].name
            elif path.split('/')[3] == 'most-frequent-loser':
                return sorted(needed_players2, key=lambda player: player.games_and_looses[game_name] / player.frequency[game_name])[-1].name
            elif path.split('/')[3] == 'most-losses':
                return sorted(needed_players2, key=lambda player: player.games_and_looses[game_name])[-1].name
            elif path.split('/')[3] == 'record-holder':
                return self.record_holder_func(game_name)

    def record_holder_func(self, game_name):
        """To simplify previous function."""
        record_holders = [game.record_holder for game in self.games if game.name == game_name]
        record = record_holders[0]
        for record_holder in record_holders:
            if int(record_holder[1]) > int(record[1]):
                record = record_holder
        return record[0].name

    def total_info(self, path):
        """If needed total info."""
        if path == "/total":
            return len(self.games)
        elif path[:7] == "/total/":
            if path[7:] == 'points':
                return len([game for game in self.games if game.points])
            elif path[7:] == 'places':
                return len([game for game in self.games if game.places])
            elif path[7:] == 'winner':
                return len([game for game in self.games if not game.places and not game.points])


class Game:
    """Game."""

    def __init__(self, game_data: list):
        """Initiate this class."""
        self.record_holder = None
        self.name = game_data[0]
        self.players = []
        self.places = None
        self.points = None
        self.winner = None
        self.looser = None
        if game_data[2] == 'points':
            self.points = game_data[3].split(',')
        elif game_data[2] == 'places':
            self.places = game_data[3].split(',')
        elif game_data[2] == 'winner':
            self.winner = game_data[3]
        self.players_data = []
        self.creating_players_data(game_data[1].split(','))

    def set_record_holder(self, player, record):
        """Create a record holder."""
        self.record_holder = (player, record)

    def creating_players_data(self, names):
        """
        Create player data by given data to game.

        If game has only winner, then it will use first way to add data to player.
        If game has places, player data will be created bu second way.
        And the same with points.
        """
        if self.winner:
            self.first_way(names)
        elif self.places:
            self.second_way()
        elif self.points:
            self.third_way(names)

    def first_way(self, names):
        """Create player data by winner."""
        for name in names:
            players_list = [name, None]
            if self.winner == name:
                players_list += [1, 'winner']
            else:
                players_list += [None, None]
            self.players_data.append(players_list)

    def second_way(self):
        """Create player data by places."""
        for index, name in enumerate(self.places):
            players_list = [None, index + 1]
            if self.places[0] == name:
                players_list.append('winner')
            elif self.places[-1] == name:
                players_list.append('looser')
            else:
                players_list.append(None)
            self.players_data.append([name] + players_list)

    def third_way(self, names):
        """Create player data by points."""
        places = [int(element) for element in self.points]
        places.sort()
        for index, name in enumerate(names):
            points = self.points[index]
            players_list = [name, points, None]
            if points == str(places[-1]):
                players_list.append('winner')
            elif points == str(places[0]):
                players_list.append('looser')
            else:
                players_list.append(None)
            self.players_data.append(players_list)


class Player:
    """A player."""

    def __init__(self, name):
        """Initiate this class."""
        self.name = name
        self.games_and_points = {}
        self.games_and_places = {}
        self.games_and_wins = {}
        self.games_and_looses = {}
        self.frequency = {}

    def played(self, game_name):
        """Function add to player info about the game that he has played."""
        if game_name in self.frequency:
            self.frequency[game_name] += 1
        else:
            self.frequency[game_name] = 1

    def set_by_place(self, game_name, place):
        """Add data to player if he has played a game with places."""
        if game_name in self.games_and_places:
            self.games_and_places[game_name] += [place]
        else:
            self.games_and_places[game_name] = [place]

    def set_by_points(self, game_name, points):
        """Add data to player if he has played a game with points."""
        if game_name in self.games_and_points:
            self.games_and_points[game_name] += [points]
        else:
            self.games_and_points[game_name] = [points]

    def setting_player_status(self, game_name, status):
        """Add data to player if he is a winner or looser."""
        if status == 'winner':
            if game_name in self.games_and_wins:
                self.games_and_wins[game_name] += 1
            else:
                self.games_and_wins[game_name] = 1
        elif status == 'looser':
            if game_name in self.games_and_wins:
                self.games_and_looses[game_name] += 1
            else:
                self.games_and_looses[game_name] = 1


if __name__ == '__main__':
    s = Statistics('some_statistics.txt')
    # ['riho', None, 1, 'winner']
    # p.is_a_winner('upcha')
    # print(p.winns())
    print(s.get('/game/terraforming mars/record-holder'))
    print(s.get('/player/joosep/favourite'))
