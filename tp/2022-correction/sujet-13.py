# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:03:24 2022

@author: CPEGM

Sujet n°13

"""

# Exercice 1

def rendu(somme_a_rendre):
    billet = [5, 2, 1]
    r = [0, 0, 0]
    k = 0
    while k <= 2:
        if somme_a_rendre >= billet[k]:
            somme_a_rendre -= billet[k]
            r[k] += 1
        else:
            k += 1
    return r


# Exercice 2

class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element)
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != None :
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None
