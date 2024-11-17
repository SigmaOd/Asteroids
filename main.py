# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
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
    game_clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0                              # delta-t


    while True:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  return
                
                
      screen.fill((0,0,0))
      player.draw(screen)
      pygame.display.flip()
      
      # limit Framerate to 60 fps 
      dt = game_clock.tick(60) / 1000
          



    
    # print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
        main()