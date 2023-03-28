import random

def checkstation(player, case):
    
    # Relais
    if case == "relais":
        pass # pioche n+1 cartes repas pour le 1er arrivé et achète ou non le repas, puis repose le paquet restant de côté pour les suivants
    
    # Echoppe
    if case == "echoppe":
        pass #pioche 3 random cartes souvenirs et décide d'en acheter 1, 2, 3 ou aucune
    
    # Temple
    if case == "temple":
        pass #put 1, 2 or 3 coins in temple slot

    # Rencontre
    if case == "rencontre":
        #pioche carte
        l_meet = ['miko', 'miko', 'annaibito_mer', 'annaibito_mer', 'annaibito_mer', 'annaibito_mont', 'annaibito_mont', 'annaibito_riz', 'kuge', 'kuge', 'shokunin', 'shokunin', 'samurai', 'samurai']
        random.shuffle(l_meet)
        meetcard = l_meet[0]

        if meetcard == "miko":
            pass # put coin from bank in temple slot
        elif meetcard == "annaibito_mer":
            pass # get pano card from mer
        elif meetcard == "annaibito_mont":
            pass # get pano card from mont
        elif meetcard == "annaibito_riz":
            pass # get pano card from riz
        elif meetcard == "kuge":
            pass # get 3 coins
        elif meetcard == "shokunin":
            pass # get 1 random souvenir card
        elif meetcard == "samurai":
            pass # get 3 points

    # Ferme
    if case == "ferme":
        player.purse += 3
        print("Vous gagnez 3 pièces.")

    # Source chaude
    if case == "source":
        #pioche carte
        l_sc = [2,3]
        random.shuffle(l_sc)
        sccard = l_sc[0]

        if sccard == 2:
            player.pts += 2
            print("Vous piochez une carte source chaude valant 2 points !")
        elif sccard == 3:
            player.pts += 3
            print("Vous piochez une carte source chaude valant 3 points !")

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