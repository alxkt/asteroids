import pygame
import sys

def handle_events(player, dt):
    """
    Handle user input events.

    Args:
        player (Player): The player object to control.
        dt (float): Delta time for frame rate independence.

    Returns:
        str or None: Action state like "pause", "quit", or None if no state change.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "quit"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "pause"
            elif event.key == pygame.K_SPACE:
                player.shoot()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.rotate(-dt)
    if keys[pygame.K_d]:
        player.rotate(dt)
    if keys[pygame.K_w]:
        player.move(dt)
    if keys[pygame.K_s]:
        player.move(-dt)

    return None

def handle_menu_events():
    """
    Handle user input events for the menu.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "resume"
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    return None