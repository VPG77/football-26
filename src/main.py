import pygame
from game import Game

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Football 25")

font_title = pygame.font.SysFont("Arial", 72, bold=True)
font_menu = pygame.font.SysFont("Arial", 36)

ligas = ["Cyber League", "Neo Premier", "Quantum Serie", "Hyper Liga", "Galactic Cup"]

def draw_portada():
    screen.fill((0,0,0))
    title_text = font_title.render("FOOTBALL 25", True, (0, 255, 255))
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 100))
    y_offset = 250
    for liga in ligas:
        liga_text = font_menu.render(liga, True, (255,255,255))
        screen.blit(liga_text, (WIDTH//2 - liga_text.get_width()//2, y_offset))
        y_offset += 50
    instructions = font_menu.render("Presiona ENTER para continuar", True, (50, 100, 200))
    screen.blit(instructions, (WIDTH//2 - instructions.get_width()//2, HEIGHT - 100))

def main():
    clock = pygame.time.Clock()
    running = True
    in_menu = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and in_menu:
                if event.key == pygame.K_RETURN:
                    in_menu = False
                    game = Game(screen)
                    game.run()

        if in_menu:
            draw_portada()
            pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
