"""
File:       wordsearch.py
Author:     Frederick Oke
Date:       7/8/2021
E-mail:     foke1@umbc.edu
Description:
            a game of wordsearch
"""

import random

# used to tell the program when player is done inputting words
STOP_PARAM = 'nomore'
DEFAULT_SPACE = ' '

# stuff_list indexes
NUM_WORDS_INDEX = 1
WORDS_LIST_INDEX = 0

WORD_START_INDEX = 0

# orientation directions
RIGHT = 1
UP_RIGHT = 2
UP = 3
LEFT_UP = 4
LEFT = 5
LEFT_DOWN = 6
DOWN = 7
DOWN_RIGHT = 8

class WordSearchGame:
    """
    Class for all things related to the game. Created primarily for the game board
    :return: none
    """
    def __init__(self):
        #hold a list of words for the game
        self.word_list = self.get_words()
        #length and width of the square grid
        self.grid_side = 0
        #create an empty board for the game
        self.grid = self.generate_grid()
        #make grid of adequate size

        #populate the board with words
        self.populate_board()

    #get a list of words for the game
    def get_words(self):
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

    #run the game
    def run_game(self):
        """
        Runs the game.
        :return: none
        """
        pass


    def generate_grid(self):
        """
        Size of the board depends on the area of words in words_list
        :return: grid of size equal to a multiple of the combined area of words in words list.
        """
        # the combined area of every letter in each word entered by the user into words_list
        combined_area = 0
        for word in self.word_list:
            combined_area += len(word)

        # generate board size based on area of words_list
        # grid size is twice the area of words_list
        multiplier = 4
        size = multiplier * combined_area

        # grid area is the product of (a side of the grid)^2
        grid_area = 0

        # begin at an area of none, then increase both len and width by one until you have the parameters of a square
        # grid that is not less than size.
        while grid_area < size:
            self.grid_side += 1
            grid_area = self.grid_side ** 2

        # the grid of the board begins as empty and its final size is determined by combined area of
        the_grid = []
        for x in range(self.grid_side):
            grid_row = []
            for y in range(self.grid_side):
                grid_row.append(DEFAULT_SPACE)
            the_grid.append(grid_row)

        #TEST to see if grid made correctly
        print('TEST: GRID APPEARANCE BELOW')
        for x in range(0, self.grid_side):
            print(the_grid[x])

        #returns an empty board of adequate size
        return the_grid

    #populate the board with words
    def populate_board(self):
        """
        Populates the board with words in random orientations, leaving blank in all other coordinate spaces
        :return: grid populated with designated words in random orientations
        """

        # choose a random unpopulated coordinate,
        # do not move onto next word until an orientation for the current is found

        for i in range(0, len(self.word_list)):

            # continue trying to find an orientation until a place is found
            place_found = False

            while not place_found:
                #continue picking cords within bounds
                x_cord = random.randint(0, self.grid_side - 1)
                y_cord = random.randint(0, self.grid_side - 1)

                if (self.grid[x_cord][y_cord] == DEFAULT_SPACE):

                    #returns valid orientation or -1
                    direction = self.find_orient(x_cord, y_cord, i, direction = 1)

                    #if the the orientation is -1 we break this loop and try again. else, proceed with this orientatio
                    #then break the loop to begin the same for the next word
                    if direction != -1:

                        #breaks the loop
                        place_found = True
                        self.place_orient(x_cord, y_cord, direction, i)

    #HELPER FUNCTIONS OF POPULATE_BOARD() FUNCTION
    def find_orient(self, x_cord, y_cord, word_list_index, direction):
        """
        Recursively attempts to orient the word in one of 8 directions
        :return: int oriented direction 1-8 if found, -1 otherwise
        """
        #make sure to set d outside of fn call in run_game
        #RECURSIVE CASE current orientation ubstructed and not all directions checked.
        if (self.check_orient(x_cord, y_cord, direction, word_list_index) == False) and (direction < 8):
            return self.find_orient(x_cord, y_cord, word_list_index, direction + 1)

        #BASE CASE current orientation unobstructed or all directions checked
        elif (self.check_orient(x_cord, y_cord, direction, word_list_index)):
            return direction

        else:
            #invalid direction
            return -1

    def check_orient(self, x, y, d, word_list_index):
        """
        Recursively checks that there are no obstructions to orientation and that it stays within bounds
        :return: bool whether there exists space for the word in this orientation or not
        """

        can_fit = True
        #check word is in bounds based on orientation
        #remember x will be up and down, y will be left to right

        #cardinal horizontal
        if (d == RIGHT):
            # check bounds s.t. entire word fits
            if ((y + (len(self.word_list[word_list_index]) - 1)) < len(self.grid)):

                # check each space below starting position for the length of the ship to see if the word will fit
                for i in range(y, y + len(self.word_list[word_list_index])):

                    if self.grid[x][i] != DEFAULT_SPACE:
                        can_fit = False

                        # return that the word is obstructed in this orientation
                        return can_fit

                # if it can fit then place it on the board
                return can_fit

            else:
                can_fit = False
                return can_fit

        if (d == UP_RIGHT):
            # check bounds s.t. entire word fits
            if (0 <= (x - (len(self.word_list[word_list_index]) - 1))) and (
                    (y + (len(self.word_list[word_list_index]) - 1)) <= len(self.grid)):

                # check each space below starting position for the length of the ship to see if the word will fit
                y_step = 0
                for i in range(x, x - len(self.word_list[word_list_index]), -1):

                    if self.grid[i][y + y_step] != DEFAULT_SPACE:
                        can_fit = False

                        # return that the word is obstructed in this orientation
                        return can_fit

                    y_step += 1

                # if it can fit then place it on the board
                return can_fit

            else:
                can_fit = False
                return can_fit

        if (d == UP):
            # check bounds s.t. entire word fits
            if (0 <= (x - (len(self.word_list[word_list_index]) - 1))):

                # check each space below starting position for the length of the ship to see if the word will fit
                for i in range(x, x - len(self.word_list[word_list_index]), -1):

                    if self.grid[i][y] != DEFAULT_SPACE:
                        can_fit = False

                        # return that the word is obstructed in this orientation
                        return can_fit

                # if it can fit then place it on the board
                return can_fit

            else:
                can_fit = False
                return can_fit

        if (d == LEFT_UP):
            # check bounds s.t. entire word fits
            if (0 <= (x - (len(self.word_list[word_list_index]) - 1))) and (
                    0 <= (y - (len(self.word_list[word_list_index]) - 1))):

                # check each space below starting position for the length of the ship to see if the word will fit
                y_step = 0
                for i in range(x, x - len(self.word_list[word_list_index]), -1):

                    if self.grid[i][y - y_step] != DEFAULT_SPACE:
                        can_fit = False

                        # return that the word is obstructed in this orientation
                        return can_fit

                    y_step += 1

                # if it can fit then place it on the board
                return can_fit

            else:
                can_fit = False
                return can_fit

        if (d == LEFT):
            # check bounds s.t. entire word fits
            if (0 <= (y - (len(self.word_list[word_list_index]) - 1))):

                # check each space below starting position for the length of the ship to see if the word will fit
                for i in range(y, y - len(self.word_list[word_list_index]), -1):

                    if self.grid[x][i] != DEFAULT_SPACE:
                        can_fit = False

                        # return that the word is obstructed in this orientation
                        return can_fit

                # if it can fit then place it on the board
                return can_fit

            else:
                can_fit = False
                return can_fit

        if (d == LEFT_DOWN):
            # check bounds s.t. entire word fits
            if ((x + (len(self.word_list[word_list_index]) - 1)) < len(self.grid)) and (
                    0 <= (y - (len(self.word_list[word_list_index]) - 1))):

                # check each space below starting position for the length of the ship to see if the word will fit
                y_step = 0
                for i in range(x, x + len(self.word_list[word_list_index])):

                    if self.grid[i][y - y_step] != DEFAULT_SPACE:
                        can_fit = False

                        # return that the word is obstructed in this orientation
                        return can_fit

                    y_step += 1

                # if it can fit then place it on the board
                return can_fit

            else:
                can_fit = False
                return can_fit

        if (d == DOWN):
            # check bounds s.t. entire word fits
            if ((x + (len(self.word_list[word_list_index]) - 1)) < len(self.grid)):

                # check each space below starting position for the length of the ship to see if the word will fit
                for i in range(x, x + len(self.word_list[word_list_index])):

                    if self.grid[i][y] != DEFAULT_SPACE:
                        can_fit = False

                        #return that the word is obstructed in this orientation
                        return can_fit

                # if it can fit then place it on the board
                return can_fit

            else:
                can_fit = False
                return can_fit

        if (d == DOWN_RIGHT):
            # check bounds s.t. entire word fits
            if ((x + (len(self.word_list[word_list_index]) - 1)) < len(self.grid)) and (y + (len(self.word_list[word_list_index]) - 1) < len(self.grid)):

                # check each space below starting position for the length of the ship to see if the word will fit
                y_step = 0
                for i in range(x, x + len(self.word_list[word_list_index])):

                    if self.grid[i][y + y_step] != DEFAULT_SPACE:
                        can_fit = False

                        # return that the word is obstructed in this orientation
                        return can_fit

                    y_step += 1

                # if it can fit then place it on the board
                return can_fit

            else:
                can_fit = False
                return can_fit

    def place_orient(self, x, y, d, word_list_index):

        if (d == RIGHT):
            index_step = 0
            # place the word on the board in this orientation
            for e in range(y, y + len(self.word_list[word_list_index])):
                self.grid[x][e] = self.word_list[word_list_index][WORD_START_INDEX + index_step]
                index_step += 1

        elif (d == UP_RIGHT):
            index_step = 0
            # place the word on the board in this orientation
            for e in range(x, x + len(self.word_list[word_list_index])):
                self.grid[e][y + index_step] = self.word_list[word_list_index][WORD_START_INDEX + index_step]
                index_step += 1

        elif (d == UP):
            index_step = 0
            # place the word on the board in this orientation
            for e in range(x, x - len(self.word_list[word_list_index]), -1):
                self.grid[e][y] = self.word_list[word_list_index][WORD_START_INDEX + index_step]
                index_step += 1

        elif (d == LEFT_UP):
            index_step = 0
            # place the word on the board in this orientation
            for e in range(x, x + len(self.word_list[word_list_index])):
                self.grid[e][y - index_step] = self.word_list[word_list_index][WORD_START_INDEX + index_step]
                index_step += 1

        elif (d == LEFT):
            index_step = 0
            # place the word on the board in this orientation
            for e in range(y, y - len(self.word_list[word_list_index]), -1):
                self.grid[x][e] = self.word_list[word_list_index][WORD_START_INDEX + index_step]
                index_step += 1

        elif (d == LEFT_DOWN):
            index_step = 0
            # place the word on the board in this orientation
            for e in range(x, x + len(self.word_list[word_list_index])):
                self.grid[e][y + index_step] = self.word_list[word_list_index][WORD_START_INDEX + index_step]
                index_step += 1

        elif (d == DOWN):
            index_step = 0
            # place the word on the board in this orientation
            for e in range(x, x + len(self.word_list[word_list_index])):
                self.grid[e][y] = self.word_list[word_list_index][WORD_START_INDEX + index_step]
                index_step += 1

        elif (d == DOWN_RIGHT):
            index_step = 0
            # place the word on the board in this orientation
            for e in range(x, x + len(self.word_list[word_list_index])):
                self.grid[e][y + index_step] = self.word_list[word_list_index][WORD_START_INDEX + index_step]
                index_step += 1

    def fill_whitespace(self):
        """
        For each empty space on the grid randomly fill it with an uppercase alphabetical character
        """
        pass

if __name__ == '__main__':

    WordSearchGame().run_game()

    # make a board based off of the combined area of all words given by player
    # Give player board to solve
    # Play game
    # End game when player solves board
