
import pygame, math, random

pygame.init()

pygame.display.set_caption('Galaga pobre')
clock = pygame.time.Clock()
screen_width = 850
screen_height = 600
surface = pygame.display.set_mode((screen_width,screen_height))
fondo = 0,0,0
disparo = 255,124,221
nave = 51,255,255
enemigo = 255,102,102


class Square:
    def __init__(self, color, x, y, width, height):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.direction = 'E'
        self.speed = 5

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

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Dibujado de nave principal
sq = Square(nave,200,200,100,100)

bullets = []
enemies = []

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key) #Ver si la tecla fue presionada
            if event.key==119: #W
                sq.direction = 'N'
            if event.key==97: #A
                sq.direction = 'W'
            if event.key==115: #S
                sq.direction = 'S'
            if event.key==100: #D
                sq.direction = 'E'
            if event.key==32: #Espacio
                #Disparo
                spawnx = sq.rect.x + sq.rect.width/2 - 10
                b = Square(disparo, spawnx,sq.rect.y, 20,20)
                b.direction = 'N'
                b.speed = 10
                bullets.append(b)
    
    #Mover los objetos
    for b in bullets:
        b.move()
    for e in enemies:
        e.move()
    sq.move() 
    
    #Spawn enemeigos
    if random.randint(1,30) == 15: #15 doesn't matter
        x = random.randint(0,screen_width-40)
        e = Square(enemigo, x,-40, 40,40)
        e.direction = 'S'
        enemies.append(e)
    
    # Colision de balas y enemigos ; Colision nave y enemigos mientras dispara
    for i in reversed(range(len(bullets))):
        for j in reversed(range(len(enemies))):
            if bullets[i].collided(enemies[j].rect):
                del enemies[j]
                del bullets[i]
                break
            elif sq.collided(enemies[j].rect):
                pygame.quit()

    
    surface.fill(fondo) 
    for b in bullets:
        b.draw(surface)
    for e in enemies:
        e.draw(surface)
    sq.draw(surface)
    pygame.display.flip()
    clock.tick(30) #30 FPS
pygame.quit()
exit()