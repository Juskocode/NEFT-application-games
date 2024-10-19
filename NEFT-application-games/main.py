import pygame
from sys import exit
import config

pygame.init()
clock = pygame.time.Clock()

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    while True:
        quit_game()
        
        config.window.fill((0, 0, 0))
        
        clock.tick(60)
        pygame.display.flip()
main()