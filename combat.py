# Par PandEwok
from MonsterFunction import *
from player import *

# class représentant une instance d= Combat entre deux MonsterMunch
class Combat:

    # constructeur avec j1 un joueur, j2 un second joueur ou une IA et backpack1 ou backpack 2 les inventaires
    def __init__(self, user, opponent=MonsterMunch()):
        self.j1 = user
        self.j2 = opponent
        self.backpack1 = self.j1.backpack
        if isinstance(opponent, Player):
            self.backpack2 = self.j2.backpack
            self.Monstre2 = 'rien zebi'
        else:
            self.Monstre2 = opponent
        self.Monstre1 = 'rien zebi'


    # Méthode pour initier le combat ; déclare le début d= Combat et demande aux joueurs de choisir le monstre qu'ils veulent envoyer a= Combat
    # puis l'assigne à Monster1 pour le joueur 1 ou Monster2 pour le joueur 2
    def debut(self):
        print(f"Un combat commence ! {(self.j1).name} affronte {self.j2.name} ! C'est l'heure de choisir vos monstres...")

        # début d= Combat pour joueur 1 (choix du monstre)
        print(f"{(self.j1).name}, c'est à vous de choisir un combatant. Voici vos monstres :")
        for i in range(len(self.backpack1)):
            print(f'• {self.backpack1[i].name}')
        while self.Monstre1 not in self.backpack1:
            self.Monstre1 = input("Lequel voulez-vous envoyer en premier ? ")
        for monstre in self.backpack1:
            if monstre == self.Monstre1:
                self.Monstre1 = monstre
        print(f'Vous avez choisi {self.Monstre1.name} ! {self.Monstre1.name}, go ! \n')

        # début d= Combat pour le joueur 2 (choix du monstre)
        # seulement si l'adversaire est un joueur (ou un pnj considéré comme un joueur)
        if isinstance(self.j2, Player):
            print(f"{(self.j2).name}, c'est à vous de choisir un combatant. Voici vos monstres :")
            for i in range(len(self.backpack2)):
                print(f'• {self.backpack2[i].name}')
            while self.Monstre2 not in self.backpack2:
                self.Monstre2 = input('Lequel voulez-vous envoyer en premier ? ')
            for monstre in self.backpack2:
                if monstre == self.Monstre2:
                    self.Monstre2 = monstre
            print(f'Vous avez choisi {self.Monstre2.name} ! {self.Monstre2.name}, go !')


    # Méthode qui fait un tour de jeu
    def tour_de_jeu(self):
        premier_mon, deuxieme_mon = self.Monstre1.initiative(self.Monstre2)
        if premier_mon == self.Monstre1:
            premier_j, deuxieme_j = j1, j2
        else:
            premier_j, deuxieme_j = j2, j1
        print(f"C'est {premier_mon.name} qui commence à jouer !"
              f"{premier_j.name}, qu'allez-vous faire ?")



# tests (à supprimer)
Player1 = Player('pandipanda', [MonsterMunch(), MonsterMunch(name='Joueur de LoL'), MonsterMunch(name='Esclave')])
Player2 = Player('Le Salaud', [MonsterMunch(name='Zigzaton'), MonsterMunch(name='Greou')])
duel = Combat(Player1, Player2)
print([MonsterMunch()])
print(MonsterMunch() == MonsterMunch(name='Generic Monster'))
print(MonsterMunch() == MonsterMunch(name='bato'))
print(MonsterMunch() == 'Generic Monster')

# lancement du combat
duel.debut()
duel.tour_de_jeu()