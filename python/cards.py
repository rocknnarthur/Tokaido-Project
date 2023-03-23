class Souvenir:
    def __init__(self, nom, famille, prix):
        self.name = nom
        self.category = famille
        self.price = prix
    
class PanoramaCard:
    def __init__(self, nom, paysage, nombre):
        self.name = nom
        self.land = paysage
        self.nbr = nombre

class SourceChaudeCard:
    def __init__(self, points):
        self.pts = points

class RencontreCard:
    def __init__(self, nom, effet):
        self.name = nom
        self.effect = effet