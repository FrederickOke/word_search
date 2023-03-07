import random

# number of inputs to request
NUM_COORDS = 2 # number of inputs requested for a coordinate pair

# used to tell the program when player is done inputting words
STOP_PARAM = 'nomore'
DEFAULT_SPACE = ' '

# stuff_list indexes
NUM_WORDS_INDEX = 1
WORDS_LIST_INDEX = 0

WORD_START_INDEX = 0
X_COORD_INDEX = 0
Y_COORD_INDEX = 1

# orientation directions
RIGHT = 2
UP_RIGHT = 1
UP = 8
LEFT_UP = 7
LEFT = 5
LEFT_DOWN = 6
DOWN = 3
DOWN_RIGHT = 4

#ascii values
MINIMUM_ASCII = 97
MAXIMUM_ASCII = 122

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

        #fill board with whitespace
        self.fill_whitespace()

    #take turns
    def take_turn(self):
        gameover = False
        guess = []
        """
        Allows the player to designate the beginning and end coordinates of their guess, and updates display if neccessary
        :return: bool - whether the game should be continued or not after the current turn is completed
        """

        #test
        print ("Test: make a downward guess")

        #Find the start of the guess
        guess_start_x = int(input("What is the x coordinate of the start of your guess?"))
        #while coordinate is out of bounds
        while ( (guess_start_x < 0) or (guess_start_x > self.grid_side - 1) ):
            guess_start_x = int(input("Invalid input: please pick an x coordinate in bounds"))

        guess_start_y = int(input("What is the y coordinate of the start of your guess?"))
        #while coordinate is out of bounds
        while ( (guess_start_y < 0) or (guess_start_y > self.grid_side - 1) ):
            guess_start_y = int(input("Invalid input: please pick a y coordinate in bounds"))

        guess_start = (guess_start_x, guess_start_y)

        #Find the end of the guess
        #while coordinate is out of bounds
        guess_end_x = int(input("What is the x coordinate of the end of your guess?"))
        while ((guess_end_x < 0) or (guess_end_x > self.grid_side - 1)):
            guess_end_x = int(input ("Invalid input: please pick an x coordinate in bounds"))

        guess_end_y = int(input("What is the y coordinate of the end of your guess?"))
        while ((guess_end_y < 0) or (guess_end_y > self.grid_side -1)):
            guess_end_y = int(input ("Invalid input: please pick a y coordinate in bounds"))

        guess_end = (guess_end_x, guess_end_y)


        #orthogonal guesses
        #left

        #right
        #up

        #down
        if (guess_end(X_COORD_INDEX) - guess_start(X_COORD_INDEX)) > 0:

            if (guess_end(Y_COORD_INDEX) == guess_start(Y_COORD_INDEX)):

                for i in range(guess_start(X_COORD_INDEX), guess_end(X_COORD_INDEX)):
                    guess.append(self.grid[i][guess_end_y])
        #diagonal guesses
        #left

        return gameover

    #display board
    def display_board(self):
        """
        Displays the updated board and
        """

        #print out the board
        for x in range(0, self.grid_side):
            print(self.grid[x])

        #print out a list of words yet to be found
        print("\nWord List: ")
        for word in self.word_list:
            print(f"{word}")

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
            words_list.append(word.lower())
            num_words += 1
            word = input("Enter a word you'd like to put into the word search (enter 'nomore' to finish): ")

        return words_list

    #run the game
    def run_game(self):
        """
        Runs the game.
        :return: none
        """
        game_over = False
        while not game_over:
            self.display_board()
            if not self.take_turn():
                game_over = True

        if game_over:
            print("\nThank You for Playing!")



        # TEST to see if grid made correctly
        #print("run_game() called")
        #print("Observe if game board has been made correctly")
        #print('TEST: GRID APPEARANCE BELOW')
        #print(f"self.grid_side = {self.grid_side} units")



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
        # TEST: see if more size ends the looping problem

        multiplier = 4
        size = multiplier * combined_area

        #print(f"The size is {multiplier} times the combined area.")
        #print(f'The combined area was {combined_area} units.')
        #print(f'The size will be {size} units.')

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
        #print('TEST: GRID APPEARANCE BELOW')
        #for x in range(0, self.grid_side):
        #    print(the_grid[x])

        #returns an empty board of adequate size
        return the_grid

    #populate the board with words
    def populate_board(self):
        """
        Populates the board with words in random orientations, leaving blank in all other coordinate spaces
        :return: grid populated with designated words in random orientations
        """

        #TEST: tell me we are here
        #   print("populate_board() called")

        # choose a random unpopulated coordinate,
        # do not move onto next word until an orientation for the current is found

        for i in range(0, len(self.word_list)):
            #TEST: tell me what loop we are on
            #print(f"Current loop is loop {i}")

            # continue trying to find an orientation until a place is found
            place_found = False

            #TEST: tell me when while loop starts
            #print("While loop has started.")
            while not place_found:
                #continue picking cords within bounds
                x_cord = random.randint(0, self.grid_side - 1)
                y_cord = random.randint(0, self.grid_side - 1)

                #TEST: tell me what coord we are on.
                #print(f"Trying x_coord:{x_cord}, y_coord:{y_cord}.")

                #try to place if an empty place is found
                if (self.grid[x_cord][y_cord] == DEFAULT_SPACE):
                    #TEST: tell me if recursive call has activated
                    #print("recursive call will activate")

                    #returns valid orientation or -1
                    direction = self.find_orient(x_cord, y_cord, i, direction = 1)

                    #if the orientation is -1 we break this loop and try again. else, proceed with this orientation
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
        #RECURSIVE CASE: current orientation ubstructed and not all directions checked.
        if (self.check_orient(x_cord, y_cord, direction, word_list_index) == False) and (direction < 8):
            return self.find_orient(x_cord, y_cord, word_list_index, direction + 1)

        #BASE CASE: current orientation unobstructed or all directions checked
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
            if (0 <= (x - (len(self.word_list[word_list_index]) + 1))) and (
                    (y + (len(self.word_list[word_list_index]) - 1)) <= len(self.grid) - 1):

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
            if (0 <= (x - (len(self.word_list[word_list_index]) + 1))):

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
            if (0 <= (x - (len(self.word_list[word_list_index]) + 1))) and (
                    0 <= (y - (len(self.word_list[word_list_index]) + 1))):

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
            if (0 <= (y - (len(self.word_list[word_list_index]) + 1))):

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
            if ((x + (len(self.word_list[word_list_index]) - 1)) < len(self.grid) - 1) and (
                    0 <= (y - (len(self.word_list[word_list_index]) + 1))):

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
            if ((x + (len(self.word_list[word_list_index]) - 1)) < len(self.grid) - 1) and (y + (len(self.word_list[word_list_index]) - 1) < len(self.grid) - 1):

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
            for e in range(x, x - len(self.word_list[word_list_index]), -1):
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
                self.grid[e][y - index_step] = self.word_list[word_list_index][WORD_START_INDEX + index_step]
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
        For each empty space on the grid randomly fill it with an lowercase alphabetical character
        """
        for x in range (0, self.grid_side):
            for y in range (0, self.grid_side):
                if (self.grid[x][y] == DEFAULT_SPACE):
                    self.grid[x][y] = chr(random.randint(MINIMUM_ASCII, MAXIMUM_ASCII))


if __name__ == '__main__':

    WordSearchGame().run_game()

    # make a board based off of the combined area of all words given by player
    # Give player board to solve
    # Play game
    # End game when player solves board
