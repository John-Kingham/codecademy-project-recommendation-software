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

# Function name: get_albums
def get_albums(category: str) -> list[list[str]]:
    """
    Given a music category, returns a list of albums from that category.

    Parameters
    ----------
    category : str
        The music category the albums should be from.

    Returns
    -------
    list : a list of list[str]
        blah.
    """
    # This function needs to use either a Linked List, a Hash Map or a Tree.
    # The albums in a category could be stored in a linked list.
    # Each node's value would be the album list of four data items.
    # We could store each linked list in a hash map, keyed by category name

    # TODO

    # Before writing this function, we need a function to load the albums 
    # for a given category into a linked list
    return [[""],[""]]


def recommendation() -> None:
    """
    A basic recommendation program with a command-line interface.

    Users can search for categories of interesting using partial search strings.
    They're shown a list of matching categories.
    They can select a category and sell a list of albums in that category.
    """
    # greet the user
    # while the user hasn't quit
    #   while there are no matching categories
    #       ask for a partial category search string
    #       if there were no matching categories
    #           tell the user
    #   show the user a numbered list of the matching categories
    #   while user input is invalid
    #       ask the user to pick a number from that list
    #   show the user the list of albums from that category
    #   ask the user if they want to quit or search again
