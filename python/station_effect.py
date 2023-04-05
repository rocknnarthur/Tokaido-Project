import random
import csv
from player import Player

riz_complete = 0
mont_complete = 0
mer_complete = 0
riz_first = None
mont_first = None
mer_first = None

# Fonction about landscape effect
def panoramacheck(player, case):

    global riz_complete, mont_complete, mer_complete, riz_first, mont_first, mer_first

    if case == "riziere":
        if player.riz < 3:
            player.riz += 1
            player.pts += player.riz
            print(f"Vous obtenez +1 carte panorama rizière. Total = {player.riz}")
            # Si panorama rizière complété
            if player.riz == 3:
                print(f"Bravo, le joueur {player.color} a complété le panorama rizière !")
                if riz_complete == 0:
                    riz_first = player
                    riz_first.pts += 3
                    print(f"Le joueur {riz_first.color} {riz_first.pseudo} obtient la carte accomplissement panorama rizière. +3pts bonus !")
                riz_complete += 1
                
            return True
        
        else:
            print("Vous avez déjà complété ce panorama.")
            return False

    elif case == "montagne":
        if player.mont < 4:
            player.mont += 1
            player.pts += player.mont
            print(f"Vous obtenez +1 carte panorama montagne. Total = {player.mont}")
            # Si panorama montagne complété
            if player.mont == 4:
                print(f"Bravo, le joueur {player.color} a complété le panorama montagne !")
                if mont_complete == 0:
                    mont_first = player
                    mont_first.pts += 3
                    print(f"Le joueur {mont_first.color} {mont_first.pseudo} obtient la carte accomplissement panorama montagne. +3pts bonus !")
                mont_complete += 1
                
            return True

        else:
            print("Vous avez déjà complété ce panorama.")
            return False

    elif case == "mer":
        if player.mer < 5:
            player.mer += 1
            player.pts += player.mer
            print(f"Vous obtenez +1 carte panorama mer. Total = {player.mer}")
            # Si panorama mer complété
            if player.mer == 5:
                print(f"Bravo, le joueur {player.color} a complété le panorama mer !")
                if mer_complete == 0:
                    mer_first = player
                    mer_first.pts += 3
                    print(f"Le joueur {mer_first.color} {mer_first.pseudo} obtient la carte accomplissement panorama mer. +3pts bonus !")
                mer_complete += 1
                
            return True

        else:
            print("Vous avez déjà complété ce panorama.")
            return False



