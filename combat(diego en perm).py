from main import *
from player import *

class combat():
    
    def __init__(self, user, opponent=MonsterMunch()):
        self.j1 = user
        self.j2 = opponent
        
    def debut(self):
        print(f'Un combat commence ! {(self.j1).name} affronte {self.j2} ! C\'est l\'heure de choisir vos monstres...')
        print(f'{(self.j1).name}, c\'est à vous de choisir un combatant. Voici vos monstres :')
        
player1 = player('pandipanda', [MonsterMunch()])
duel = combat(player1)
duel.debut()