import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    #To draw the player, override the draw method of CircleShape. It should take the screen object as a parameter, and call pygame.draw.polygon. It takes:
    #The screen object
    #A color (use "white")
    #A list of points (use self.triangle() that we provided for you)
    #A line width (use 2)
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)