mealdraw = []
# Check the station for applying effect on player
def checkstation(player, case, l_meet, l_souvenir, l_meal, player_n, gamemode):

    global mealdraw

    # Relais
    if case == "relais":

        if player.purse > 0:
            # En fonction du mode de jeu, change ou non le nombre de cartes repas à piocher
            if gamemode == 3:
                n_meal = player_n
            else:
                n_meal = player_n+1

            # Pioche n+1 cartes repas (Tous les autres modes) ou pioche n cartes repas (Mode Gastronomie)
            if len(mealdraw) == 0:
                for meal in range(0, n_meal):
                    mealdraw.append(l_meal[meal])
                del(l_meal[0:3])

            
            
            print(l_meal)
            print(mealdraw)
            
            small_price = 10
            price = 0
            for m in mealdraw:
                with open('python/repas.csv') as mealcsv:
                    reader = csv.reader(mealcsv, delimiter = ';')
                    for row in reader:
                        if m == row[0]:
                            price = int(row[1])
                
                if price < small_price:
                    small_price = price

            if player.purse >= small_price:
                meal_ask = -1
                while not -1 < meal_ask < len(mealdraw)+1:
                    meal_ask = int(input(f"Quel repas voulez-vous acheter ? [entrez position numérique du repas ou '0' pour ne pas acheter] : "))
                    if not -1 < meal_ask < len(mealdraw)+1:
                        print("Entrez une valeur correcte.")
                    
                    elif meal_ask == 0:
                        break

                    else:
                        repas = mealdraw[meal_ask-1]
                        print(repas)
                        with open('python/repas.csv') as mealcsv:
                            reader = csv.reader(mealcsv, delimiter = ';')
                            for row in reader:
                                print(row)
                                if repas == row[0]:
                                    price = int(row[1])
                                    print(price)

                        if player.purse < price:
                            print("Repas trop cher pour vous ! En choisir un autre")
                            meal_ask = -1

                if meal_ask == 0:
                    print("Vous décidez de ne pas manger.")
                    print(mealdraw)
                
                else:
                    player.purse -= price
                    player.pts += 6
                    player.mealdeck.append(repas)
                    print(f"Vous achetez le repas {repas}, -{price} pièces.")
                    mealdraw.remove(repas)
                    print(mealdraw)

            else:
                print("Vous n'avez pas les moyens d'acheter l'un des repas proposés.")

            return True

        else:
            print("Vous n'avez pas d'argent donc aucun achat de repas possible.")
            return True
    
    # Echoppe
    if case == "echoppe":
        if player.purse > 0:
            # Pioche 3 cartes souvenirs
            souvdraw = []
            souvdepot = []
            for souv in range(0, 3):
                souvdraw.append(l_souvenir[souv])
            del(l_souvenir[0:3])
            
            print(l_souvenir)
            print(souvdraw)
            
            for s in souvdraw:
                with open('python/souvenir.csv') as souvcsv:
                    reader = csv.reader(souvcsv, delimiter = ';')
                    for row in reader:
                        if s == row[1]:
                            price = int(row[2])

                if player.purse >= price:
                    while True:
                        souv_ask = int(input(f"Voulez-vous acheter le souvenir {s} pour {price} pièces [oui=1 ou non=0] : "))
                        if souv_ask == 0:
                            print("Vous décidez de ne pas l'acheter.")
                            souvdepot.append(s)
                            break

                        elif souv_ask == 1:
                            player.purse -= price
                            player.souvdeck.append(s)
                            print(f"Vous achetez le souvenir {s}, -{price} pièces.")
                            break

                        else:
                            print("Entrez une réponse correcte.")

                else:
                    print(f"Vous n'avez pas les moyens d'acheter ce souvenir: {s} valant {price} pièces")

            random.shuffle(souvdepot)
            l_souvenir.extend(souvdepot)
            print(l_souvenir)
            return True

        else:
            print("Vous ne pouvez pas y aller sans argent.")
            return False
    
    # Temple
    if case == "temple":
        if player.purse > 0:
            depot = 0
            while not 0 < depot < 4 and player.purse >= depot:
                print("Vous devez déposer un nombre de pièces adéquat avec votre bourse.")
                depot = int(input("Combien de pièces à déposer? [1, 2 ou 3]: "))
            
            player.purse -= depot
            player.amen += depot
            player.pts += depot
            print(f"Vous avez déposé {depot} pièces au temple.")
            return True

        else:
            print("Vous ne pouvez pas y aller sans argent.")
            return False

    # Rencontre
    if case == "rencontre":
        #pioche carte
        meetcard = l_meet[0]
        del(l_meet[0])

        if meetcard == "miko":
            player.amen += 1
            player.meetdeck.append(meetcard)
            print("Carte Miko, une pièce de la banque est placé sur votre slot temple !")
            return True

        elif meetcard == "annaibito_mer":
            print("Carte Annaibito mer !")
            player.meetdeck.append(meetcard)
            if player.mer == 5:
                print("Vous avez déjà complété le panorama mer.")
                lpano_choice = []
                if player.riz < 3:
                    lpano_choice.append("riziere")
                if player.mont < 4:
                    lpano_choice.append("montagne")

                pano = 0
                while not 0 < pano < len(lpano_choice)+1:
                    pano = int(input(f"Choisir un panorama parmi {lpano_choice} [entrez position numérique du panorama]: "))
                    panoramacheck(player, lpano_choice[pano-1])
                return True
            
            else:
                panoramacheck(player, "mer")
                return True
            

        elif meetcard == "annaibito_mont":
            print("Carte Annaibito montagne !")
            player.meetdeck.append(meetcard)
            if player.mont == 4:
                print("Vous avez déjà complété le panorama montagne.")
                lpano_choice = []
                if player.riz < 3:
                    lpano_choice.append("riziere")
                if player.mer < 5:
                    lpano_choice.append("mer")

                pano = 0
                while not 0 < pano < len(lpano_choice)+1:
                    pano = int(input(f"Choisir un panorama parmi {lpano_choice} [entrez position numérique du panorama]: "))
                    panoramacheck(player, lpano_choice[pano-1])
                return True
            
            else:
                panoramacheck(player, "montagne")
                return True

        elif meetcard == "annaibito_riz":
            print("Carte Annaibito rizière !")
            player.meetdeck.append(meetcard)
            if player.riz == 3:
                print("Vous avez déjà complété le panorama rizière.")
                lpano_choice = []
                if player.mer < 5:
                    lpano_choice.append("mer")
                if player.mont < 4:
                    lpano_choice.append("montagne")

                pano = 0
                while not 0 < pano < len(lpano_choice)+1:
                    pano = int(input(f"Choisir un panorama parmi {lpano_choice} [entrez position numérique du panorama]: "))
                    panoramacheck(player, lpano_choice[pano-1])
                return True
            
            else:
                panoramacheck(player, "riziere")
                return True

        elif meetcard == "kuge":
            player.purse += 3
            player.meetdeck.append(meetcard)
            print("Carte Kuge, vous gagnez 3 pièces !")
            return True

        elif meetcard == "shokunin":
            pass # get 1 random souvenir card
            player.meetdeck.append(meetcard)
            print("Carte Shokunin, vous gagnez 1 carte rencontre aléatoire !")
            return True

        elif meetcard == "samurai":
            player.pts += 3
            player.meetdeck.append(meetcard)
            print("Carte Samurai, vous gagnez 3 points !")
            return True

    # Ferme
    if case == "ferme":
        player.purse += 3
        print("Vous gagnez 3 pièces.")
        return True

    # Source chaude
    if case == "source":
        #pioche carte
        sccard = random.randint(2,3)
        player.pts += sccard
        print(f"Vous piochez une carte source chaude valant {sccard} points. +{sccard}pts !")
        return True

    # Rizière
    if case == "riziere" or "montagne" or "mer":
        if panoramacheck(player, case):
            return True
        else:
            return False



