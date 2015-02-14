"""
Module:
WelcomeScreen.py

Author:
Mark Nauman

Description:
Contains the class to handle the welcome screen.

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

class WelcomeScreen:
    """
    Class Name:
    WelcomeScreen

    Base Class:
    None

    Description:
    Define the base class for the welcome page
    """

    def __init__(self, screen):
        """
        Method Name:
        __init__

        Description:
        Initialize the class objects.  Also, drawing the welcome screen
        here since we should only have to do it once (not every iteration)

        Inputs:
        screen - screen to draw the welcome page on

        Outputs:
        None
        """

        # Store the screen for access in other methods
        self.screen = screen

        # Set the colors
        self.title_color = (255, 255, 255)
        self.players_color = (255, 255, 255)

        # Set the title text
        self.title = ["Team #1", "Presents", "Trivial Pursuit"]

        # Array to store the player buttons
        self.players = [None, None, None]

        # Number of players selected
        self.num_players = 0

        # Set the font we will use for printing text (font, size, bold, italic)
        font = pygame.font.SysFont('Arial', 80, False, False)

        # Get the screen size
        (width, height) = self.screen.get_size()

        # Wipe the screen clean
        self.screen.fill((0, 0, 0))

        # First half of the screen is reserved for the title.  Figure out the
        # y coordinate for the first line of the title text.
        y_offset = (height / 2) / (len(self.title)+1)
        y = y_offset

        # Generate the title
        for line in self.title:

            # Generate the text to display on the screen
            text = font.render(line, True, self.title_color)

            # Figure out the x coordinate
            x = (width - text.get_width()) / 2

            # Add it to the screen
            self.screen.blit(text, (x, y))

            # Move the y coordinate
            y += y_offset

        # Second half of the screen is reserved for player selection.  Figure
        # out the y coordinate for the first line of the text.
        y_offset = (height / 2) / 3
        y = (height / 2) + y_offset

        # Generate the text to ask for the number of players
        text = font.render("How Many Players?", True, self.players_color)

        # Figure out the x coordinate
        x = (width - text.get_width()) / 2

        # Add it to the screen
        self.screen.blit(text, (x, y))

        # Move the y coordinate
        y += y_offset

        # Figure out the x coordinate for the first number of players
        # select
        x_offset = width / (len(self.players)+1)
        x = x_offset

        # Generate the player selection options
        for index in range(len(self.players)):

            # Generate the text to display on the screen
            text = font.render("%d" % (index+2), True, self.players_color)

            # Add it to the screen
            self.players[index] = self.screen.blit(text, (x, y))

            # Move the x coordinate
            x += x_offset

    def execute(self, clicked):
        """
        Method Name:
        execute

        Description:
        If the mouse is clicked it will determine if the user selected a
        valid option.

        Inputs:
        clicked - flag to indicate if the screen was clicked

        Outputs:
        True if an action was performed, else False
        """

        # If the mouse is clicked we need to see if we recognize
        # what was clicked
        if clicked is True:

            # Get the mouse position
            pos = pygame.mouse.get_pos()

            # See if any of the player options was clicked
            for index in range(len(self.players)):

                # Was this one clicked?
                if self.players[index].collidepoint(pos):

                    # Store the number of players
                    self.num_players = index+2
                    return True

        # If we got this far, nothing has happened
        return False

    def get_num_players(self):
        """
        Method Name:
        get_num_players

        Description:
        Returns the number of players that will be playing the game

        Inputs:
        None

        Outputs:
        self.num_players
        """

        return self.num_players

################################################################################
# Functions
################################################################################

# No functions.  Everything is in classes above.

################################################################################
# Main
################################################################################
if __name__ == "__main__":

    print "This Python module cannot be executed standalone!"
