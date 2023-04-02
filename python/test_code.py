l = ["a", "a", "b", "b", "c", "d"]
l2 = [] 
i = 0
pts = 0
if len(l) != 0:

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
        for fam in l:
            if not fam in l2:
                l2.append(fam)

        for fam2 in l2:
            l.remove(fam2)
        print(l2)
    
        pts += ((len(l2)*2) - 1)
        l2 = []
        print(pts)

else:
    print("pas de souvenirs dans la collection.")
    
# Test de l'attribution des points pour les souvenirs