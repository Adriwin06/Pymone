from MonsterFunction import *
from player import *

# class représentant une instance de combat entre deux MonsterMunch
class combat():
    
    # constructeur avec j1 un joueur, j2 un second joueur ou une IA et inventory1 ou inventory 2 les inventaires
    def __init__(self, user, opponent=MonsterMunch()):
        self.j1 = user
        self.j2 = opponent
        self.inventory1 = self.j1.inventory
        if isinstance(opponent, player):
            self.inventory2 = self.j2.inventory
        self.Monstre1 = 'rien zebi'
        
    def debut(self):
        print(f'Un combat commence ! {(self.j1).name} affronte {self.j2.name} ! C\'est l\'heure de choisir vos monstres...')
        print(f'{(self.j1).name}, c\'est à vous de choisir un combatant. Voici vos monstres :')
        for i in range(len(self.inventory1)):
            print(f'• {self.inventory1[i].name}')
        while self.Monstre1 not in self.inventory1:
            self.Monstre1 = input('Lequel voulez-vous envoyer en premier ? ')
        

# tests (à supprimer)
player1 = player('pandipanda', [MonsterMunch(), MonsterMunch(name='Joueur de LoL'), MonsterMunch(name='Esclave')])
duel = combat(player1)
print([MonsterMunch()])
print(MonsterMunch() == MonsterMunch(name='Generic Monster'))
print(MonsterMunch() == MonsterMunch(name='bato'))
print(MonsterMunch() == 'Generic Monster')

# lancement du combat
duel.debut()