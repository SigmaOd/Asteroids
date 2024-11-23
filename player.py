#
#
#
import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS,PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN, SCREEN_HEIGHT, SCREEN_WIDTH
from shot import Shot

class Player(CircleShape):
    # containers = ()


    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.health = 3
        self.color = "white"
        self.respawn_chances = 3
    
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), 2)
        
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_MOVE_SPEED * dt

    def shoot(self):
        if self.shot_timer > 0:
            return
        self.shot_timer = PLAYER_SHOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED

    def get_damaged(self):
        self.health -= 1
        if self.health == 2:
            self.color = "orange"
        if self.health == 1:
            self.color = "red"
        

 def collision_check(self, circle):
        while self.position.distance_to(circle.position) >= self.radius + circle.radius:
             if self.position.distance_to(circle.position) == self.radius + circle.radius:
                  return True
        return False
            
    def respawn(self):
            self.respawn_chances -= 1
            self.health == 3
            
        
    # def move_down(self,dt):
    #     self.position += pygame.Vector2(0,-dt)
