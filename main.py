import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

#gameloop
running = True
while running:
    #Keep loop running at the right speed
    clock.tick(FPS)
    #Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Update
    all_sprites.update()
    #Draw/Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
