import pygame

class Player:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.speed = 5
        self.stamina = 100
        self.radius = 25  # caricatura cabeza grande
        self.color = (0, 200, 255)

    def handle_keys(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.stamina -= 0.1
        if keys[pygame.K_s]:
            self.y += self.speed
            self.stamina -= 0.1
        if keys[pygame.K_a]:
            self.x -= self.speed
            self.stamina -= 0.1
        if keys[pygame.K_d]:
            self.x += self.speed
            self.stamina -= 0.1

    def update(self):
        self.stamina = max(0, min(100, self.stamina))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        font = pygame.font.SysFont("Arial", 20)
        name_surf = font.render(self.name, True, (255,255,255))
        screen.blit(name_surf, (self.x - name_surf.get_width()//2, self.y + self.radius))
