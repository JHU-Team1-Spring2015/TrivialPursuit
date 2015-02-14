"""
Module:
TrivialPursuit.py

Author:
Mark Nauman

Description:
This is the main program for Team #1's Trivial Pursuit game

Improvements/Todo:
None at this time
"""

################################################################################
# Dependencies
################################################################################

import pygame
import WelcomeScreen
import GameBoard

################################################################################
# Variables
################################################################################

# None

################################################################################
# Classes
################################################################################

################################################################################
# Main
################################################################################
if __name__ == "__main__":

    # Initialize the pygame engine
    pygame.init()

    # Open the screen (resolution, options)
    screen = pygame.display.set_mode((600, 600),
                                     pygame.DOUBLEBUF | pygame.HWSURFACE)

    # Set the window title
    pygame.display.set_caption("Team #1 - Trivial Pursuit")

    # Enable the clock, we will use this later to limit the frame rate
    clock = pygame.time.Clock()

    # Initialize the various variables
    state = 1
    welcome_screen = WelcomeScreen.WelcomeScreen(screen)
    game_board = None

    # Main display loop
    done = False
    while done is False:

        # Process any events that have occurred
        mouse_click = False
        for event in pygame.event.get():

            # If the user wants to quit, let them quit
            if event.type == pygame.QUIT:
                done = True

            # If the left mouse is pressed
            if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
                mouse_click = True

        # If the state is 1 (welcome screen)
        if state == 1:

            # If the user selected number of players
            if welcome_screen.execute(mouse_click):

                num_players = welcome_screen.get_num_players()
                game_board = GameBoard.GameBoard(screen, num_players)
                state += 1

        # If the state is 2 (waiting for dice roll)
        elif state == 2:

            game_board.execute(mouse_click)

        # Copy the window buffer to the main display
        pygame.display.flip()

        # Limit the frame rate so we do not kill the user's CPU
        clock.tick(10)

    # When the above function exits, we are okay to quit
    pygame.quit()
