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

for player in range(1, player_n+1):
    pass        ## instancier les classes joueurs avec leur couleur avant de commencer la partie






print("stopping script")