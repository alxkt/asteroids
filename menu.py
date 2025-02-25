import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from event_handler import handle_menu_events

def main_menu():
    """
    Display the main menu and handle user input to start the game or quit.
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

        action = handle_menu_events()
        if action == "start":
            return  # Start the game

        clock.tick(60)