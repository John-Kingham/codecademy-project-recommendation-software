# Codecademy Project: Recommendation Software

## Overview (from Codecademy)
In this portfolio project, you will research, brainstorm, and build a basic recommendation program for a topic of your choice that has the following functionality:

- By entering letters or words into the terminal, the program will suggest a specific category for the user to explore. 
- If the user is interested in the category, the program will provide a variety of related recommendations to the user. 

After you finish building the program, you will create a blog post to share the program on a publication of your choice.

## Requirements

**This recommendation program will help users find music they might want to listen to.**

Mapping Codecademy's requirements onto the music recommendation program gives the following:

### Functional Requirement 1: Choose Music Category
- The user enters the full or partial name of a music category they're interested in. For example, they might enter "rock" or "classic".
- If the user's input is invalid or doesn't match any categories, they will be given the option of entering a new search or quitting the program.
- If the user's input matches one category, they will be told the name of that category and shown a list of albums from that category.
- If the user's input matches many categories, they will be shown a list of those categories and given the option of selecting one. For example, a search for "rock" might return a list of categories including "hard rock", "soft rock" and "rock & roll".

### Functional Requirement 2: Show Albums
- The user selects a specific music category using the Choose Music Category process.
- The program shows the user a list of albums from that category.
- The program then asks the user if they want to search again, or quit, and proceeds as requested.

### Technical Requirements
As requested by Codecademy:
1. The program should be written in Python.
2. The program should use a command line interface.
3. The program should use at least one of these data structures: Linked List, Hash Map, Tree.

## Architecture
- Programming language: Python 3
  - As required
- User interface: Command line (required by Codecademy)
  - As required
- Programming paradigm: Object-oriented and procedural
  - Object-oriented because the program will use linked lists and I've learned to build linked-lists using an object-oriented approach.
  - Procedural because this is a small program that can run as a simple "main" function.
- Database: Python lists
  - This was Codecademy's default choice so I went with that.

## High-level design

The program will:
- Use a "main" function to manage user interaction.
- Use helper functions as needed to simplify the main function.
- Store several pieces of album data in a list.
- Store all of the album data lists for a category in an object-oriented linked list.
  - The linked list will consist of Node and LinkedList classes.
- Store the category linked lists in a hashmap keyed by category name.
  - The hashmap will be implemented as a HashMap class that uses open addressing to resolve collisions. 