import pygame

from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shoots import Zap

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    zaps = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Zap.containers = (zaps, updatable, drawable)

    character = Player((SCREEN_WIDTH / 2) , (SCREEN_HEIGHT / 2))
    spawning_asteroids = AsteroidField()
    
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in asteroids:
            if character.check_collision(asteroid):
                print("Game Over!")
                return
            for zap in zaps:
                if zap.check_collision(asteroid):
                    zap.kill()
                    asteroid.split()
        

        screen.fill("black")

        for draws in drawable:
            draws.draw(screen)

        pygame.display.flip()
        
        dt = fps.tick(60) / 1_000

if __name__ == "__main__":
    main()