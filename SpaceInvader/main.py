import pygame
import os

# Initialize pygame
pygame.init()

os.environ["SDL_VIDEODRIVER"] = "dummy"


# create a window screen for the game
screen = pygame.display.set_mode((800, 600)) # (width, height)

# title
pygame.display.set_caption('Space Invaders')

# set icon
# Icon is from Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
icon = pygame.image.load('space-invaders-icon32.png')
pygame.display.set_icon(icon)


# Player's Ship Icon
# player spaceship from Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
player_img = pygame.image.load('player-space-ship64.png')
# location - middle and lower half of screen
playerX = 370 # left=0 right=800
playerY = 500 # top=0 bottom=600

# player location change
playerX_change = 0


def player(x,y):
    # draw (blit) the player on screen
    screen.blit(player_img, (x, y)) # image and coordinates


# game loop
running = True
while running:
    # background - must be first
    screen.fill((0, 150, 100)) # RGB colors 0-255 (red, green, blue)

    
    # EVENTS
    for event in pygame.event.get(): # checks all events
        # close the game down
        if event.type == pygame.QUIT: # check to see if close button is clicked
            running = False # will stop game
    
        # Keystrokes
        if event.type == pygame.KEYDOWN: # if any key was pressed
            # print('Non Directional key was pressed')
            
            if event.key == pygame.K_LEFT: # if key pressed was left arrow
                # print('left arrow was pressed')
                playerX_change = -0.3 # left movement speed
            
            if event.key == pygame.K_RIGHT: # if key pressed was right arrow
                # print('right arrow was pressed')
                playerX_change = 0.3 # right movement speed
        
        if event.type == pygame.KEYUP: # if any key was released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    # print('Keystoke was released')
                    playerX_change = 0 # stops movement when key is released
    
    # move right
    # increase playerX continuously to the right
    # playerX += 0.1

    # move left
    # decrease playerX continuously to the left
    # playerX -= 0.1

    # move up
    # increase playerY continuously up
    # playerY -= 0.1
    
    # move down
    # increase playerY continuously down
    # playerY += 0.1

    # add player - must be after screen fill
    playerX += playerX_change # location of player dependant on X_change

    # set boundaries for player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: # 64 pixels - 800 pixels = 763
        playerX = 736

    player(playerX, playerY)
    
    # this updates the screen
    pygame.display.update()















