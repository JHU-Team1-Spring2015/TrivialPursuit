"""
Module:
GameBoard.py

Author:
Mark Nauman

Description:
This contains the classes for the game board

Improvements/Todo:
None at this time
"""

################################################################################
# Dependencies
################################################################################

import pygame
import pymsgbox
import Tiles
import Player
import random
import Dice
import Questions

################################################################################
# Variables
################################################################################

# None

################################################################################
# Classes
################################################################################


class GameBoard:
    """
    Class Name:
    Board

    Base Class:
    None

    Description:
    Define the base class for the game board
    """

    # Define the game board tiles [[Top Row], [Next Row], ..., [Last Row]]
    board = [
        [   #
            Tiles.People(True),
            Tiles.Events(),
            Tiles.RollAgain(),
            Tiles.Places(),
            Tiles.Holidays(),
            Tiles.Places(),
            Tiles.RollAgain(),
            Tiles.People(),
            Tiles.Events(True)
        ],
        [
            Tiles.Holidays(),
            None,
            None,
            None,
            Tiles.Places(),
            None,
            None,
            None,
            Tiles.Places()
        ],
        [
            Tiles.RollAgain(),
            None,
            None,
            None,
            Tiles.Events(),
            None,
            None,
            None,
            Tiles.RollAgain()
        ],
        [
            Tiles.Events(),
            None,
            None,
            None,
            Tiles.People(),
            None,
            None,
            None,
            Tiles.Holidays()
        ],
        [
            Tiles.Places(),
            Tiles.Events(),
            Tiles.People(),
            Tiles.Holidays(),
            Tiles.Hub(),
            Tiles.Events(),
            Tiles.Places(),
            Tiles.Holidays(),
            Tiles.People()
        ],
        [
            Tiles.Events(),
            None,
            None,
            None,
            Tiles.Places(),
            None,
            None,
            None,
            Tiles.Holidays()
        ],
        [
            Tiles.RollAgain(),
            None,
            None,
            None,
            Tiles.Holidays(),
            None,
            None,
            None,
            Tiles.RollAgain()
        ],
        [
            Tiles.People(),
            None,
            None,
            None,
            Tiles.People(),
            None,
            None,
            None,
            Tiles.Events()
        ],
        [
            Tiles.Holidays(True),
            Tiles.Places(),
            Tiles.RollAgain(),
            Tiles.People(),
            Tiles.Events(),
            Tiles.People(),
            Tiles.RollAgain(),
            Tiles.Holidays(),
            Tiles.Places(True)
        ]
    ]

    # Define the players
    players = []

    def __init__(self, screen, num_players):
        """
        Method Name:
        __init__

        Description:
        Initialize the class objects.  Setup the game board and player objects.

        Inputs:
        screen - screen to draw the welcome page on
        num_players - number of players to create

        Outputs:
        None
        """

        # Initialize the questions
        self.questions = Questions.Questions()

        # Store the screen for access in other methods
        self.screen = screen

        # Set the font we will use for text (font, size, bold, italic)
        self.font = pygame.font.SysFont('Arial', 25, False, False)

        # Initialize the tile sizes and positions
        (screen_width, screen_height) = self.screen.get_size()
        y_pos = 0
        tile_height = screen_height / len(self.board)
        for row in range(len(self.board)):
            x_pos = 0
            tile_width = screen_width / len(self.board[row])
            for col in range(len(self.board[row])):
                if self.board[row][col] is not None:
                    self.board[row][col].initialize((tile_width, tile_height), (x_pos, y_pos))
                x_pos += tile_width
            y_pos += tile_height

        # Figure out where the hub is located
        hub_row = (len(self.board) / 2)
        hub_col = (len(self.board[hub_row]) / 2)

        # Initialize the players
        for player in range(num_players):
            self.players.append(Player.Player(player+1, (hub_row, hub_col)))

        # Starting player is random
        self.player = random.randint(0, num_players-1)

        # Figure out the starting coordinate for the lower right
        # empty quadrant
        row = len(self.board) / 2
        col = len(self.board[row]) / 2
        (width, height) = self.board[row][col].get_size()
        (x, y) = self.board[row][col].get_position()
        x += width
        y += height

        # Figure out the size of the lower right empty quadrant
        row = len(self.board) - 1
        col = len(self.board[row]) - 1
        (width, height) = self.board[row][col].get_position()
        width = width - x
        height = height - y

        # Initialize the dice
        self.dice = Dice.Dice((x, y), (width, height))

        # Draw the initial board
        self.draw()

    def reset(self):
        """
        Method Name:
        reset

        Description:
        Reset the board.  All tiles are inactive and we
        are waiting for a dice to be rolled

        Inputs:
        None

        Outputs:
        None
        """

        # Loop through all of the tiles on the game board and deactivate
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] is not None:
                    self.board[row][col].deactivate()

        # Reset the dice
        self.dice.reset()

    def update_tiles(self, (row, col), x, y, moves):
        """
        Method Name:
        update_tiles

        Description:
        Will update the active and deactivate tiles based on the player
        position and dice roll value

        Inputs:
        (row, col) - current board position
        x - current direction in the x-axis
        y - current direction in the y-axis
        moves - remaining moves

        Outputs:
        None
        """

        # Move the player piece
        row = row + x
        col = col + y

        # If we are outside the board area, quit
        if ((row < 0) or (col < 0) or
                (row >= len(self.board)) or (col >= len(self.board[row]))):
            return

        # If we are on an illegal space, quit
        if self.board[row][col] is None:
            return

        # If we have exhausted all moves, activate the tile and quit
        if moves == 0:
            self.board[row][col].activate()
            return

        # Update the number of moves
        moves -= 1

        # If this is the first move, try all directions
        if (x == 0) and (y == 0):
            self.update_tiles((row, col), -1, 0, moves)
            self.update_tiles((row, col), 1, 0, moves)
            self.update_tiles((row, col), 0, -1, moves)
            self.update_tiles((row, col), 0, 1, moves)

        # If we are moving left or right, try that direction also up and down
        elif x != 0:
            self.update_tiles((row, col), x, 0, moves)
            self.update_tiles((row, col), 0, -1, moves)
            self.update_tiles((row, col), 0, 1, moves)

        # If we are moving up or down, try that direction also left and right
        elif y != 0:
            self.update_tiles((row, col), 0, y, moves)
            self.update_tiles((row, col), -1, 0, moves)
            self.update_tiles((row, col), 1, 0, moves)

    def draw(self):
        """
        Method Name:
        draw

        Description:
        Draw the board on the screen

        Inputs:
        None

        Outputs:
        None
        """

        # Redraw the game board
        self.screen.fill((0, 0, 0))
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] is not None:
                    self.board[row][col].draw(self.screen)

        # Redraw the player pieces
        for player in self.players:

            # Get the player location
            (row, col) = player.get_location()

            # Get the tile position and size
            size = self.board[row][col].get_size()
            position = self.board[row][col].get_position()

            # Draw the player piece
            player.draw(self.screen, position, size)

        # Redraw the dice
        self.dice.draw(self.screen)

        # Figure out the starting coordinates for the upper left
        # empty quadrant
        row = 0
        col = 0
        (width, height) = self.board[row][col].get_size()
        (x, y) = self.board[row][col].get_position()
        x += width
        y += height

        # Generate the text for the active player
        temp = self.players[self.player].get_name()

        # Add the text to the screen
        text1 = self.font.render(temp, True, (255, 255, 255))
        self.screen.blit(text1, (x, y))

        # Also, need to tell the player which piece they are
        temp = "Player Piece #%d" % (self.player+1)

        # Add the text to the screen
        text2 = self.font.render(temp, True, (255, 255, 255))
        self.screen.blit(text2, (x, y + text1.get_height()))

    def execute(self, clicked):
        """
        Method Name:
        execute

        Description:
        If the mouse is clicked it will determine if the user selected a
        valid tile.

        Inputs:
        clicked - flag to indicate if the screen was clicked

        Outputs:
        Name of the game winner
        """

        # If the mouse is clicked we need to see if we recognize
        # what was clicked
        if clicked is True:

            # Get the mouse position
            pos = pygame.mouse.get_pos()

            # Check if the dice was clicked
            roll = self.dice.clicked(pos)
            if roll != 0:

                # Activate/Deactivate tiles
                pos = self.players[self.player].get_location()
                self.update_tiles(pos, 0, 0, roll)

                # Redraw the board
                self.draw()

                # Save some processing and just quit this function
                return None

            # Loop through all of the tiles on the game board
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.board[row][col] is not None:

                        # Get the tile clicked status
                        is_clicked = \
                            self.board[row][col].clicked(pos)

                        # If clicked, set the text to display
                        if is_clicked:

                            return self.update(row, col)

    def update(self, row, col):
        """
        Method Name:
        update

        Description:
        Update the game board based on if the player answers the
        question correctly

        Inputs:
        (row, col) - location of the selected game board tile

        Outputs:
        Name of the game winner
        """

        # Assume not the end of the game
        winner = None

        # Grab the tile type / question category
        tile_type = self.board[row][col].get_type()
        question_category = tile_type

        # Move the player piece
        self.players[self.player].set_location((row, col))

        # If it is a hub tile, we need to select the
        # question category
        if tile_type == "Hub":

            # If the player can win, the other players
            # select the category for the active player
            text = ""
            if self.players[self.player].can_win():
                text = "Other Players, "

            # Generate the text to select a question category
            text += "Please select a question category:\n"

            # Configure the buttons
            buttons = ["People", "Events", "Places", "Holidays"]

            # Display the prompt to the user
            question_category = pymsgbox.confirm(text, "Category?", buttons)

        # If not a roll again tile, ask the player a question
        correct_answer = True
        if tile_type != "Roll Again":

            # Display the question
            correct_answer = self.questions.ask(question_category)

        # If the player answers incorrectly, move to the next player
        if correct_answer is False:

            # Move next player
            self.player = (self.player + 1) % len(self.players)

        # If the tile is a headquarter
        elif self.board[row][col].get_headquarter() is True:

            # Add the scoring wedge
            self.players[self.player].add_wedge(self.board[row][col].get_type())

        # If it is a hub and the player can win the game
        if (tile_type == "Hub") and self.players[self.player].can_win():

                # Set the game winner
                winner = self.players[self.player].get_name()

        # Reset the board
        self.reset()

        # Redraw the board
        self.draw()

        # Return the status
        return winner


################################################################################
# Functions
################################################################################


################################################################################
# Main
################################################################################
if __name__ == "__main__":

    print "This Python module cannot be executed standalone!"
