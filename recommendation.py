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

# Function name: recommendation
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
