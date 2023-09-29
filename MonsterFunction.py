import random

class MonsterMunch():
    def __init__(self, pV=200, pA=30, pD=0, pVitesse=100, Attack={'Charge': 1.2, 'Foudre': 1.7, 'Feu': 1.1}, element='Feu', faiblesse='eau'):
        self.pV_orig = pV                       # PV originaux (à ne pas changer)
        self.pV = pV                            # PV actuels
        self.pA = pA                            # puissance d'attaque
        self.pD = pD                            # caractéristique de défense
        self.pVitesse = pVitesse                # vitesse du Monstre
        self.degats_Infl = 0                    # variable qui stockerant le nombre de dégats infligés par le Monstre
        self.degats = 0                         # variable qui stockerant le nombre de dégats subi par le Monstre
        self.Attack = Attack
        self.element = element
        self.faiblesse = faiblesse

    # Thomas : perso je conseille de rajouter une fonction __eq__, __str__ et éventuellement __repr__


# Définition de la méthode "heal" qui soigne le joueur. Prends en compte une quantité etl'ajoute au pV actuels
    def heal(self, amount):
        if (self.pV + amount) > self.pV_orig:
            self.pV = self.pV_orig
        self.pV += amount



# Définition de la méthode "esquive" qui renvoie >>> True <<< si l'ennemi esquive en fonction des condition. Sinon, renvoie False
    def esquive(self, other):   
        assert isinstance(other, MonsterMunch), "other is not a MonsterMunch"

        # Si l'ennemi est plus rapide que toi, augmenter les chances d'esquiver par palier
        if (self.pVitesse - other.pVitesse) < 0 < -10:
            # return True if random.random.randint(0, 100) < 15 else False
            if random.randint(0,100) < 15:
                return True
            return False
        
        elif (self.pVitesse - other.pVitesse) < 0 < -20:
            if random.randint(0,100) < 30:
                return True
            return False
        
        elif (self.pVitesse - other.pVitesse) < 0 < -30:
            if random.randint(0,100) < 40:
                return True
            return False
        
        elif (self.pVitesse - other.pVitesse) < -50:
            if random.randint(0,100) < 50:
                return True
            return False

        # Si l'ennemi est moins rapide que toi, diminuer les chances d'esquiver pas palier
        elif (self.pVitesse - other.pVitesse) > 10:
            if random.randint(0,100) < 7:
                return True
            return False
        
        else:
            if random.randint(0,100) < 4:
                return True
            return False



# Définition de la méthode "faiblesse" qui renvoie >>> 'Faible' <<< si l'ennemi est faible, >>> Résistant <<< si l'ennemi est resistant, >>> 'none' si rien ne se passe
    def faiblesse(self, other):
        assert isinstance(other, MonsterMunch), "other is not a MonsterMunch"
        elements_faiblesse = {'Feu': 'Eau', 'Pierre': 'Nature', 'Nature':'Feu', 'Eau':'Pierre'}
        elements_resistant = {'Pierre': 'Eau', 'Nature': 'Pierre', 'Eau':'Nature'}
        for key, value in elements_faiblesse.items():
            if self.element == value and other.element == key:
                return 'Faible'
        for key, value in elements_resistant.items():
            if self.element == value and other.element == key:
                return 'Résistant'
        return 'none'
            



# Définition de la méthode "attack" qui
    def attack(self, other):
        assert isinstance(other, MonsterMunch), "other is not a MonsterMunch"
        # Si la défense de l'ennemi est supérieure à l'attaque
        if other.pD > self.pA:
            self.degats_Infl *= random.uniform(0.05, 0.2)
            # self.degats_Infl *= round(random.uniform(0.05, 0.2), 2) # Il vaut mieux arrondir (avec round) les floats générés aléatoirement parce que sinon la ram peut se faire pomper à mort # round(float, 2) = arrondir le float avec deux chiffres après la virgule
        # Chance de coup critique
        elif random.randint(0, 100) == 69:
            self.degats_Infl *= 1.50
        # Si l'attaque est supérieure à la défense de l'ennemi
        else:
            self.degats_Infl *= random.uniform(0.75, 1.0)



        if MonsterMunch.esquive(self, other) is True: # En vrai le "is True" est pas nécessaire
        # Correction : if self.esquive(other) is True:
            return "L'ennemi vous a pris de vitesse et a esquivé"
        else:
            if MonsterMunch.faiblesse(self, other) == 'Faible':
                self.degats_Infl *= 2
                other.pV -= self.degats_Infl
                print(f"Vous avez Infligés {self.degats_Infl} de dégâts à l'ennemis")
                print("L'ennemi est faible")
            elif MonsterMunch.faiblesse(self, other) == 'Résistant':
                self.degats_Infl *= 0.5
                other.pV -= self.degats_Infl
                print(f"Vous avez Infligés {self.degats_Infl} de dégâts à l'ennemis")
                print("L'ennemi est résistant")
            else:
                other.pV -= self.degats_Infl
                print(f"Vous avez Infligés {self.degats_Infl} de dégâts à l'ennemis")



# Définition de la méthode "initiative" qui renvoie le premier ennemi a attaquer
    def initiative(self, other):   
        assert isinstance(other, MonsterMunch), "other is not a MonsterMunch" 
        if self.pVitesse > other.pVitesse:
            return self
        else:
            return other