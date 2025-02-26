import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main_menu():
    """
    Display the main menu and handle user input to start the game.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids - Main Menu")
    font = pygame.font.Font(None, 74)
    clock = pygame.time.Clock()

    while True:
        screen.fill("black")
        title_text = font.render("Asteroids", True, "white")
        start_text = font.render("Press ENTER to Start", True, "white")
        quit_text = font.render("Press ESC to Quit", True, "white")

        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Start the game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        clock.tick(60)

def pause_screen(screen):
    """
    Display the pause screen and handle user input to resume or quit the game.
    """
    font = pygame.font.Font(None, 74)
    
    while True:
        screen.fill("black")
        pause_text = font.render("PAUSED", True, "white")
        resume_text = font.render("Press ENTER to Resume", True, "white")
        quit_text = font.render("Press ESC to Quit", True, "white")

        screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 4))
        screen.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Resume the game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()