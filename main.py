import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    character = Player((SCREEN_WIDTH / 2) , (SCREEN_HEIGHT / 2))
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        character.draw(screen)
        pygame.display.flip()
        
        dt = fps.tick(60) / 1_000

if __name__ == "__main__":
    main()