# Count all souvenir points at the end of the game
def souvenircheck(player):
    l = []
    l2 = []
    i = 0
    points = 0

    if len(player.souvdeck) != 0:

        for souv in player.souvdeck:
            with open('python/souvenir.csv') as souvcsv:
                reader = csv.reader(souvcsv, delimiter = ';')
                for row in reader:
                    if souv == row[1]:
                        fam = int(row[0])
                        l.append(fam)

        if len(l) <= 4:
            i = 1
        if 4 < len(l) <= 8:
            i = 2
        if 8 < len(l) <= 12:
            i = 3
        if 12 < len(l) <= 16:
            i = 4
        if 16 < len(l) <= 20:
            i = 5
        if 20 < len(l) <= 24:
            i = 6

        for n in range(i):
            for fam1 in l:
                if not fam1 in l2:
                    l2.append(fam1)

            for fam2 in l2:
                l.remove(fam2)
            print(l2)
        
            points += ((len(l2)*2) - 1)
            l2 = []
            print(points)
        
        player.pts += points
        print(f"Le joueur {player.color} gagne {points}pts avec ses cartes souvenirs !")

    else:
        print(f"Aucun souvenir dans la collection du joueur {player.color}.")



# Temple bonus points function
def templebonus(lplayer):

    lp = []
    for p in lplayer:
        lp.append(p)
    
    # Range dans l'ordre décroissant les scores d'offrandes et les joueurs associés
    bigamen = None
    l_amen = []
    l_amen_player = []
    for np in range(len(lp)):
        bigger_amen = -1
        for p in lp:
            if p.amen > bigger_amen:
                bigger_amen = p.amen
                bigamen = p
        l_amen.append(bigger_amen)
        l_amen_player.append(bigamen)
        lp.remove(bigamen)
        # EN FAIT CE CODE EST BON

    # Permet de détecter les égalités d'offrande
    l_verif = [[], [], [], [], []]
    l_verif_player = [[], [], [], [], []]

    for e in l_amen:
        b = 0
        ind = 0
        for nb in range(len(l_amen)):
            if e in l_verif[nb]:
                pass

            else:
                if b == 0:
                    l_verif[l_amen.index(e)].append(e)
                    l_verif_player[l_amen.index(e)].append(l_amen_player[ind])
                    print(l_amen.index(e))
                    b = 1

            ind += 1

    print(l_verif)
    print(l_verif_player)

    # Ajout des points bonus pour le temple
    i = 0
    for lilp in l_verif_player:
        if len(lilp) != 0 and not all(x.amen in (0,0) for x in lilp):
            if i == 0:
                for p in lilp:
                    p.pts += 10
                    print(f"joueur {p.color} +10pts bonus temple")
            if i == 1:
                for p in lilp:
                    p.pts += 7
                    print(f"joueur {p.color} +7pts bonus temple")
            if i == 2:
                for p in lilp:
                    p.pts += 4
                    print(f"joueur {p.color} +4pts bonus temple")
            if i == 3:
                for p in lilp:
                    p.pts += 2
                    print(f"joueur {p.color} +2pts bonus temple")
            i += 1
        elif all(x.amen in (0,0) for x in lilp):
            for p in lilp:
                print(f"Pas de points pour le joueur {p.color} car pas d'offrande")



# SUCCESS FUNCTION !
