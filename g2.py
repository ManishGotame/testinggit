import pygame
from light import tracking
#import pyfirmata as fir
#board = fir.Arduino('COM3')
#led = board.get_pin('d:6:o')

pygame.init() # initialize the pygame
background = 25,0,0
# create the screen
screen = pygame.display.set_mode((1366, 768))
# width, height

pygame.display.set_caption("MymYGame")
icon = pygame.image.load('intro_ball.gif')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("intro_ball.gif")
playerX = 300 
playerY = 280
# ends here
playerChange = 0
playerChangeY = 0

def player(posX, posY): # blit = draw
    screen.blit(playerImg, (posX, posY))

def runMotor(x,y):
    if x >= 900 and y >= 500:
        led.write(1)
    else:
        led.write(0)

running = True
while running:
    # every event gets logged in pygame.event.get() and we loop throught all the events. A button pressed on the keyboard is called a "keystroke" 
    screen.fill(background)
    for event in pygame.event.get(): # a quit function
        if event.type == pygame.QUIT:
            running = False

        def nope():
            if event.type == pygame.KEYDOWN: # keydown means key being pressed down
                if event.key == pygame.K_LEFT:
                    playerChange = -0.1
                
                elif event.key == pygame.K_RIGHT:
                    playerChange = 0.1
                
                elif event.key == pygame.K_DOWN:
                    playerChangeY = 0.1
                
                elif event.key == pygame.K_UP:
                    playerChangeY = -0.1
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerChange = 0
                    playerChangeY = 0 
    playerX, playerY = tracking()               
    #playerX += playerChange
    #playerY += playerChangeY

    player(playerX, playerY)
    #runMotor(playerX, playerY)
    pygame.display.update()
  





























































