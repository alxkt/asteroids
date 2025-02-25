import pygame
from constants import *

class CircleShape(pygame.sprite.Sprite):
    """
    Base class for circular game objects.
    """
    def __init__(self, x, y, radius):
        """
        Initialize the CircleShape object.

        Args:
            x (float): The x-coordinate of the object's initial position.
            y (float): The y-coordinate of the object's initial position.
            radius (float): The radius of the object.
        """
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, other):
        """
        Check if this object collides with another circular object.

        Args:
            other (CircleShape): The other circular object to check collision with.

        Returns:
            bool: True if the objects collide, False otherwise.
        """
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius

    def draw(self, screen):
        """
        Draw the object on the screen.

        Args:
            screen (pygame.Surface): The surface to draw the object on.
        """
        pass

    def update(self, dt):
        """
        Update the object's state.

        Args:
            dt (float): Delta time for frame rate independence.
        """
        pass