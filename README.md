# Codecademy Project: Recommendation Software

## Overview (from Codecademy)
In this portfolio project, you will research, brainstorm, and build a basic recommendation program for a topic of your choice that has the following functionality:

- By entering letters or words into the terminal, the program will suggest a specific category for the user to explore. 
- If the user is interested in the category, the program will provide a variety of related recommendations to the user. 

After you finish building the program, you will create a blog post to share the program on a publication of your choice.

## Requirements

**This recommendation program will help users find music they might want to listen to.**

Mapping Codecademy's requirements onto the music recommendation program gives the following:

### Functional Requirement 1: Choose a Music Category
- The user enters the full or partial name of a music category they're interested in. For example, they might enter "rock" or "classical" or "b".
- If the user's input doesn't match any categories, they will be asked to try again.
- If the user's input matches one category, they have chosen that category.
- If the user's input matches several categories, they will be shown a list of those categories from which they can choose one. For example, a search for "rock" might return a list of categories including "hard rock", "soft rock" and "rock & roll".

### Functional Requirement 2: Get Albums by Category
- Once the user has selected one category, the program shows them a list of albums from that category.

### Implicit Requirements
- The program should validate user input.
- The program should give the user the option of quitting or searching again.

### Technical Requirements
As requested by Codecademy:
1. The program should be written in Python.
2. The program should use a command line interface.
3. The program should use at least one of these data structures: Linked List, Hash Map, Tree.

## Architecture
- Programming language: Python 3
  - As required by Codecademy.
  - Type annotation: All of the code uses type annotation.
- User interface: Command line
  - As required by Codecademy.
- Programming paradigm: Object-oriented and procedural
  - Why object-oriented? Because the program will use hashmaps and linked lists and I've learned to build them using an object-oriented approach. It's also a good opportunity to practice designing and writing classes.
  - Why procedural? Because the user interface will be coded in the main function.
- Database: CSV file
  - Codecademy's example database was a Python list of lists. I wanted to practice working with CSV files, so I've gone down that route.

## High-level design
- Classes
  - MusicDatabase: 
    - A class that allows the user interface function to deal with database-related activities at a high level of abstraction.
    - This class manages the conversion of the csv database file into a hashmap which maps music categories to linked lists of Album objects.
  - Album:
    - A dataclass that stores album data from the CSV file.
  - HashMap:
    - A hashmap that the MusicDatabase object uses to store linked lists of Album objects.
  - Node:
    - A node for use in a singly linked list.
  - LinkedList:
    - A singly linked list which the MusicDatabase object fills with Album objects.
- Functions
  - Main:
    - Contains all of the user interface code.
- Database
  - music_database.csv
    - I asked GitHub Copilot to build me a database of fictional albums with the some relevant fields (category, name, artist, release date). It performed this task admirably.
    - Originally, I asked Copilot to build that data as a Python list of lists. I then decided to use csv instead, so I wrote a short script to convert the list of lists into csv format.

## Unit testing
All classes have related unit tests using the Python unittest module.