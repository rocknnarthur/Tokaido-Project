
import random
from player import Player
import csv

# Starting game menu
while True:
    print("""==========TOKAIDO==========

Bienvenue à toi voyageur !

Choisis un mode de jeu: [1/2/3/4]
1) Voyage Initiatique ✓
2) Trajet Retour X
3) Gastronomie X
4) Préparatifs X
    """)
    # Gamemode choice
    gamemode = int(input("Mode de jeu: "))

    if gamemode == 1:
        pass

    elif gamemode == 2:
        pass

    elif gamemode == 3:
        pass

    elif gamemode == 4:
        pass
    
    break

# Player number
player_n = 0
while not 1 < player_n < 6:
    player_n = int(input("Nombre de joueurs: "))
    if not 1 < player_n < 6:
        print("Le nombre de joueurs doit être entre 2 et 5.")

# Player color
l_color = ['purple', 'yellow', 'green', 'gray', 'blue']
lplayer_color = []
print(l_color)
for player in range(1, player_n+1):
    loop = True
    while loop:
        ask_color = input(f"Couleur joueur {player}: ")
        for color in l_color:
            if ask_color == color:
                l_color.remove(f'{color}')
                lplayer_color.append(f'{color}')
                loop = False

lplayer = []
for p in range(1, player_n+1):                                      ## instancier les classes joueurs avec leur couleur avant de commencer la partie
    ask_pseudo = input(f"Pseudo du joueur {lplayer_color[p-1]}: ")
    pl = Player(ask_pseudo, lplayer_color[p-1], 0, 7, 0)
    lplayer.append(pl)

for p in lplayer:
    p.afficher()

random.shuffle(lplayer)


relais = [1,15,28,42,55]
a = 1


Tour = True
while Tour:

    current_p = lplayer[0]
    print(f'Le joueur {current_p.color} joue')

    move = -1
    while move <= current_p.locate or move > relais[a]:
        print('Pas de retour en arrière ni de dépassement de relais !')
        move = int(input("Quelle station? : "))

    with open('board.csv') as board:                      #  permet de lire le csv contenant les cases du plateau
        reader = csv.reader(board, delimiter = ';')
        line_count = move
        for row in reader:
            if str(line_count) == row[0]:
                case = row[1]

    current_p.locate = move
    print(f"Le joueur {current_p.color} est sur une case {case} situé à {move}.")

    for p in lplayer:
        small = 100
        if p.locate < small:
            small = p.locate
            current_p = p

    

    


print("stopping script")