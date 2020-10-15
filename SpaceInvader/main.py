import pygame
import os

# Initialize pygame
pygame.init()

os.environ["SDL_VIDEODRIVER"] = "dummy"


# create a window screen for the game
screen = pygame.display.set_mode((800, 600)) # height and width

# when the game is running
running = True
while running:
    # events
    for event in pygame.event.get(): # checks all events
        if event.type == pygame.QUIT: # check to see if close button is clicked
            running = False # will stop game
