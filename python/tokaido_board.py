import pygame, sys
import station_effect as se
import random
from classes import Player, Crosshair
from fichier import Fichier

# Init
pygame.init()
pygame.display.set_caption("Plateau Tokaido")
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((1080,720))

# Crosshair
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

# Board's backgrounds
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

# Get infos from pregame settings
lp_infos = Fichier("lplayer.dat").lire() # PSEUDO, COLOR, GENDER
gamemode = Fichier("gamemode.dat").lire() #MODE
player_n = len(lp_infos)

# Player class instance
if gamemode == 2:
    fstation = 55
else:
    fstation = 1

if gamemode == 0:
    startmoney = 7
    tuile = None
else:
    l_tuile = [("Kinko", 7), ("Hirotada", 8), ("Yoshiyasu", 9), ("Zen-emon", 6), ("Mitsukuni", 6), ("Sasayakko", 5), ("Umegae", 5), ("Chuubei", 4), ("Satsuki", 2), ("Hiroshige", 3)]
    random.shuffle(l_tuile)

lplayer = []
for p in lp_infos:
    if gamemode != 0: # CHOIX DES TUILES VOYAGEURS
        tuiledraw = []
        tuiledraw.append(l_tuile[0])
        tuiledraw.append(l_tuile[1])
        del(l_tuile[0:2])
        print(tuiledraw)
        tuile_ask = 0
        while not 0 < tuile_ask < 3:
            tuile_ask = int(input("Quelle tuile voulez-vous choisir ? [entrez position numérique de la tuile] : "))
            if not 0 < tuile_ask < 3:
                print("Entrez une valeur correcte.")
        startmoney = tuiledraw[tuile_ask-1][1]
        tuile = tuiledraw[tuile_ask-1][0]
        print(tuiledraw[tuile_ask-1])

    pl = Player(p[0], p[1], fstation, startmoney, tuile, p[2])
    lplayer.append(pl)

print(lplayer)

# Player shuffle for starting
random.shuffle(lplayer)

for p in lplayer:
    p.afficher()

# Some setups 
if player_n >= 4:
    ldb_case = [2, 6, 7, 8, 10, 12, 18, 19, 20, 21, 23, 25, 31, 33, 35, 37, 38, 41, 44, 46, 48, 49, 52, 53]

relais = [1,15,28,42,55]
if gamemode == 2:
    a = 3
else:
    a = 1

l_meal = ["Misoshiru", "Misoshiru", "Misoshiru", "Nigirimeshi", "Nigirimeshi", "Nigirimeshi", "Dango", "Dango", "Dango", "Yakitori", "Yakitori", "Soba", "Soba", "Sushi", "Sushi", "Tofu", "Tofu", "Tempura", "Tempura", "Unagi", "Donburi", "Udon", "Fugu", "Tai Meshi", "Sashimi"]
random.shuffle(l_meal)
l_souvenir = ["Koma", "Gofu", "Washi", "Hashi", "Uchiwa", "Yunomi", "Ocha", "Sake", "Konpeito", "Kanaboko", "Daifuku", "Manju", "Netsuke", "Shamisen", "Jubako", "Sumie", "Shikki", "Ukiyoe", "Kanzashi", "Sandogasa", "Geta", "Haori", "Yukata", "Furoshiki"]
random.shuffle(l_souvenir)
l_meet = ["miko", "miko", "annaibito_mer", "annaibito_mer", "annaibito_mer", "annaibito_mont", "annaibito_mont", "annaibito_riz", "kuge", "kuge", "shokunin", "shokunin", "samurai", "samurai"]
random.shuffle(l_meet)


# Fixing first player turn
current_p = lplayer[0]

#MAIN LOOP
while True:

    """
    COMPLETE WITH THE CODE FROM tokaido.py
    """

    # PYGAME EVENTS DETECTION
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