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

player_n = 0
while not 1 < player_n < 6:
    player_n = int(input("Nombre de joueurs: "))
    if not 1 < player_n < 6:
        print("Le nombre de joueurs doit être entre 2 et 5.")
    
    

print("stopping script")

