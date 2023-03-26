class Player:
    def __init__(self, pseudo, couleur, station, argent, points):
        self.pseudo = pseudo
        self.color = couleur
        self.locate = station
        self.purse = argent
        self.pts = points

    def afficher(self):
        print(f"{self.pseudo}, {self.color}, station {self.locate}, {self.purse} pieces, {self.pts} points")