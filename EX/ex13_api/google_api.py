"""EX13."""
from __future__ import print_function
import googleapiclient.discovery
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms
        get_links_from_spreadsheet('1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms', 'token.json')

    Returns
        ['Student Name', 'Alexandra', 'Andrew', 'Anna', 'Becky', ... and so on from the first column]
    """
    # If modifying these scopes, delete the file token.json.
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    # The ID and range of a sample spreadsheet.
    creds = Credentials.from_authorized_user_file(token, scopes)
    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range='A:A').execute()
    return [row[0] for row in result.get('values')]


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.

    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')
    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    api_service_name = "youtube"
    api_version = "v3"
    developer_key_ = developer_key

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key_)
    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=link.split('?list=')[1],
        maxResults=100000
    )
    videoids = []
    response = request.execute()
    for item in response['items']:
        videoids.append(f'www.youtube.com/watch?v={item["contentDetails"]["videoId"]}')
    return videoids


if __name__ == '__main__':
    print(get_links_from_spreadsheet('1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms', 'token.json'))
    print(get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK', "AIzaSyCzqrS9g9oHUz_uuZTJGdOgIzZyXwV6jRY"))
