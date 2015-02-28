"""
Module:
Dice.py

Author:
Mark Nauman

Description:
Contains the class for the dice.  It draws the graphics and handle
generating the random roll value.

Improvements/Todo:
None at this time
"""

################################################################################
# Dependencies
################################################################################

import pygame
import random

################################################################################
# Variables
################################################################################

# None

################################################################################
# Classes
################################################################################

class Dice:
    """
    Class Name:
    Player

    Base Class:
    None

    Description:
    Define the base class for the player
    """

    def __init__(self, pos, size):
        """
        Method Name:
        __init__

        Description:
        Initialize the dice information including the
        value of the dice roll

        Inputs:
        pos - starting position for the dice icon
        size - size available for the dice icon

        Outputs:
        None
        """

        # Initialize the dice to zero
        self.roll = 0

        # Separate the tuples
        (x, y) = pos
        (width, height) = size

        # Leave a little bit of pad
        pad = 50
        x += pad
        y += pad
        width -= (2 * pad)
        height -= (2 * pad)

        # Store the position and the size
        self.pos = (x, y)
        self.size = (width, height)
        self.rect = None

        # Calculate the space available for the text
        # to print on the dice surface
        pad = 5
        text_width = width - (2 * pad)
        text_height = height - (3 * pad)

        # Goofy loop, but we need to make sure we pick
        # a good font size
        font_size = 50
        while True:

            # Generate the "Roll Dice" text
            self.font = pygame.font.SysFont('Arial', font_size, True, False)
            self.text_roll = self.font.render("Roll", True, (0, 0, 0))
            self.text_dice = self.font.render("Dice", True, (0, 0, 0))

            # If the width is okay
            if ((text_width > self.text_roll.get_width()) and
               (text_width > self.text_dice.get_width())):

                # Calculate the total text height
                total_height = self.text_roll.get_height() + \
                               self.text_dice.get_height()

                # If the height is okay, we can get out of this loop
                if text_height > total_height:
                    break

            # If we get this far, we need to shrink the font and loop
            font_size -= 1

        # X position is calculated as <pad><text><pad>
        x_roll = (width - self.text_roll.get_width()) / 2
        x_dice = (width - self.text_dice.get_width()) / 2

        # Y position is calculated as <pad><text1><pad><text2><pad>
        pad = (height - self.text_roll.get_height() -
               self.text_dice.get_height()) / 3

        y_roll = pad
        y_dice = pad + self.text_roll.get_height() + pad

        # Store
        self.text_roll_pos = (x_roll, y_roll)
        self.text_dice_pos = (x_dice, y_dice)

    def draw(self, screen):
        """
        Method Name:
        draw

        Description:
        Draw the dice on the screen

        Inputs:
        screen - screen to draw the game piece on

        Outputs:
        None
        """

        # Setup the dice surface
        surface = pygame.Surface(self.size)
        surface.fill((255, 255, 255))

        # If the dice has been rolled
        if self.roll != 0:

            # Generate the dice roll value text and center it
            (width, height) = self.size
            text = self.font.render("%d" % self.roll, True, (0, 0, 0))
            x_text = (width - text.get_width()) / 2
            y_text = (height - text.get_height()) / 2
            surface.blit(text, (x_text, y_text))

        # If the dice has not been rolled
        else:

            # Print the roll dice text
            surface.blit(self.text_roll, self.text_roll_pos)
            surface.blit(self.text_dice, self.text_dice_pos)

        # Add the surface to the screen
        self.rect = screen.blit(surface, self.pos)

    def clicked(self, pos):
        """
        Method Name:
        clicked

        Description:
        Determines if the dice was clicked

        Inputs:
        pos - clicked coordinate tuple (x, y) in pixels

        Outputs:
        Dice roll value
        """

        # Can only click if in the initial state and it is clicked
        was_clicked = (self.roll == 0) and self.rect.collidepoint(pos)

        # If clicked, generate the dice roll
        if was_clicked:

            self.roll = random.randint(1, 6)
            return self.roll

        # If not clicked or already clicked return zero
        return 0

    def reset(self):
        """
        Method Name:
        reset

        Description:
        Reset the dice to the initial state

        Inputs:
        None

        Outputs:
        None
        """

        # Reset the dice
        self.roll = 0

################################################################################
# Functions
################################################################################

# No functions.  Everything is in classes above.

################################################################################
# Main
################################################################################
if __name__ == "__main__":

    print "This Python module cannot be executed standalone!"
