"""EX13."""


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.
    Example input with https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms
        get_links_from_spreadsheet('1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms', 'token.json')

    Returns
        ['Student Name', 'Alexandra', 'Andrew', 'Anna', 'Becky', ... and so on from the first column]
    """
    return []


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.
    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')

    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    return []