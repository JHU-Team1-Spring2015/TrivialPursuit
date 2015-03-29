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
import pymsgbox

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

    # Define the wedges [(color tuple), [quadrant]].  This could
    # be a helper class, but okay for now as a simple array since only
    # two elements
    colors = {
        "People": [(255, 0, 0), [0, 0]],      # Red
        "Events": [(255, 255, 255), [1, 0]],  # White
        "Places": [(0, 0, 255), [0, 1]],      # Blue
        "Holidays": [(0, 255, 0), [1, 1]]     # Green
    }

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

        # Get the player name to make things a bit more personal
        self.name = pymsgbox.prompt("Enter Player Name?", "Player Name?",
                                    "Player #%d" % player_number)

        # Error check if they hit cancel
        if self.name is None:
            self.name = "Player #%d" % player_number

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
        # all players are occupying the same tile and 3 pixels pad on
        # each side (<pad><piece><pad><piece><pad>)
        length = (min(width, height) - (3*3)) / 2

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

        # Create the player piece surface as a black rectangle
        surface = pygame.Surface((length, length))
        surface.fill((0, 0, 0))

        # Create the player piece wedges
        for category in self.answered.keys():

            # If the player has answered this question
            if self.answered[category] is True:

                # Get the color and quadrant
                wedge_color = self.colors[category][0]
                wedge_quadrant = self.colors[category][1]

                # Calculate the wedge size assuming with 2 pixels pad on
                # each side (<pad><wedge><pad><wedge><pad>)
                wedge_pad = 2
                wedge_size = (length - 3 * wedge_pad) / 2

                # Calculate the wedge position based on the quadrant
                wedge_x = wedge_pad + ((wedge_size + wedge_pad) * wedge_quadrant[0])
                wedge_y = wedge_pad + ((wedge_size + wedge_pad) * wedge_quadrant[1])

                # Draw the wedge
                pygame.draw.rect(surface, wedge_color,
                                 (wedge_x, wedge_y, wedge_size, wedge_size))

        font = pygame.font.SysFont('Arial', length-10, True, False)
        text = font.render("%d" % self.player_number, True, (150, 150, 150))
        x_text = (length - text.get_width()) / 2
        y_text = (length - text.get_height()) / 2
        surface.blit(text, (x_text, y_text))
        screen.blit(surface, (x, y))

    def add_wedge(self, category):
        """
        Method Name:
        add_wedge

        Description:
        Add a scoring wedge to the player piece

        Inputs:
        category - question category to add the wedge

        Outputs:
        None
        """

        self.answered[category] = True

    def can_win(self):
        """
        Method Name:
        can_win

        Description:
        Determine if the player can win (i.e., has all scoring wedges)

        Inputs:
        category - question category to add the wedge

        Outputs:
        None
        """

        # Determine if the user has answered all of the questions
        can_win = True
        for category in self.answered.keys():
            if self.answered[category] is False:
                can_win = False

        # Return the status
        return can_win

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

    def get_name(self):
        """
        Method Name:
        get_name

        Description:
        Get the player name

        Inputs:
        None

        Outputs:
        self.name
        """

        return self.name

################################################################################
# Functions
################################################################################

# No functions.  Everything is in classes above.

################################################################################
# Main
################################################################################
if __name__ == "__main__":

    print "This Python module cannot be executed standalone!"
