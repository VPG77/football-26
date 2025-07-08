import pygame
import random

class AI:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.speed = 4
        self.radius = 25
        self.color = (255, 100, 100)

    def update(self):
        self.x += random.choice([-1,0,1]) * self.speed * 0.1
        self.y += random.choice([-1,0,1]) * self.speed * 0.1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        font = pygame.font.SysFont("Arial", 20)
        name_surf = font.render(self.name, True, (255,255,255))
        screen.blit(name_surf, (self.x - name_surf.get_width()//2, self.y + self.radius))
