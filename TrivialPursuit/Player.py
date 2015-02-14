"""
Module:
Player.py

Author:
Mark Nauman

Description:
Contains the class for each player.  Keeps track of what questions
have been answered.  Also is responsible for drawing the game piece.

Improvements/Todo:
None at this time
"""

################################################################################
# Dependencies
################################################################################

import pygame


################################################################################
# Variables
################################################################################

# None

################################################################################
# Classes
################################################################################

class Player:
    """
    Class Name:
    Player

    Base Class:
    None

    Description:
    Define the base class for the player
    """

    def __init__(self, player_number, location):
        """
        Method Name:
        __init__

        Description:
        Initialize the player information including
        the player number and questions answered

        Inputs:
        player_number - player number
        location - location tuple (row, col) of the player on the board

        Outputs:
        None
        """

        # Store the player number
        self.player_number = player_number

        # Initialize the questions the player has answered
        self.answered = {
            "People": False,
            "Events": False,
            "Places": False,
            "Holidays": False
        }

        # Store the player location
        self.location = location

    def draw(self, screen, pos, size):
        """
        Method Name:
        draw

        Description:
        Draw the game piece on the screen

        Inputs:
        screen - screen to draw the game piece on
        pos - position of the current tile
        size - size of the current tile

        Outputs:
        None
        """

        # Strip the tuples
        (width, height) = size
        (x_start, y_start) = pos

        # Calculate the game piece size assuming four players and
        # all players are occupying the same tile and 5 pixels pad on
        # each side (<pad><piece><pad><piece><pad>)
        length = (min(width, height) - (3*5)) / 2

        # Calculate the x coordinate
        pad = (width - length - length) / 3
        if (self.player_number == 1) or (self.player_number == 3):
            x = x_start + pad
        else:
            x = x_start + pad + length + pad

        # Calculate the y coordinate
        pad = (height - length - length) / 3
        if (self.player_number == 1) or (self.player_number == 2):
            y = y_start + pad
        else:
            y = y_start + pad + length + pad

        # This is some ugly code to draw the player game piece.
        # needs some logic to add the tiles based on the questions
        # that have been answered
        surface = pygame.Surface((length, length))
        surface.fill((0, 0, 0))
        pygame.draw.rect(surface, (255, 255, 255), (1, 1, length-2, length-2))

        font = pygame.font.SysFont('Arial', length-10, True, False)
        text = font.render("%d" % self.player_number, True, (0, 0, 0))
        x_text = (length - text.get_width()) / 2
        y_text = (length - text.get_height()) / 2
        surface.blit(text, (x_text, y_text))
        screen.blit(surface, (x, y))

    def set_location(self, location):
        """
        Method Name:
        set_location

        Description:
        Set the player location

        Inputs:
        location - location tuple (row, col)

        Outputs:
        None
        """

        self.location = location

    def get_location(self):
        """
        Method Name:
        get_location

        Description:
        Get the player location

        Inputs:
        None

        Outputs:
        self.location
        """

        return self.location

################################################################################
# Functions
################################################################################

# No functions.  Everything is in classes above.

################################################################################
# Main
################################################################################
if __name__ == "__main__":

    print "This Python module cannot be executed standalone!"
