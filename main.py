# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
# from constants import (
#       SCREEN_WIDTH, 
#       SCREEN_HEIGHT, 
#       ASTEROID_MIN_RADIUS, 
#       ASTEROID_KINDS, 
#       ASTEROID_SPAWN_RATE, 
#       ASTEROID_MAX_RADIUS
#       ) 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
          for event in pygame.event.get():
                if event.type == pygame.QUIT:
                      return
          screen.fill((0,0,0))
          pygame.display.flip()



    
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
        main()