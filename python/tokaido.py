import random
import csv
from player import Player
import station_effect as se

# Starting game menu
print("""==========TOKAIDO==========

Bienvenue à toi voyageur !

Choisis un mode de jeu: [1/2/3/4]
1) Voyage Initiatique ✓
2) Trajet Retour X
3) Gastronomie X
4) Préparatifs X
    """)

# Gamemode choice
while True:    
    gamemode = int(input("Mode de jeu: "))

    if gamemode == 1:
        travel_init = True
        print("Mode: Voyage Initiatique")
        break

    elif gamemode == 2:
        print("Trajet Retour. Pas développé.")

    elif gamemode == 3:
        print("Gastronomie. Pas développé.")

    elif gamemode == 4:
        print("Préparatifs. Pas développé.")
    
    else:
        print("Entrez une valeur correcte.")

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


# Voyage Initiatique gamemode
while travel_init:

    print(f'Le joueur {current_p.color} joue')

    move = 0
    while move <= current_p.locate or move > relais[a]:
        move = int(input("Quelle station? : "))

        # Read CSV for board stations
        with open('python/board.csv') as board:
            reader = csv.reader(board, delimiter = ';')
            line_count = move
            for row in reader:
                if str(line_count) == row[0]:
                    case = row[1]
            
        # Check if move is legally possible and legal = apply effect, else loop again
        if move > current_p.locate and move <= relais[a]:
            for p in lplayer:
                if move == p.locate and move != relais[a]:
                    print(f"vous ne pouvez pas aller sur cette case, elle est occupée par le joueur {p.color} !")
                    move = 0
            if move != 0:
                if not se.checkstation(current_p, case, l_meet, l_souvenir, l_meal, player_n):
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
        # Check if the game is finished
        if a == 5:
            break
        print(f"Vous passez maintenant à la {a}e partie du plateau.")
        l_meal.extend(se.mealdraw)
        print(l_meal)
        se.mealdraw = []
        print(se.mealdraw)
        nbrelais = 0

# Add Souvenir points to each player
for p in lplayer:
    se.souvenircheck(p)

# Add Temple bonus points
l_amen = se.templebonus(lplayer)
temple_b = 10
amen_detector = 50
for p in se.l_amen:
    p.pts += temple_b
    if p.amen != amen_detector:
        if temple_b == 10 or 7:
            temple_b -= 3
        elif temple_b == 4:
            temple_b -= 2
    #FAUT TROUVER UN MOYEN DE DETECTER LES EGALITES D'OFFRANDE

# Add Success points

# Results and show the winner
winner = None
lp_result = []
for np in range(len(lplayer)):
    bigger_pts = -1
    for p in lplayer:
        if p.pts > bigger_pts:
            bigger_pts = p.pts
            winner = p
    lp_result.append(winner)
    lplayer.remove(winner)
    

print(f"""
Félicitations !
Le joueur {lp_result[0].color} {lp_result[0].pseudo} remporte cette partie avec {lp_result[0].pts}pts !
""")

print("Classement des perdans:")
for other in range(1, len(lp_result)):
    print(f"En {other+1}e, le joueur {lp_result[other].color} {lp_result[other].pseudo} avec {lp_result[other].pts}pts")

print("\nstopping script")