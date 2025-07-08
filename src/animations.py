import pygame

class Animation:
    def __init__(self):
        self.goal = False
        self.counter = 0

    def start_goal_animation(self):
        self.goal = True
        self.counter = 0

    def update(self, screen):
        if self.goal:
            font = pygame.font.SysFont("Arial", 72, True)
            text = font.render("GOOOL!!!", True, (255, 255, 0))
            screen.blit(text, (screen.get_width()//2 - text.get_width()//2, 250))
            self.counter += 1
            if self.counter > 120:  # 2 segundos a 60fps
                self.goal = False
