import random
import pygame
import config

class Player:
    def __init__(self):
        # Bird Object
        self.x, self.y = 50, 200
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.Color = random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
        self.vel = 0
        self.flap = False
        self.alive = True

        # Network atributtes
        self.decision = None

    
    def draw(self, window):
        pygame.draw.rect(window, self.Color, self.rect)

    def ground_collision(self, ground):
        return pygame.Rect.colliderect(self.rect, ground)
    
    def sky_collision(self):
        return bool(self.rect.y < 30)
    
    def pipe_collision(self):
        for p in config.pipes:
            return pygame.Rect.colliderect(self.rect, p.top_rect) or \
                   pygame.Rect.colliderect(self.rect, p.bot_rect)
    
    def update(self, ground):
        if not (self.ground_collision(ground) or self.pipe_collision()):
            # Gravity
            self.vel += 0.25
            self.rect.y += self.vel
            if self.vel > 5:
                self.vel = 5
        else:
            self.alive = False
            self.flap = False
            self.vel = 0
    
    def bird_flap(self):
        if not self.flap and not self.sky_collision():
            self.flap = True
            self.vel = -5
        if self.vel >= -3:
            self.flap = False
    
    # Network functions
    def think(self):
        self.decision = random.uniform(0, 1)
        if self.decision > 0.78: # 0.73 ratio to flap
            self.bird_flap()