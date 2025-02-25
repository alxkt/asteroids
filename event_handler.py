import pygame
import sys

def handle_events(player, dt):
    """
    Hander user input events.
    Args:
        player (Player): The player object to control.
        dt (float): Delta time for frame rate independance.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.rotate(-dt)
    if keys[pygame.K_d]:
        player.rotate(dt)
    if keys[pygame.K_w]:
        player.move(dt)
    if keys[pygame.K_s]:
        player.move(-dt)
    if keys[pygame.K_SPACE]:
        player.shoot()

def handle_menu_events():
    """
    Handle input events for the menu.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "start"
            if event.key == pygame.K_ESCAPE:
                pygame.quite()
                sys.exit()
    return None