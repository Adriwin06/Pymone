from MonsterFunction import *

class player():
    
    def __init__(self, name='Player', inventory=[]):
        self.name = name
        self.inventory = inventory


    #ajouter un MonsterMunch à l'inventaire
    def add(self, Monster):
        self.inventory.append(Monster)