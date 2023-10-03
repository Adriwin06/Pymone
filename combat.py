from MonsterFunction import *
from player import *

class combat():
    
    def __init__(self, user, opponent=MonsterMunch()):
        self.j1 = user
        self.j2 = opponent
        self.inventory1 = self.j1.inventory
        
    def debut(self):
        print(f'Un combat commence ! {(self.j1).name} affronte {self.j2} ! C\'est l\'heure de choisir vos monstres...')
        print(f'{(self.j1).name}, c\'est à vous de choisir un combatant. Voici vos monstres :')
        for i in range(len(self.inventory1)):
            print(f'• {self.inventory1[i]}')
        
player1 = player('pandipanda', [MonsterMunch()])
duel = combat(player1)
print([MonsterMunch()])
duel.debut()