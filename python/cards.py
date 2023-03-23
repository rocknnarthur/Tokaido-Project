class Souvenir:
    def __init__(self, nom, famille, prix):
        self.name = nom
        self.category = famille
        self.price = prix
    
class Panorama:
    def __init__(self, nom, paysage, nombre):
        self.name = nom
        self.land = paysage
        self.nbr = nombre

class SourceChaude:
    def __init__(self, points):
        self.pts = points