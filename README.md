# Codecademy Project: Recommendation Software

## Overview (from Codecademy)
In this portfolio project, you will research, brainstorm, and build a basic recommendation program for a topic of your choice that has the following functionality:

- By entering letters or words into the terminal, the program will suggest a specific category for the user to explore. 
- If the user is interested in the category, the program will provide a variety of related recommendations to the user. 

After you finish building the program, you will create a blog post to share the program on a publication of your choice.

## Technical requirements
This project consists of two main parts:

1. Implementing an autocomplete that, based on a user’s input, returns a list of possible categories based on the beginning of a word.
2. Retrieving and displaying all of the data related to the category selected by the user.

Given that this project comes at the end of the data structures and algorithms lessons, the requirement below is the most important part of the project: 

**The program should use at least one of these data structures: Linked List, Hash Map, Tree.**

## Think of an idea
I'm going to build a recommendation program that helps users find music they might want to listen to.

## Project brainstorming
A first-pass guess at the functionality is:

1. Show a welcome message to the user
2. Ask the user to enter the beginning letter(s) of a music category. For example, if they just enter "r", they'll be shown a list of categories to choose from that start with "r", such as rock and reggae.
3. Show the options as a numbered list and ask the user to choose an option, or zero to try again.
4. Once the user chooses a music category, they'll be shown a list of popular (fictional) albums from that category.
5. To improve the user experience, the program will include input validation and easy ways to choose other categories or quit.

## Autocomplete
- This turned out to be a one-liner using "search_string in string" and a list comprehension.
- I needed to create a database of music categories and imaginary albums, so I asked GitHub Copilot and Microsoft Copilot, and between then they generated the appropriate content and Python lists.

## Category retrieval
Here are some initial thoughts:
- This needs to use either a Linked List, a Hash Map or a Tree.
- The albums in a category could be stored in a linked list.
- Each node's value would be a Python list containing the album's four data items (name, artist, release date).
- We could store each linked list in a hash map, keyed by category name.
- Once the user has chosen a category, we can use that as a key to look for the album linked list in the hash map. 
- Once we have the linked list of albums, we can traverse through the list and print out all the data.
