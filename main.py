import sys
import pygame
import constants
import player 
import asteroid
import asteroidfield
import shot
from logger import log_state
from logger import log_event


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver} ")
    print(f"Screen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}")
    
    #initialize game
    pygame.init()

    #Creating Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable,drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots,updatable,drawable)


    clocks = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT))
    charater = player.Player(x = constants.SCREEN_WIDTH/2, y= constants.SCREEN_HEIGHT/2)
    field = asteroidfield.AsteroidField()



    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill(color="black")

        #Character actions
        for X in updatable:
            X.update(dt)
            if X == charater:
                charater.cool_down -= dt 
        for X in drawable:
            X.draw(screen)
        
        for X in asteroids:
            if charater.collides_with(X) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for Y in shots:
                if Y.collides_with(X) == True:
                    log_event("asteroid_shot")
                    X.split()
                    Y.kill()
        pygame.display.flip()


        dt = clocks.tick(60)/1000
        


if __name__ == "__main__":
    main()
