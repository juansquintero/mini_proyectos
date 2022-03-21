import pygame

class Movement():
    
    def __init__():

        pass

    def move(self):
        
        if self.direction == 'E':
            self.rect.x = self.rect.x+self.speed
        if self.direction == 'W':
            self.rect.x = self.rect.x-self.speed
        if self.direction == 'N':
            self.rect.y = self.rect.y-self.speed
        if self.direction == 'S':
            self.rect.y = self.rect.y+self.speed

    def collided(self, other_rect):
        return self.rect.colliderect(other_rect)
