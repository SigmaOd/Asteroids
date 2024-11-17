# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
# from asteroids import Asteroids
from asteroidfield import AsteroidField
from shot import Shot
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
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
#     asteroid = Asteroids(SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4, 3)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0                              # delta-t



    while True:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  return
                
                
      for obj in updatable:
           obj.update(dt)
      
      for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collision_check(shot):
                  shot.kill()
                  asteroid.split()
      screen.fill((0,0,0))
    
      for obj in drawable:
           obj.draw(screen)

      # player.update(dt)
      # player.draw(screen)
      pygame.display.flip()
      
      # limit Framerate to 60 fps 
      dt = game_clock.tick(60) / 1000
          



    
    # print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
     main()