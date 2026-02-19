import circleshape
import constants
import pygame
import shot


class Player(circleshape.CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.rotation = 0
        self.x = x
        self.y = y
        self.cool_down = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,'white',self.triangle(),constants.LINE_WIDTH)
        pass

    def rotate(self,dt):
        self.rotation += constants.PLAYER_TURN_SPEED*dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1*dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1*dt)
        if keys[pygame.K_SPACE]:
            
            self.shoot()

    
    def move(self, dt):
        unit_vector = pygame.Vector2(0,1)
        rotate_vector = unit_vector.rotate(self.rotation)
        rotate_vector_speed = rotate_vector*constants.PLAYER_SPEED*dt
        self.position += rotate_vector_speed

    def shoot(self):
        if self.cool_down > 0:
            pass
        else:
            fire = shot.Shot(self.position[0],self.position[1],constants.SHOT_RADIUS)
            fire.velocity = pygame.Vector2(0,1).rotate(self.rotation)*constants.PLAYER_SHOT_SPEED
            self.cool_down = constants.PLAYER_SHOOT_COOLDOWN_SECONDS