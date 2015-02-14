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
import Tiles
import Player
import random

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

        # Store the screen for access in other methods
        self.screen = screen

        # Set the font we will use for text (font, size, bold, italic)
        self.font = pygame.font.SysFont('Arial', 25, False, False)

        # Initialize the debug text
        self.debug_text = "Testing"

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

        # Draw the initial board
        self.draw()

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

        # Figure out the starting coordinates for the upper left
        # empty quadrant
        row = 0
        col = 0
        (width, height) = self.board[row][col].get_size()
        (x, y) = self.board[row][col].get_position()
        x += width
        y += height

        # Generate the text for the active player
        text = self.font.render("Player #%d" % (self.player+1),
                                True, (255, 255, 255))

        # Add the text to the screen
        self.screen.blit(text, (x, y))

        # Figure out the starting coordinate for the upper right
        # empty quadrant
        row = 0
        col = len(self.board[row]) / 2
        (width, height) = self.board[row][col].get_size()
        (x, y) = self.board[row][col].get_position()
        x += width
        y += height

        # Generate the text for the debug
        text = self.font.render(self.debug_text, True, (255, 255, 255))

        # Add the text to the screen
        self.screen.blit(text, (x, y))

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
        None
        """

        # If the mouse is clicked we need to see if we recognize
        # what was clicked
        if clicked is True:

            # Reinitialize the debug text
            self.debug_text = ""

            # Get the mouse position
            pos = pygame.mouse.get_pos()

            # Loop through all of the tiles on the game board
            for row in range(len(self.board)):
                for col in range(len(self.board[row])):
                    if self.board[row][col] is not None:

                        # Get the tile clicked status
                        (is_clicked, text, headquarter) = \
                            self.board[row][col].clicked(pos)

                        # If clicked, set the text to display
                        if is_clicked:

                            # Store the debug text
                            self.debug_text = text
                            if headquarter is True:
                                self.debug_text += " (Headquarter)"

                            # Move the player piece
                            self.players[self.player].set_location((row, col))

                            # Move next player
                            self.player = (self.player + 1) % len(self.players)

                            # Redraw the board
                            self.draw()


################################################################################
# Functions
################################################################################


################################################################################
# Main
################################################################################
if __name__ == "__main__":

    print "This Python module cannot be executed standalone!"
