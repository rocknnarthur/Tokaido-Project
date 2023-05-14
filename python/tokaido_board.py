import pygame, sys
import station_effect as se
import random
import csv
import pickle
from classes import Player, Case, Crosshair
from fichier import Fichier

# Init
pygame.init()
pygame.display.set_caption("Plateau Tokaido")
pygame.display.set_icon(pygame.image.load("python/images/sakura.png"))
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((1080,720))

# Crosshair
crosshair = Crosshair("python/images/sakura_flower.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#rotation image
def rotation_image(image,angle):
    """il s'agit d'une fonction qui permet de faire une rotation d'image dans le cas
    où elle serait à l'envers par exemple"""
    location = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image,angle)
    rot_sprite.get_rect().center = location
    return rot_sprite

#defilement plateau
position = 0
position2 = 0
position_state = False
def scroll_image(bg,bg2,bg3):
    """fonction qui fait défiler les images"""
    global position
    global position2
    global position_state
    screen.fill((0,0,0))
    screen.blit(bg,(position,0))
    screen.blit(bg2,(bg.get_width()+ position,0))
    screen.blit(bg3,(bg.get_width() + bg2.get_width()+ position2,0))
    if position_state == True:
         position -= 5
         position2 -= 5
         #Sassayako.rect.x -= 5
         #Yoshiyasu.rect.x -= 5
    elif position_state == False:
         position -=0
         position2 -=0

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

# Couleurs Voyageurs
purple_rgb = (203,49,222)
blue_rgb = (0,127,255)
green_rgb = (22,184,78)
gray_rgb = (160,160,160)
yellow_rgb = (240,195,0)

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

fichier_stations = open("python/Stations.py","rb")
Station_dico = pickle.load(fichier_stations)
fichier_stations.close()

liste_case = []
for k in range(55):
     case_posx = Station_dico[str(k)][-2]
     case_posy = Station_dico[str(k)][-1]
     case = Case((case_posx,case_posy),k)
     liste_case.append(case)

pos_list = [-900, -895]
pos_listInter = [-1580, -1580]
pos_list2 = [-2140, -2140]

if player_n >= 4:
    ldb_case = [2, 6, 7, 8, 10, 12, 18, 19, 20, 21, 23, 25, 31, 33, 35, 37, 38, 41, 44, 46, 48, 49, 52, 53]
else:
    ldb_case = []

relais = [1,15,28,42,55]
if gamemode == 2:
    a = 3
else:
    a = 1

compteur_case = a

# pour les ecarts de case sur le 1er relais
gap = f"0.{player_n-1}"
gap = float(gap)
for p in lplayer:
    print(p.locate)
    p.locate -= gap
    gap -= 0.1

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

    #BLIT BOARD
    scroll_image(background, background2, background3)

    if compteur_case == 1:
          range_compteur = (15,0)
          """selon la partie du plateau où on se trouve, j'organise la position des cases cliquables (invisibles)"""
          for i in range(range_compteur[0]):
               screen.blit(liste_case[i].surface,liste_case[i].rect)
     
    if compteur_case == 2:
          range_compteur = (15,28)
          for i in range (range_compteur[0],range_compteur[1]):
               screen.blit(liste_case[i].surface,liste_case[i].rect) 
     
    if compteur_case == 3:
          range_compteur = (28,42)
          for i in range(range_compteur[0],range_compteur[1]):
               screen.blit(liste_case[i].surface,liste_case[i].rect)
     
    if compteur_case == 4:
          range_compteur = (42,55)
          for i in range(range_compteur[0],range_compteur[1]):
               screen.blit(liste_case[i].surface,liste_case[i].rect)                             

     #c'est comme ça que le défilement s'arrête automatiquement aux position que je souhaite
    if position == pos_list[0]:
        position_state = False
        compteur_case = 2
               
    if position2 == pos_listInter[1]:
        position_state = False
        compteur_case = 3

    if position2 == pos_list2[1]:
        position_state = False
        compteur_case = 4

    #BLIT HUD
    se.hud_set(green_rgb, purple_rgb, yellow_rgb, blue_rgb, gray_rgb, current_p, screen)

    #BLIT PIONS
    for p in lplayer:
        with open('python/board.csv') as board:
            reader = csv.reader(board, delimiter = ';')
            line_count = p.locate
            for row in reader:
                if str(line_count) == row[0]:
                    p.x = int(row[2])
                    p.y = int(row[3])

        screen.blit(pygame.image.load(f"python/images/player_{p.color}.png"), (p.x, p.y))
        

    

    """
    COMPLETE WITH THE CODE FROM tokaido.py
    """

    # PYGAME EVENTS DETECTION
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if compteur_case == 1:
                for m in range(range_compteur[0]):
                    case = liste_case[m]
                    if case.rect.collidepoint(mouse_pos):
                       #MOVE STATION
                       move = int(case.nom)+1
                       se.move_set(move, current_p, relais, a, lplayer, player_n, ldb_case, l_meet, l_souvenir, l_meal, gamemode)

    pygame.time.Clock().tick(120)

    crosshair_group.draw(screen)
    crosshair_group.update()
    pygame.display.update()