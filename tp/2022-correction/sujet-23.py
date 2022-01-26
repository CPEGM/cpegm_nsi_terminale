# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:48:41 2022

@author: CPEGM

Sujet n°23

"""

# Exercice 1
def max_dico(d):
    name, maxi = '', 0
    for elt in d:
        if d[elt] > maxi:
            name, maxi = elt, d[elt]
    return name, maxi

print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50}))

# Exercice 2
class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()

    def affiche(self):
        print(self.contenu)


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if (element != '+') and (element != '*'): # Il fallait changer le "or" en "and"
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return p.depiler()
