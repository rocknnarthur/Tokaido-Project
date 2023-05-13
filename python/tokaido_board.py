import pygame, sys
import station_effect as se
from classes import Player, Crosshair

#init
pygame.init()
pygame.display.set_caption("Plateau Tokaido")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((1080,720))

# crosshair
crosshair = Crosshair("python/images/sakura_flower.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

def rotation_image(image,angle):
    """il s'agit d'une fonction qui permet de faire une rotation d'image dans le cas
    où elle serait à l'envers par exemple"""
    location = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image,angle)
    rot_sprite.get_rect().center = location
    return rot_sprite

#board's backgrounds
background = pygame.image.load("python/images/00.png")
background = pygame.transform.scale(background,(720,1080))
background2 = pygame.image.load("python/images/01.png")
background2 = pygame.transform.scale(background2,(720,1080))
background3 = pygame.image.load("python/images/02.png")
background3 = pygame.transform.scale(background3,(720,1080))

background = rotation_image(background,90)
background2 = rotation_image(background2,90)
background3 = rotation_image(background3,90)

position = 0
position2 = 0

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    screen.blit(background,(position,0))
    screen.blit(background2,(background.get_width() + position,0))
    screen.blit(background3,(background.get_width() + background2.get_width() + position2,0))

    crosshair_group.draw(screen)
    crosshair_group.update()
    pygame.display.update()