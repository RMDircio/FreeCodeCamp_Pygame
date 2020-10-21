import pygame
import os
import random
import math
from pygame import mixer


# Initialize pygame
pygame.init()

os.environ["SDL_VIDEODRIVER"] = "dummy"


# create a window screen for the game
screen = pygame.display.set_mode((800, 600)) # (width, height)

# background music
mixer.music.load('romariogrande__alien-dream.wav')
mixer.music.play(-1) # -1 means play on loop

# background image
# background = pygame.image.load('space-background-with-ficti.png')
# background = pygame.image.load('3d-space-background-with-fictional-planets-night-sky.png')
# background = pygame.image.load('8725.eps')
background = pygame.image.load('8725.png')
background = pygame.image.load('hubble_constellations_galaxy_133115_800x600.png')

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

# set player score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32) # (font name, size)
# set where text should be
textX = 10
textY = 10

# free fonts - dafont.com
def show_score(x,y):
    score = font.render('Score: ' + str(score_value), True, (255,255,255)) # (text to display, should display, color)
    screen.blit(score, (x, y))

def player(x,y):
    # draw (blit) the player on screen
    screen.blit(player_img, (x, y)) # image and coordinates



# Alien Icon
# Alien Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
# multiple aliens
alien_img = []
alienX = []
alienY = []
alienX_change = [] 
alienY_change = []
num_of_aliens = 6

for i in range(num_of_aliens):
    # icon
    alien_img.append(pygame.image.load('alien.png'))
    # location - make this random
    alienX.append(random.randint(0, 735)) # left=0 right=800
    alienY.append(random.randint(50, 150)) # top=0 bottom=600
    alienX_change.append(0.8)
    alienY_change.append(20)


def alien(x,y, i):
    # draw (blit) the alien on screen
    screen.blit(alien_img[i], (x, y)) # image and coordinates


# laser Icon
laserImg = pygame.image.load('laser.png')
laserX = 0
laserY = 500 # set to equal player
laserX_change = 0 # laser do not move on the x axis
laserY_change = 2
# ready state = not visible  -  Fire state is visible and moving
laser_state = 'ready'

def fire_laser(x, y):
    global laser_state # grab the global state
    laser_state = 'fire'
    screen.blit(laserImg, (x + 16, y + 10)) # draw laser with centered above player corridnates


# collision - https://www.mathplanet.com/education/algebra-2/conic-sections/distance-between-two-points-and-the-midpoint
def is_collision(alienX, alienY, laserX, laserY):
    # use equation
    distance = math.sqrt((math.pow(laserX - alienX, 2)) + (math.pow(laserY - alienY, 2)))
    if distance < 27: # if laser hits alien
        return True
    else:
        return False

    

# game loop
running = True
while running:
    # background - must be first
    screen.fill((0, 150, 100)) # RGB colors 0-255 (red, green, blue)
    screen.blit(background, (0,0)) # set the coordinates (top left) of where background picture should sit

    
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
                playerX_change = -2.5 # left movement speed
            
            if event.key == pygame.K_RIGHT: # if key pressed was right arrow
                # print('right arrow was pressed')
                playerX_change = 2.5 # right movement speed
            
            if event.key == pygame.K_SPACE: # if key pressed is SPACE BAR
                # keep laser from always being in fire position
                if laser_state is 'ready': # is laser on screen already? if not move on
                    laser_sound = mixer.Sound('sunnyflower__laser-gun.wav') # set laser sound
                    laser_sound.play()
                    laserX = playerX # reset laser X value to equal player
                    fire_laser(laserX, laserY) # fire laser - keep laser in straight line

        
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

    # add alien - must be after screen fill
    for i in range(num_of_aliens):
        alienX[i] += alienX_change[i] # location of alien dependant on X_change

        # set boundaries for alien
        if alienX[i] <= 0:
            alienX_change[i] = 0.8 # move to the right after hitting left wall
            alienY[i] += alienY_change[i]  # move alien down
        elif alienX[i] >= 736: # 64 pixels - 800 pixels = 763
            alienX_change[i] = -0.8 # move to the left after hitting right wall
            alienY[i] += alienY_change[i] # move alien down
        
        # collision checks
        collision = is_collision(alienX[i], alienY[i], laserX, laserY)
        if collision: # if laser hits
            boom_sound = mixer.Sound('anomaex__sci-fi-explosion.wav') # set explosion sound
            boom_sound.play()
            laserY = 500 # reset laser
            laser_state = 'ready'
            score_value += 1 # add to score for each hit
            # respawn the alien
            alienX[i] = random.randint(0, 736) # left=0 right=800
            alienY[i] = random.randint(50, 150) # top=0 bottom=600
        
        alien(alienX[i], alienY[i], i)

    # laser movement
    # when laser gets to top of screen
    if laserY <=0:
        laserY = 500 # set to equal player
        laser_state = 'ready'

    if laser_state is 'fire':
        fire_laser(laserX,laserY)
        laserY-= laserY_change # decrease Y to make laser move up


    player(playerX, playerY)
    show_score(textX, textY)
   
    # this updates the screen
    pygame.display.update()



# <a href='https://www.freepik.com/photos/background'>Background photo created by kjpargeter - www.freepik.com</a>

# <a href='https://www.freepik.com/vectors/background'>Background vector created by rawpixel.com - www.freepik.com</a>



# https://wallpaperscraft.com/download/hubble_constellations_galaxy_133115/800x600


# Bullet
# Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>


