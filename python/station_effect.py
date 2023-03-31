import random

def panoramacheck(player, case):
    if case == "riziere":
        if player.riz < 3:
            player.riz += 1
            player.pts += player.riz
            if player.riz == 3:
                if riz_complete == 0:
                    riz_first = player
                riz_complete += 1
                print("Bravo, vous avez complété le panorama rizière !")
        
        else:
            print("Vous avez déjà complété ce panorama.")
            return False

    elif case == "montagne":
        if player.mont < 4:
            player.mont += 1
            player.pts += player.mont
            if player.mont == 4:
                if mont_complete == 0:
                    mont_first = player
                mont_complete += 1
                print("Bravo, vous avez complété le panorama montagne !")

        else:
            print("Vous avez déjà complété ce panorama.")
            return False

    elif case == "mer":
        if player.mer < 5:
            player.mer += 1
            player.pts += player.mer
            if player.mer == 5:
                if mer_complete == 0:
                    mer_first = player
                mer_complete += 1
                print("Bravo, vous avez complété le panorama mer !")

        else:
            print("Vous avez déjà complété ce panorama.")
            return False


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
            print("Vous ne pouvez pas y aller sans argent.")
            return False

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
            if player.mer == 5:
                lpano_choice = []
                if player.riz < 3:
                    lpano_choice.append("riziere")
                if player.mont < 4:
                    lpano_choice.append("montagne")

                pano = 0
                while not 0 < pano < 3:
                    pano = int(input(f"Choisir un panorama parmi {lpano_choice} [1 ou 2]: "))
                    panoramacheck(player, lpano_choice[pano-1])

        elif meetcard == "annaibito_mont":
            if player.mont == 4:
                lpano_choice = []
                if player.riz < 3:
                    lpano_choice.append("riziere")
                if player.mer < 5:
                    lpano_choice.append("mer")

                pano = 0
                while not 0 < pano < 3:
                    pano = int(input(f"Choisir un panorama parmi {lpano_choice} [1 ou 2]: "))
                    panoramacheck(player, lpano_choice[pano-1])

        elif meetcard == "annaibito_riz":
            if player.riz == 3:
                lpano_choice = []
                if player.mer < 5:
                    lpano_choice.append("mer")
                if player.mont < 4:
                    lpano_choice.append("montagne")

                pano = 0
                while not 0 < pano < 3:
                    pano = int(input(f"Choisir un panorama parmi {lpano_choice} [1 ou 2]: "))
                    panoramacheck(player, lpano_choice[pano-1])

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
    if case == "riziere" or "montagne" or "mer":
        panoramacheck(player, case)