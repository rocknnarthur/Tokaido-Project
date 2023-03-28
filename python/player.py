class Player:
    def __init__(self, pseudo, couleur, station, argent):
        self.pseudo = pseudo
        self.color = couleur
        self.locate = station
        self.purse = argent
        self.pts = 0
        self.amen = 0
        self.riz = 0
        self.mont = 0
        self.mer = 0

    def afficher(self):
        print(f"{self.pseudo}, {self.color}, station {self.locate}, {self.purse} pieces, {self.pts} points")