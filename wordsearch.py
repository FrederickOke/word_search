"""
File:       wordsearch.py
Author:     Frederick Oke
Date:       7/8/2021
E-mail:     foke1@umbc.edu
Description:
            a game of wordsearch
"""

# used to tell the program when player is done inputting words
STOP_PARAM = 'nomore'

DEFAULT_SPACE = ' '


def get_words():
    """
    Obtains the words a player would like to search for
    :return: words_lists
    """

    words_list = []  # given words can be a list of lists

    word = input("Enter a word you'd like to put into the word search (enter 'nomore' to finish): ")

    # while word does not equal stop param, keep adding words to words_list
    while word != STOP_PARAM:
        words_list.append(word)
        word = input("Enter a word you'd like to put into the word search (enter 'nomore' to finish): ")

    return words_list


def generate_board(words_list):
    """
    Size of the board depends on the area of words in words_list
    :return: grid of size equal to a multiple of the combined area of words in words list.
    """

    combined_area = 0

    for word in words_list:
        combined_area += len(word)

    # generate board size based on area of words_list
    # grid size is twice the area of words_list
    size = 2 * combined_area

    print(f'The size will be {size} units.')
    print(f'The combined area was {combined_area} units.')

    """grid = []
    row = []

    # make each row up of spaces, then make the grid up of rows.
    for i in range(len(size)):

        grid.append(row)

        for e in range(len(size)):

            row.append(DEFAULT_SPACE)

    print(grid)"""


if __name__ == '__main__':

    # Allow player to input words into list of words called given words
    generate_board(get_words())

    # Generate board
    # Give player board to solve
    # Play game
    # End game when player solves board

    pass