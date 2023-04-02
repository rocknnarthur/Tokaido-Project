import random
import csv

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
            if player.riz == 3:
                if riz_complete == 0:
                    riz_first = player
                    print(riz_first.pseudo)
                riz_complete += 1
                print(f"Bravo, le joueur {player.color} a complété le panorama rizière !")
            return True
        
        else:
            print("Vous avez déjà complété ce panorama.")
            return False

    elif case == "montagne":
        if player.mont < 4:
            player.mont += 1
            player.pts += player.mont
            print(f"Vous obtenez +1 carte panorama montagne. Total = {player.mont}")
            if player.mont == 4:
                if mont_complete == 0:
                    mont_first = player
                    print(mont_first.pseudo)
                mont_complete += 1
                print(f"Bravo, le joueur {player.color} a complété le panorama montagne !")
            return True

        else:
            print("Vous avez déjà complété ce panorama.")
            return False

    elif case == "mer":
        if player.mer < 5:
            player.mer += 1
            player.pts += player.mer
            print(f"Vous obtenez +1 carte panorama mer. Total = {player.mer}")
            if player.mer == 5:
                if mer_complete == 0:
                    mer_first = player
                    print(mer_first.pseudo)
                mer_complete += 1
                print(f"Bravo, le joueur {player.color} a complété le panorama mer !")
            return True

        else:
            print("Vous avez déjà complété ce panorama.")
            return False

mealdraw = []

def checkstation(player, case, l_meet, l_souvenir, l_meal, player_n):

    global mealdraw

    # Relais
    if case == "relais":

        if player.purse > 0:
            # Pioche n+1 cartes repas
            if len(mealdraw) == 0:
                for meal in range(0, player_n+1):
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
                meal_ask = 0
                while not 0 < meal_ask < len(mealdraw)+1:
                    meal_ask = int(input(f"Quel repas voulez-vous acheter ? [entrez position numérique du repas] : "))
                    if not 0 < meal_ask < len(mealdraw)+1:
                        print("Entrez une valeur correcte.")

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
                            meal_ask = 0 

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

        pass # pioche n+1 cartes repas pour le 1er arrivé et achète ou non le repas, puis repose le paquet restant de côté pour les suivants
    
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