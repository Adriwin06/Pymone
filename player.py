# Par PandEwok
from MonsterFunction import *

class Player:

    def __init__(self, name='Player', inventory=[]):
        self.name = name
        self.backpack = inventory


    #ajouter un MonsterMunch à l'inventaire
    def add(self, Monster):
        self.backpack.append(Monster)