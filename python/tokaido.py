import random
from player import Player
from station_effect import checkstation
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

# Player class instance
lplayer = []
for p in range(1, player_n+1):                                      ## instancier les classes joueurs avec leur couleur avant de commencer la partie
    ask_pseudo = input(f"Pseudo du joueur {lplayer_color[p-1]}: ")
    pl = Player(ask_pseudo, lplayer_color[p-1], 1, 7)
    lplayer.append(pl)

for p in lplayer:
    p.afficher()

# Player shuffle for starting
random.shuffle(lplayer)

# Some setups 
relais = [1,15,28,42,55]
a = 1
mealdraw = []
souvdraw = []
riz_complete = 0
mont_complete = 0
mer_complete = 0

# Game round with fixing first player
current_p = lplayer[0]

Tour = True
while Tour:

    print(f'Le joueur {current_p.color} joue')

    move = 0
    while move <= current_p.locate or move > relais[a]:
        move = int(input("Quelle station? : "))

        # Read CSV for board stations
        with open('python/board.csv') as board:                      #  permet de lire le csv contenant les cases du plateau
            reader = csv.reader(board, delimiter = ';')
            line_count = move
            for row in reader:
                if str(line_count) == row[0]:
                    case = row[1]
            
        # Check if move is legally possible and legal -> apply effect, else loop again
        if move > current_p.locate and move <= relais[a]:
            if not checkstation(current_p, case):
                move = 0
        else:
            print('Pas de retour en arrière ni de dépassement de relais !')
        
    # Move player
    current_p.locate = move
    print(f"Le joueur {current_p.color} est sur une case {case} situé à {move}.")

    # Check who's playing next (= farthest player)
    small_locate = 100
    for p in lplayer:
        if p.locate < small_locate:
            small_locate = p.locate
            current_p = p

    # Checking if all players are arrived at next relais
    nbrelais = 0
    for p in lplayer:
        if p.locate == relais[a]:
            nbrelais += 1
    
    if nbrelais == player_n:
        a += 1
        print(f"Vous passez maintenant à la {a+1}e partie du plateau.")
        mealdraw = []
        nbrelais = 0


print("stopping script")