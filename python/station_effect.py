import random

def panoramacheck(player, case):
    pass

def checkstation(player, case):
    
    # Relais
    if case == "relais":
        pass # pioche n+1 cartes repas pour le 1er arrivé et achète ou non le repas, puis repose le paquet restant de côté pour les suivants
    
    # Echoppe
    if case == "echoppe":
        pass #pioche 3 random cartes souvenirs et décide d'en acheter 1, 2, 3 ou aucune
    
    # Temple
    if case == "temple":
        if player.purse > 0:
            depot = 0
            while not 0 < depot < 4 and player.purse >= depot:
                print("Vous devez déposer un nombre de pièces adéquat à votre bourse.")
                depot = int(input("Combien de pièces à déposer? [1, 2 ou 3]: "))
            
            player.purse -= depot
            player.amen += depot
            print(f"Vous avez déposé {depot} pièces au temple.")

        else:
            pass #impossible d'aller au temple

    # Rencontre
    if case == "rencontre":
        #pioche carte
        l_meet = ['miko', 'miko', 'annaibito_mer', 'annaibito_mer', 'annaibito_mer', 'annaibito_mont', 'annaibito_mont', 'annaibito_riz', 'kuge', 'kuge', 'shokunin', 'shokunin', 'samurai', 'samurai']
        random.shuffle(l_meet)
        meetcard = l_meet[0]

        if meetcard == "miko":
            player.amen += 1
            print("Carte Miko, une pièce de la banque est placé sur votre slot temple !")

        # CREER FONCTION PANORAMA PCK TROP CHIANT SINON

        elif meetcard == "annaibito_mer":
            pass # get pano card from mer

        elif meetcard == "annaibito_mont":
            pass # get pano card from mont

        elif meetcard == "annaibito_riz":
            if player.riz == 0:
                player.riz += 1
                player.pts += 1

            elif player.riz == 1:
                player.riz += 1
                player.pts += 2

            elif player.riz == 2:
                player.riz += 1
                player.pts += 3
                if riz_complete == 0:
                    riz_first = player
                riz_complete += 1

            # Si panorama riziere deja complet
            elif player.riz == 3:
                panoc = input("Panorama rizière complet. Choisir un autre panorama [mont/mer]: ")
                if panoc == "mont":
                    pass

        elif meetcard == "kuge":
            player.purse += 3
            print("Carte Kuge, vous gagnez 3 pièces !")
        elif meetcard == "shokunin":
            pass # get 1 random souvenir card
            print("Carte Shokunin, vous gagnez 1 carte rencontre aléatoire !")
        elif meetcard == "samurai":
            player.pts += 3
            print("Carte Samurai, vous gagnez 3 points !")

    # Ferme
    if case == "ferme":
        player.purse += 3
        print("Vous gagnez 3 pièces.")

    # Source chaude
    if case == "source":
        #pioche carte
        sccard = random.randint(2,3)
        player.pts += sccard
        print(f"Vous piochez une carte source chaud valant {sccard} points. +{sccard}pts !")

    # Rizière
    if case == "riziere":
        if player.riz == 0:
            player.riz += 1
            player.pts += 1

        elif player.riz == 1:
            player.riz += 1
            player.pts += 2

        elif player.riz == 2:
            player.riz += 1
            player.pts += 3
            if riz_complete == 0:
                riz_first = player
            riz_complete += 1

    # Montagne
    if case == "montagne":
        if player.mont == 0:
            player.mont += 1
            player.pts += 1

        elif player.mont == 1:
            player.mont += 1
            player.pts += 2

        elif player.mont == 2:
            player.mont += 1
            player.pts += 3

        elif player.mont == 3:
            player.mont += 1
            player.pts += 4
            if mont_complete == 0:
                mont_first = player
            mont_complete += 1

    # Mer
    if case == "mer":
        if player.mer == 0:
            player.mer += 1
            player.pts += 1

        elif player.mer == 1:
            player.mer += 1
            player.pts += 2

        elif player.mer == 2:
            player.mer += 1
            player.pts += 3

        elif player.mer == 3:
            player.mer += 1
            player.pts += 4

        elif player.mer == 4:
            player.mer += 1
            player.pts += 5
            if mer_complete == 0:
                mer_first = player
            mer_complete += 1