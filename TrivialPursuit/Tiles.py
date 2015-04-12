"""
Module:
Tiles.py

Author:
Mark Nauman

Description:
This contains the classes for the game board tiles

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


class Tile:
    """
    Class Name:
    Tile

    Base Class:
    None

    Description:
    Define the base class for the game board tiles
    """

    # Set the class object color to black
    color = (0, 0, 0)

    # Set the tile type
    tile_type = "N/A"

    # Set the tile image
    image_file = ""
    image = None

    def __init__(self, headquarter=False):
        """
        Method Name:
        __init__

        Description:
        Initialize the class objects

        Inputs:
        headquarter - optional input parameter to declare if the tile
                      is a head quarters tile

        Outputs:
        None
        """

        # Initialize some of the information
        self.size = (0, 0)
        self.position = (0, 0)
        self.active = False
        self.headquarter = headquarter

        # Initialize the graphics
        self.surface = None
        self.rect = None

    def initialize(self, size, position):
        """
        Method Name:
        initialize

        Description:
        Initialize the tile surface and position

        Inputs:
        size - tile size tuple (width, height) in pixels
        position - tile position tuple (x, y) coordinates in pixels

        Outputs:
        None
        """

        # Store the size and position
        self.size = size
        self.position = position

        # Create the image
        self.image = pygame.image.load(self.image_file).convert()
        self.image = pygame.transform.scale(self.image, self.size)

    def draw(self, screen):
        """
        Method Name:
        draw

        Description:
        Draws the tile to the screen

        Inputs:
        screen - screen to draw the tile on

        Outputs:
        None
        """

        # If the tile is not active, grey out the image
        if self.active is False:
            self.image.set_alpha(50)

        # If the tile is active, set the image to the normal
        else:
            self.image.set_alpha(255)

        # Draw the image to the screen
        self.rect = screen.blit(self.image, self.position)

    def clicked(self, pos):
        """
        Method Name:
        clicked

        Description:
        Determines if the tile was clicked

        Inputs:
        pos - clicked coordinate tuple (x, y) in pixels

        Outputs:
        (True/False, Tile Type, Headquarter)
        True if the tile was clicked; False if not
        Tile Type
        True if the tile is a headquarter tile; False it not
        """

        was_clicked = self.active and self.rect.collidepoint(pos)
        return was_clicked

    def get_size(self):
        """
        Method Name:
        get_size

        Description:
        Get the tile size

        Inputs:
        None

        Outputs:
        self.size
        """

        return self.size

    def get_position(self):
        """
        Method Name:
        get_position

        Description:
        Get the tile position

        Inputs:
        None

        Outputs:
        self.position
        """

        return self.position

    def get_type(self):
        """
        Method Name:
        get_type

        Description:
        Return the tile type

        Inputs:
        None

        Outputs:
        self.tile_type
        """

        return self.tile_type

    def get_headquarter(self):
        """
        Method Name:
        get_headquarter

        Description:
        Return the tile headquarter status

        Inputs:
        None

        Outputs:
        self.headquarter
        """

        return self.headquarter

    def activate(self):
        """
        Method Name:
        activate

        Description:
        Activate this tile

        Inputs:
        None

        Outputs:
        None
        """

        self.active = True

    def deactivate(self):
        """
        Method Name:
        deactivate

        Description:
        Deactivate this tile

        Inputs:
        None

        Outputs:
        None
        """

        self.active = False


class People(Tile):
    """
    Class Name:
    People

    Base Class:
    Tile

    Description:
    Define the class for the people question tiles
    """

    # Set the class object color to red
    color = (255, 0, 0)

    # Set the tile type
    tile_type = "People"

    # Set the tile image file
    image_file = "people.png"


class Events(Tile):
    """
    Class Name:
    Events

    Base Class:
    Tile

    Description:
    Define the class for the event question tiles
    """

    # Set the class object color to white
    color = (255, 255, 255)

    # Set the tile type
    tile_type = "Events"

    # Set the tile image file
    image_file = "events.png"


class Places(Tile):
    """
    Class Name:
    Places

    Base Class:
    Tile

    Description:
    Define the class for the places question tiles
    """

    # Set the class object color to blue
    color = (0, 0, 255)

    # Set the tile type
    tile_type = "Places"

    # Set the tile image file
    image_file = "places.png"


class Holidays(Tile):
    """
    Class Name:
    Holidays

    Base Class:
    Tile

    Description:
    Define the class for the holidays question tiles
    """

    # Set the class object color to green
    color = (0, 255, 0)

    # Set the tile type
    tile_type = "Holidays"

    # Set the tile image file
    image_file = "holiday.png"


class RollAgain(Tile):
    """
    Class Name:
    RollAgain

    Base Class:
    Tile

    Description:
    Define the class for the roll again tiles
    """

    # Set the class object color to grey
    color = (100, 100, 100)

    # Set the tile type
    tile_type = "Roll Again"

    # Set the tile image file
    image_file = "rollagain.png"


class Hub(Tile):
    """
    Class Name:
    Hub

    Base Class:
    Tile

    Description:
    Define the class for the hub tiles
    """

    # Set the class object color to yellow
    color = (255, 255, 0)

    # Set the tile type
    tile_type = "Hub"

    # Set the tile image file
    image_file = "hub.png"


################################################################################
# Functions
################################################################################


################################################################################
# Main
################################################################################
if __name__ == "__main__":

    print "This Python module cannot be executed standalone!"
