from random import*
class MonsterMunch():
    def __init__(self, pV=200, pA=30, pD=0, pVitesse=100, Attack={'Charge': 1.2, 'Foudre': 1.7, 'Feu': 1.1}):
        self.pV_orig = pV                       # ← PV originaux (à ne pas changer)
        self.pV = pV                            # ← PV actuels
        self.pA = pA                            # ← puissance d'attaque
        self.pD = pD                            # ← caractéristique de défense
        self.pVitesse = pVitesse
        self.degats_Infl = 0
        self.degats = 0
        self.Attack = Attack



# Définition de la méthode "heal" qui soigne le joueur en fonction d'une quantité
    def heal(self, amount):
        if self.pV + amount > self.pV_orig:
            self.pV = self.pV_orig
        self.pV += amount



# Définition de la méthode "esquive" qui renvoie >True si l'ennemi esquive en fonction des condition. Sinon, renvoie False
    def esquive(self, other):   
        assert isinstance(other, MonsterMunch), "other is not a MonsterMunch"

        # Si l'ennemi est plus rapide que toi, augmenter les chances d'esquiver par palier
        if self.pVitesse - other.pVitesse < 0 < -10:
            if random.randint(0,100) < 15:
                return True
            return False
        
        elif self.pVitesse - other.pVitesse < 0 < -20:
            if random.randint(0,100) < 30:
                return True
            return False
        
        elif self.pVitesse - other.pVitesse < 0 < -30:
            if random.randint(0,100) < 40:
                return True
            return False
        
        elif self.pVitesse - other.pVitesse < -50:
            if random.randint(0,100) < 50:
                return True
            return False

        # Si l'ennemi est plus rapide que toi, augmenter les chances d'esquiver pas palier"      
        elif self.pVitesse - other.pVitesse > 10:
            if random.randint(0,100) < 7:
                return True
            return False
        
        else:
            if random.randint(0,100) < 4:
                return True
            return False



# Définition de la méthode "attack" qui
    def attack(self, other):
        assert isinstance(other, MonsterMunch), "other is not a MonsterMunch"
        # Si la défense de l'ennemi est supérieure à l'attaque
        if other.pD > self.pA:
            self.degats_Infl *= random.uniform(0.05, 0.2)
        # Chance de coup critique
        elif randint(0, 100) == 69:
            self.degats_Infl *= 1.50
        # Si l'attaque est supérieure à la défense de l'ennemi
        else:
            self.degats_Infl *= random.uniform(0.75, 1.0)

        if MonsterMunch.esquive(self, other) is True:
            return "L'ennemi vous a pris de vitesse et a esquivé"
        else:
            other.pV -= self.degats_Infl
            print(f"Vous avez Infligés {self.degats_Infl} de dégâts à l'ennemis")



    def initiative(self, other):   
        assert isinstance(other, MonsterMunch), "other is not a MonsterMunch" 
        if self.pVitesse > other.pVitesse:
            return object
        else:
            return other