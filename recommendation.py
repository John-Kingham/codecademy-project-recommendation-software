from dataclasses import dataclass
import csv
from hashmap import HashMap
from linked_list import LinkedList, Node


@dataclass(order=True)
class Album:
    """
    A data class that holds data related to an album.
    """

    category: str
    name: str
    artist: str
    release_date: str


class MusicDatabase:
    """
    A database of albums.
    This class allows the user interface to deal with the music data at a higher level of
    abstraction than linked lists and hashmaps.
    """

    def __init__(self, filename: str) -> None:
        """
        Creates a new music database using data from a csv file.

        Parameters
        ----------
        filename
            The name of the csv file.
        """

        # load data from csv into a hashmap of linked lists

        self.hashmap: HashMap = HashMap()
        with open(filename, newline="") as music_file:
            music_reader = csv.DictReader(music_file)
            for row in music_reader:
                album: Album = Album(
                    row["Category"], row["Name"], row["Artist"], row["Release Date"]
                )
                album_list: LinkedList = self.hashmap.get(album.category)
                if not album_list:
                    album_list = LinkedList(album)
                    self.hashmap.add(album.category, album_list)
                else:
                    album_list.insert(album)

    def find_categories(self, search_string: str) -> list[str]:
        """
        Returns a list of category names that contain the search string.

        Parameters
        ----------
        search_string
            A full or partial category name which may match zero or more categories.

        Returns
        -------
        list of category names
            The category names that contain the search string. Empty if no matches are found.
        """
        categories: list[str] = []
        for category in self.hashmap.keys():
            if search_string in category:
                categories.append(category)
        return categories

    def get_albums(self, category: str) -> list[Album]:
        """
        Given a music category, returns the albums from that category.

        Parameters
        ----------
        category
            The music category the albums should be from.

        Returns
        -------
        list of Albums
            The albums from the category. Empty if no matching albums are found.
        """
        category_albums: LinkedList = self.hashmap.get(category)
        if not category_albums:
            return []
        album_list: list[Album] = []
        node: Node = category_albums.head
        more_nodes: bool = True
        while more_nodes:
            album_list.append(node.value)  # type: ignore
            if node.next:
                node = node.next
            else:
                more_nodes = False
        return album_list


def main() -> None:
    """
    This program is a basic music recommendation engine with a command-line interface.

    Users can search for categories of music using partial search strings.
    They're shown a list of matching categories.
    They can select a category and sell a list of albums in that category.
    """
    database: MusicDatabase = MusicDatabase("music_database.csv")
    print("Welcome to the Music Recommendation Engine\n")

    # get the user to choose a single music category

    quit: bool = False
    while not quit:
        chosen_category: str = ""
        while not chosen_category:
            search_string: str = input(
                "Please enter all or part of the name of a music category you'd like to listen to:\n"
            )
            categories: list[str] = database.find_categories(search_string)
            if len(categories) == 0:
                print(
                    "Sorry, your search didn't match any categories. Please try again.\n"
                )
                continue
            if len(categories) == 1:
                chosen_category = categories[0]
                continue
            print(
                "Your search matches several categories. Please choose from the list of categories below by entering the related number.\n"
            )
            for i in range(len(categories)):
                print(f"{i+1} : {categories[i]}")
            while not chosen_category:
                chosen_index: int = (
                    int(input(f"\nEnter your choice (from 1 to {len(categories)}):\n"))
                    - 1
                )
                if chosen_index not in range(len(categories)):
                    print("Sorry, your choice wasn't valid. Please try again.\n")
                    continue
                chosen_category = categories[chosen_index]

        # show the user a list of albums from their chosen category

        print(f"You have chosen the {chosen_category} category.\n")
        print("Here is a list of albums from that category.\n")
        albums: list[Album] = database.get_albums(chosen_category)
        for album in albums:
            print(
                f"Name: {album.name}, Artist: {album.artist}, Release Date: {album.release_date}"
            )

        # ask the user if they want to quit or search again

        choice: str = input("\nTo search again, enter any letter. To quit, enter q:\n")
        if choice == "q":
            print("Thank you for using the music recommendation engine. Goodbye...")
            quit = True


if __name__ == "__main__":
    main()
