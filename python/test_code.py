from player import Player

p1 = Player("Art333", "green", 1, 7)
p2 = Player("B", "purple", 1, 7)
p1.amen += 1
p2.amen += 0

lp = [p1, p2]


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
    l_amen_player.append(bigamen.color)
    lp.remove(bigamen)
    # A MODIFIER DE TOUTE URGENCE ! CA DONNE QUE LES PLUS GRANDS ET DU COUP CEUX CHECKER APRES SONT NIQUES

    print(l_amen)
    print(l_amen_player)