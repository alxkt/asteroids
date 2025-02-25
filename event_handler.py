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
            pygame.quite()
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


