import random

class MonsterMunch:
    def __init__(self, name='Generic Monster', pV=200, pA=30, pD=0, pVitesse=100, Attack={'Charge': 1.2, 'Coup de queue': 1.7, 'Basique': 1.1}, element='Feu'):
    # Pk pas ajouter des attaques défensives et des attaques qui agissent sur plusieurs tours (comme du poison par exemple)
        self.name = name                        # nom à afficher
        self.pV_orig = pV                       # PV originaux (à ne pas changer)
        self.pV = pV                            # PV actuels
        self.pA = pA                            # puissance d'attaque
        self.pD = pD                            # caractéristique de défense
        self.pVitesse = pVitesse                # vitesse du Monstre
        self.degats_Infl = 0                    # variable qui stock le nombre de dégats infligés par le Monstre
        self.degats = 0                         # variable qui stock le nombre de dégats subi par le Monstre
        self.Attack = Attack                    # variable qui stock les différentes attaques
        self.element = element                  # variable qui stock l'élément du monstre (Il y a 'Feu', 'Eau', 'Pierre' et 'Nature')
        self.faiblesse = 'eau'                  # variable qui stock la faiblesse du monstre ainsi que sa résistance
        self.selected_attack = 'Coup de queue'  # variable qui stock l'attaque sélectionné par le joueur



# Permet de print tous les attributs du MonsterMunch
    def __str__(self):
        return f"Vitesse : {self.pVitesse} | Degats : {self.degats} | Degats infligés : {self.degats_Infl} | PV : {self.pV} | Puissance d'attaque : {self.pA} | Caractéristique de défense : {self.pD} | Element : {self.element} | Faiblesse : {self.faiblesse}"


    # représentation d'un objet MonsterMunch (dans une liste ou autre)
    def __repr__(self):
        return f"•{self.name}•"
    
    
    # test si le nom du monstre correspond avce le nom d'un autre monstre ou avec un str égal
    def __eq__(self, other):
        assert isinstance(other, MonsterMunch) or isinstance(other, str), "On ne peut comparer un MonsterMunch avec autre chose qu'un MonsterMunch ou un string."
        if isinstance(other, MonsterMunch):
            return self.name == other.name
        else:
            return self.name == other



# Définition de la méthode "heal" qui soigne le joueur. Prends en compte une quantité etl'ajoute au pV actuels
    def heal(self, amount):
        if (self.pV + amount) > self.pV_orig:
            self.pV = self.pV_orig
        self.pV += amount



# Définition de la méthode "esquive" qui renvoie >>> True <<< si l'ennemi esquive en fonction des condition. Sinon, renvoie False
    def esquive(self, other):   
        assert isinstance(other, MonsterMunch), "other is not a MonsterMunch"

        # Si l'ennemi est plus rapide que toi, augmenter les chances d'esquiver par palier
        # Si l'ennemi est plus rapide de entre 0 et 10 points, il aura 15% de chances d'esquiver
        if (self.pVitesse - other.pVitesse) < 0 < -10:
            if random.randint(0,100) < 15:                      #on aurait pu faire plus court avec : return True if random.random.randint(0, 100) < 15 else False
                return True
            return False
        
        # Si l'ennemi est plus rapide de entre 0 et 20 points, il aura 30% de chances d'esquiver
        elif (self.pVitesse - other.pVitesse) < 0 < -20:
            if random.randint(0,100) < 30:
                return True
            return False
        
        # Si l'ennemi est plus rapide de entre 0 et 30 points, il aura 40% de chances d'esquiver
        elif (self.pVitesse - other.pVitesse) < 0 < -30:
            if random.randint(0,100) < 40:
                return True
            return False
        
        # Si l'ennemi est plus rapide de entre 0 et 50 points, il aura 50%% de chances d'esquiver
        elif (self.pVitesse - other.pVitesse) < -50:
            if random.randint(0,100) < 50:
                return True
            return False

        # Si l'ennemi est moins rapide que toi, diminuer les chances d'esquiver pas palier.
        # Si l'ennemi est moins rapide de entre 0 et 10 points, il aura 7% de chaces d'esquiver.
        # Sinon, il aura 4% de chaces d'esquiver.
        elif (self.pVitesse - other.pVitesse) > 10:
            if random.randint(0,100) < 7:
                return True
            return False
        
        else:
            if random.randint(0,100) < 4:
                return True
            return False



# Définition de la méthode "faiblesse" qui renvoie >>> 'Faible' <<< si l'ennemi est faible, >>> 'Résistant' <<< si l'ennemi est resistant, >>> 'none' <<< si rien ne se passe
    def faiblesse_resistance(self, other):
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
            


# Définition de la méthode "attack" qui attaque l'ennemi. Prends en compte les résistance et faiblesse de l'ennmei ainsi que sa vitesse
    def attack(self, other):
        assert isinstance(other, MonsterMunch), "other is not a MonsterMunch"
        
        # Si la défense de l'ennemi est supérieure à l'attaque
        if other.pD > self.pA:
            self.degats_Infl *= round(random.uniform(0.05, 0.2), 2)
        
        # Chance de coup critique de 1% (Si le nombre entier random est stirctement égal à 69)
        elif random.randint(0, 100) == 69:
            self.degats_Infl *= 1.50
        
        # Si l'attaque est supérieure à la défense de l'ennemi
        else:
            self.degats_Infl *= random.uniform(0.75, 1.0)

# Récupérer l'attaque séléctionné par le joueur et multiplier les dégâts infligés par les dégâts de l'attaque
        for key, value in self.Attack.items():
            if key == self.selected_attack:
                self.degats_Infl *= value


# Appel la méthode "esquive" et si l'ennemi a esquivé, renvoie "L'ennemi vous a pris de vitesse et a esquivé". 
# Sinon, regarde si l'ennemi est faible, résistant ou rien. Si l'ennemi est faible, augmenter les dégâts infligés. 
# Si il est résistant, réduire les dégâts infligés. Sinon, ne rien faire.
        if self.esquive(other) is True:                                 # "is True" pas nécessaire mais plus simple à lire
            return "L'ennemi vous a pris de vitesse et a esquivé"
        else:
            if self.faiblesse_resistance(other) == 'Faible':
                self.degats_Infl *= 2
                other.pV -= self.degats_Infl
                print(f"Vous avez Infligés {self.degats_Infl} de dégâts à l'ennemis")
                print("L'ennemi est faible")
            
            elif self.faiblesse_resistance(other) == 'Résistant':
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