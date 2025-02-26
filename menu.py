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
    
    Returns:
        str: "resume" if the game should continue, "quit" if the game should exit.
    """
    font = pygame.font.Font(None, 74)
    clock = pygame.time.Clock()
    
    # Clear any pending events that might have accumulated
    pygame.event.clear()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Ensure we clear events before returning
                    pygame.event.clear()
                    return "resume"
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
        # Draw pause screen
        screen.fill("black")
        pause_text = font.render("PAUSED", True, "white")
        resume_text = font.render("Press ESC to Resume", True, "white")
        quit_text = font.render("Press Q to Quit", True, "white")

        screen.blit(pause_text, (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT // 4))
        screen.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
        
        pygame.display.flip()
        clock.tick(60)

def game_over_screen(screen, score):
    """
    Display the game over screen with final score and options to restart or quit.
    
    Args:
        screen (pygame.Surface): The game screen surface to draw on
        score (int): The player's final score
        
    Returns:
        str: "restart" if the player wants to play again
    """
    font = pygame.font.Font(None, 74)
    score_font = pygame.font.Font(None, 48)
    clock = pygame.time.Clock()
    
    # Clear any pending events that might have accumulated
    pygame.event.clear()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Ensure we clear events before returning
                    pygame.event.clear()
                    return "restart"
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        # Draw game over screen
        screen.fill("black")
        game_over_text = font.render("GAME OVER", True, "white")
        score_text = score_font.render(f"Final Score: {int(score)}", True, "white")
        restart_text = font.render("Press ENTER to Restart", True, "white")
        quit_text = font.render("Press ESC to Quit", True, "white")

        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 4 - 50))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 4 + 30))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 150))
        
        pygame.display.flip()
        clock.tick(60)