import pygame
import circleshape
import constants
import random
from logger import log_event


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            
            #Rotate new asteroid
            ast1_vel = self.velocity.rotate(angle)
            ast2_vel = self.velocity.rotate(-1*angle)
            
            #Size of new asteroid
            ast = self.radius - constants.ASTEROID_MIN_RADIUS

            ast1 = Asteroid(self.position[0],self.position[1],ast)
            ast2 = Asteroid(self.position[0],self.position[1],ast)

            ast1.velocity = ast1_vel * 1.2
            ast2.velocity = ast2_vel


        