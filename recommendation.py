from music_database import categories


def autocomplete(search: str) -> list[str]:
    """
    Returns a list of music categories that match the user's input.

    Parameters
    ----------
    search: str
        What the user typed to search for one or more music categories.

    Returns
    -------
    list: str
        A list of category names that contain the user's search string.
        If no categories are found the list is empty.
    """
    return [category for category in categories if search in category]
