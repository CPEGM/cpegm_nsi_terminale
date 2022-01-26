# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:38:45 2022

@author: CPEGM

Sujet n° 3

"""

# Exercice 1

def delta(L):
    if len(L) == 1:
        return L[0]

    res = [L[0]]
    for k in range(1, len(L)):
        res.append(L[k]-L[k-1])
    return res


# Exercice 2

class Noeud:
    '''
    Classe implémentant un noeud d'arbre binaire disposant de 3 attribut:
        - valeur : la valeur de l'étiquette,
        - gauche : le sous-arbre gauche,
        - droite : le sous-arbre droit.
    '''
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

    def est_une_feuille(self):
        ''' Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None

def expression_infixe(e):
    s = ''
    if e.gauche is not None:
        s = s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit)
    if e.est_une_feuille():
            return s

    return '('+ s +')'

e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None)))
