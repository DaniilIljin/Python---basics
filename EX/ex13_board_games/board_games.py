"""EX13 Board Games."""
import re


class Statistics:
    """Needed  class."""

    def __init__(self, filename):
        """Initiate this class."""
        with open(filename, 'r') as file_content:
            content = file_content.read()
        matches = re.findall(r'.+[^\n]', content)
        self.data_ready_to_use = [match.split(';') for match in matches]
        self.games = [Game(data) for data in self.data_ready_to_use]
        self.all_players = self.creating_real_players()

    def get_data(self):
        """."""
        return self.data_ready_to_use

    def get_games(self):
        """."""
        return self.games

    def get_players(self):
        """."""
        return self.all_players

    def creating_real_players(self):
        """."""
        list_of_players = []
        for game in self.games:
            new_list = game.get_players_data()
            for player_data in new_list:
                name = player_data[0]
                if list_of_players:
                    names = [player.get_name() for player in list_of_players]
                    if name in names:
                        for player in list_of_players:
                            if name == player.get_name():
                                self.adding_data_to_player(player, player_data, game)
                            if game.get_name() in player.wins():
                                if game.get_points():
                                    if str(player.get_points()[game.get_name()][-1]) in game.get_points():
                                        game.set_record_holder(player, player.get_points()[game.get_name()][-1])
                            list_of_players += [player]
                    else:
                        new_player = Player(name)
                        self.adding_data_to_player(new_player, player_data, game)
                        if game.get_name() in new_player.wins():
                            if game.get_points():
                                if str(new_player.get_points()[game.get_name()][-1]) in game.get_points():
                                    game.set_record_holder(new_player, new_player.get_points()[game.get_name()][-1])
                        list_of_players += [new_player]
                else:
                    new_player = Player(name)
                    self.adding_data_to_player(new_player, player_data, game)
                    if game.get_name() in new_player.wins():
                        if game.get_points():
                            if str(new_player.get_points()[game.get_name()][-1]) in game.get_points():
                                game.set_record_holder(new_player, new_player.get_points()[game.get_name()][-1])
                    list_of_players += [new_player]
        return list_of_players

    def adding_data_to_player(self, player, his_data, game):
        """."""
        if his_data[1]:
            player.set_by_points(game.get_name(), his_data[1], his_data[2], his_data[3])
        elif his_data[2]:
            player.set_by_place(game.get_name(), his_data[2], his_data[3])
        elif his_data[3] == 'winner':
            player.is_a_winner(game.get_name())
        else:
            player.just_played(game.get_name())

    def get(self, path: str):
        """."""
        if self.games:
            if path[:7] == "/player":
                return self.players_info(path)
            elif path[:5] == "/game":
                return self.games_info(path)
            elif path[:6] == "/total":
                return self.total_info(path)

    def players_info(self, path):
        """."""
        if path == '/players':
            return [player.get_name() for player in self.all_players]
        elif path.split('/')[3] == 'amount':
            if path.split('/')[2] in [player.get_name() for player in self.all_players]:
                for player in self.all_players:
                    if path.split('/')[2] == player.get_name():
                        return sum([player.get_frequency()[game] for game in player.get_frequency()])
        elif path.split('/')[3] == 'favourite':
            if path.split('/')[2] in [player.get_name() for player in self.all_players]:
                for player in self.all_players:
                    if path.split('/')[2] == player.get_name():
                        return max(player.get_frequency(), key=lambda game: player.get_frequency()[game])
        elif path.split('/')[3] == 'won':
            if path.split('/')[2] in [player.get_name() for player in self.all_players]:
                for player in self.all_players:
                    if path.split('/')[2] == player.get_name():
                        if player.wins():
                            return sum([player.wins()[game] for game in player.wins()])
                        else:
                            return 0

    def games_info(self, path):
        """."""
        if path == "/games":
            return list(set([game.get_name() for game in self.games]))
        elif path.split('/')[2] in [game.get_name() for game in self.games]:
            needed_players1 = [player for player in self.all_players if path.split('/')[2] in player.wins()]
            needed_players2 = [player for player in self.all_players if
                              path.split('/')[2] in player.get_looses()]
            if path.split('/')[3] == 'amount':
                return [game.get_name() for game in self.games].count(path.split('/')[2])
            elif path.split('/')[3] == 'player-amount':
                list_of_game_players = [len(game.get_players_data()) for game in self.games if
                                            game.get_name() == path.split('/')[2]]
                return max(list_of_game_players, key=lambda element: list_of_game_players.count(element))
            elif path.split('/')[3] == 'most-wins':
                return sorted(needed_players1, key=lambda player: player.wins()[path.split('/')[2]])[-1].get_name()
            elif path.split('/')[3] == 'most-frequent-winner':
                return \
                    sorted(needed_players1, key=lambda player: player.wins()[path.split('/')[2]] / player.frequency[
                        path.split('/')[2]])[-1].get_name()
            elif path.split('/')[3] == 'most-frequent-loser':
                return sorted(needed_players2,
                                  key=lambda player: player.get_looses()[path.split('/')[2]] / player.frequency[
                                      path.split('/')[2]])[-1].get_name()
            elif path.split('/')[3] == 'most-losses':
                return sorted(needed_players2, key=lambda player: player.get_looses()[path.split('/')[2]])[
                        -1].get_name()
            elif path.split('/')[3] == 'record-holder':
                if path.split('/')[2] in [game.get_name() for game in [game for game in self.games if game.get_points()]]:
                    g = [game for game in self.games if game.get_name() == path.split('/')[2]]
                    record_holders = [game.record_holder for game in self.games if game.get_name() == path.split('/')[2]]
                    record = record_holders[0]
                    for record_holder in record_holders:
                        if int(record_holder[1]) > int(record[1]):
                            record = record_holder
                    return record[0].get_name()

    def total_info(self, path):
        """."""
        if path == "/total":
            return len(self.games)
        elif path[:7] == "/total/":
            if path[7:] == 'points':
                return len([game for game in self.games if game.get_points()])
            elif path[7:] == 'places':
                return len([game for game in self.games if game.get_places() and not game.get_points()])
            elif path[7:] == 'winner':
                return len([game for game in self.games if game.get_winner() and not game.get_places()])


