import random
from circleshape import *

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    random_rotation = random.uniform(20, 50)
    random_angle1 = self.velocity.rotate(random_rotation)
    random_angle2 = self.velocity.rotate(-random_rotation)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    split_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
    split_asteroid1.velocity = random_angle1 * 1.2

    split_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
    split_asteroid2.velocity = random_angle2 * 1.2
  
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  def update(self, dt):
    self.position += self.velocity * dt