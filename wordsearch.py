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

# stuff_list indexes
NUM_WORDS_INDEX = 1
WORDS_LIST_INDEX = 0


def get_words():
    """
    Obtains the words a player would like to search for
    :return: words_lists
    """

    words_list = []  # given words can be a list of lists

    word = input("Enter a word you'd like to put into the word search (enter 'nomore' to finish): ")

    num_words = 0
    # while word does not equal stop param, keep adding words to words_list
    while word != STOP_PARAM:
        words_list.append(word)
        num_words += 1
        word = input("Enter a word you'd like to put into the word search (enter 'nomore' to finish): ")

    return words_list


def generate_board(word_list):
    """
    Size of the board depends on the area of words in words_list
    :return: grid of size equal to a multiple of the combined area of words in words list.
    """

    # the combined area of every letter in each word entered by the user into words_list
    combined_area = 0

    for word in word_list:

        combined_area += len(word)

    # generate board size based on area of words_list
    # grid size is twice the area of words_list
    size = 2 * combined_area

    print(f'The size will be {size} units.')
    print(f'The combined area was {combined_area} units.')

    # length and width of the board
    length = 0
    width = 0

    # grid area is the product of board length and width
    grid_area = 0

    # begin at an area of none, then increase both len and width by one until you have the parameters of a square
    # grid that is not less than size.
    while grid_area < size:
        length += 1
        width += 1

        grid_area = length * width

    # length of grid and width of grid should be generated
    grid_len = length
    grid_width = width

    # the grid of the board begins as empty and its final size is determined by combined area of
    the_grid = []

    for x in range(grid_len):

        grid_row = []
        for y in range(grid_width):

            grid_row.append(DEFAULT_SPACE)

        the_grid.append(grid_row)

    """
    grid = []
    row = []
    
    # make each row up of spaces, then make the grid up of rows.
    for i in range(len(size)):
    
        grid.append(row)
    
        for e in range(len(size)):
    
            row.append(DEFAULT_SPACE)
    
    print(grid)
    """

    return the_grid


if __name__ == '__main__':

    # Allow player to input words into list of words called given words
    print(generate_board(get_words()))

    # Generate board
    # Give player board to solve
    # Play game
    # End game when player solves board

    pass