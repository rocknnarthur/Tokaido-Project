import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Tokaido")
clock = pygame.time.Clock()

test_surface = pygame.image.load("python/images/tokaido-cover.png").convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    screen.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(60)