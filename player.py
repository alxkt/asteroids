import pygame
from circleshape import CircleShape
from shot import Shot
from constants import (
    PLAYER_RADIUS,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN
)

class Player(CircleShape):
    def __init__(self, x, y):
        """
        Initialize the Player object.

        Args:
            x (float): The x-coordinate of the player's initial position.
            y (float): The y-coordinate of the player's initial position.
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    def triangle(self):
        """
        Calculate the vertices of the player's triangular shape.

        Returns:
            list: A list of three vectors representing the vertices of the triangle.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def move(self, dt):
        """
        Move the player forward or backward.

        Args:
            dt (float): Delta time for frame rate independence.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt):
        """
        Rotate the player.

        Args:
            dt (float): Delta time for frame rate independence.
        """
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        """
        Update the player's state.

        Args:
            dt (float): Delta time for frame rate independence.
        """
        self.shot_timer -= dt

    def draw(self, screen):
        """
        Draw the player on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the player on.
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def shoot(self):
        """
        Shoot a shot if the cooldown period has passed.
        """
        if self.shot_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOOT_COOLDOWN