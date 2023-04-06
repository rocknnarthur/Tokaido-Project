

argent = 1
depot = 9
print("Avant boucle")
while not argent >= depot or not 0 < depot < 4:
    print("Vous devez déposer un nombre de pièces adéquat avec votre bourse.")
    depot = int(input("Combien de pièces à déposer? [1, 2 ou 3]: "))

print("IL EST OK")