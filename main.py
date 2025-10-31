import pygame
import sys
pygame.init()

#Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (34, 34, 34) #222222
FPS = 60

#Display window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Shadows of the Golden Door")

#Clock for controlling frame rate
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Fill the screen with background color
    screen.fill(BACKGROUND_COLOR)
    
    #Update the display
    pygame.display.flip()
    
    #Control frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()