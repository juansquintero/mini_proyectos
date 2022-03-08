import pygame
import random
 
# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25
 
#Variables por si las moscas 
x = 0
y = 0 
change_x = 0
change_y = 0


def make_ball():
    """
    Nueva Bola.
    """
    
    ball2 = {'x': 0, 'y': 0,'change_x': 0,'change_y': 0}
   
    ball2["x"] = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball2["y"] = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
 
    ball2["change_x"] = random.randrange(-2, 3)
    ball2["change_y"] = random.randrange(-2, 3)
 
    return ball2
 
 
def main():

    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Mis bolas")
 
    done = False
 
    clock = pygame.time.Clock()
 
    ball_list = []
 
    ball = make_ball()
    ball_list.append(ball)
 
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)
 
        for ball2 in ball_list:
            ball2["x"] += ball2["change_x"]
            ball2["y"] += ball2["change_y"]
 
            if ball2["y"] > SCREEN_HEIGHT - BALL_SIZE or ball2["y"] < BALL_SIZE:
                ball2["change_y"] *= -1
            if ball2["x"] > SCREEN_WIDTH - BALL_SIZE or ball2["x"] < BALL_SIZE:
                ball2["change_x"] *= -1
 
        screen.fill(BLACK)
 
        for ball2 in ball_list:
            pygame.draw.circle(screen, WHITE, [ball2["x"], ball2["y"]], BALL_SIZE)

        clock.tick(60)

        pygame.display.flip()
 
    pygame.quit()
 
if __name__ == "__main__":
    main()