class Game:
    """Game."""

    def __init__(self, game_data: list):
        """."""
        self.record_holder = None
        self.game_data = game_data
        self.name = game_data[0]
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
        self.players_data = self.creating_players_data(game_data[1].split(','))

    def set_record_holder(self, player, record):
        """."""
        self.record_holder = (player, record)

    def creating_players_data(self, names):
        """."""
        list_of_players = []
        if self.winner:
            for name in names:
                players_list = [name, None]
                if self.winner == name:
                    players_list += [1, 'winner']
                else:
                    players_list += [None, None]
                list_of_players.append(players_list)
        elif self.places:
            for index, name in enumerate(self.places):
                players_list = [None, index + 1]
                if self.places[0] == name:
                    players_list.append('winner')
                elif self.places[-1] == name:
                    players_list.append('looser')
                else:
                    players_list.append(None)
                list_of_players.append([name] + players_list)
        elif self.points:
            places = [int(element) for element in self.points]
            places.sort()
            for index, name in enumerate(names):
                points = self.points[index]
                players_list = [name, points, len(places) - places.index(int(points))]
                if points == str(places[-1]):
                    players_list.append('winner')
                elif points == str(places[0]):
                    players_list.append('looser')
                else:
                    players_list.append(None)
                list_of_players.append(players_list)
        return list_of_players

    def get_players_data(self):
        """."""
        return self.players_data

    def get_places(self):
        """."""
        return self.places

    def get_winner(self):
        """."""
        return self.winner

    def get_name(self):
        """."""
        return self.name

    def get_points(self):
        """."""
        return self.points

    def get_looser(self):
        """."""
        return self.looser


class Player:
    """A player."""

    def __init__(self, name):
        """."""
        self.name = name
        self.games_and_points = {}
        self.games_and_places = {}
        self.games_and_wins = {}
        self.games_and_looses = {}
        self.frequency = {}

    def get_name(self):
        """."""
        return self.name

    def get_points(self):
        """."""
        return self.games_and_points

    def get_place(self):
        """."""
        return self.games_and_places

    def wins(self):
        """."""
        return self.games_and_wins

    def get_frequency(self):
        """."""
        return self.frequency

    def get_looses(self):
        """."""
        return self.games_and_looses

    def set_by_place(self, game_name, place, status):
        """."""
        if game_name in self.games_and_places:
            self.games_and_places[game_name] += [place]
        else:
            self.games_and_places[game_name] = [place]
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
        if game_name in self.frequency:
            self.frequency[game_name] += 1
        else:
            self.frequency[game_name] = 1

    def set_by_points(self, game_name, points, place, status):
        """."""
        if game_name in self.games_and_points:
            self.games_and_points[game_name] += [points]
        else:
            self.games_and_points[game_name] = [points]
        if game_name in self.games_and_places:
            self.games_and_places[game_name] += [place]
        else:
            self.games_and_places[game_name] = [place]
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
        if game_name in self.frequency:
            self.frequency[game_name] += 1
        else:
            self.frequency[game_name] = 1

    def is_a_winner(self, game_name):
        """."""
        if game_name in self.games_and_wins:
            self.games_and_wins[game_name] += 1
        else:
            self.games_and_wins[game_name] = 1
        if game_name in self.frequency:
            self.frequency[game_name] += 1
        else:
            self.frequency[game_name] = 1

    def just_played(self, game_name):
        """."""
        if game_name in self.frequency:
            self.frequency[game_name] += 1
        else:
            self.frequency[game_name] = 1


if __name__ == '__main__':
    s = Statistics('some_statistics.txt')
    g = Game(s.get_data()[4])
    g.creating_players_data(['ago', 'jaak', 'kristjan', 'joosep'])
    # ['riho', None, 1, 'winner']
    # p.is_a_winner('upcha')
    # print(p.winns())
    print(g.get_players_data())
    # print(s)
    print(s.get("/total/winner"))
    print(s.get('/game/terraforming mars/record-holder'))
