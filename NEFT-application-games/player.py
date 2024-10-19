import random
import pygame

class Player:
    def __init__(self):
        self.x, self.y = 50, 200
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.Color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
    
    def draw(self, window):
        pygame.draw.rect(window, self.Color, self.rect)