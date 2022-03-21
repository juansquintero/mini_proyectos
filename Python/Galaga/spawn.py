import pygame 

class Spawn():

    def __init__(self, color, x, y, width, height):
        
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.direction = 'E'
        self.speed = 5

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)