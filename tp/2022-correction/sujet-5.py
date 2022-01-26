# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:26:18 2022

@author: CPEGM

Sujet n°5

"""

# Exercice 1

def RechercheMinMax(T):
    if T == []:
        return {'min': None, 'max': None}

    return {'min': min(T), 'max': max(T)}

tableau = [0,1,4,2,-2,9,3,1,7,1]


# Exercice 2

class Carte:
    """ Initialise Couleur (entre 1 à 4), et Valeur (entre 1 et 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur =v

    """ Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi """
    def getNom(self):
        if ( self.Valeur > 1  and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """ Renvoie la couleur de la carte (parmi pique, coeur, carreau, trèfle)"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trèfle'][self.Couleur -1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """ Remplit le paquet de cartes """
    def remplir(self):
        for c in range(1, 5):
            for v in range(1, 14):
                self.contenu.append(Carte(c, v))

    """ Renvoie la carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        return self.contenu[pos - 1]
