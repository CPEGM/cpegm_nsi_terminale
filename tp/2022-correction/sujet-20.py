# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:30:22 2022

@author: CPEGM

Sujet n°20

"""

# Exercice 1
def xor(L1, L2):
    T = []
    for k in range(len(L1)):
        if L1[k] == L2[k]:
            T.append(0)
        else:
            T.append(1)
    return T


a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]
assert(xor(a, b) == [1, 1, 0, 1, 1, 0, 0, 1])
assert(xor(c, d) == [1, 1, 1, 0])

# Exercice 2
class Carre:
    def __init__(self, tableau = [[]]):
        self.ordre = len(tableau)
        self.valeurs = tableau

    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.valeurs[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        return sum(self.valeurs[i])

    def somme_col(self, j):
        '''calcule la somme des valeurs de la colonne j'''
        return sum([self.valeurs[i][j] for i in range(self.ordre)])

def est_magique(carre):
    n = carre.ordre
    s = carre.somme_ligne(0)

    #test de la somme de chaque ligne
    for i in range(0, n):
        if carre.somme_ligne(i) != s:
            return False

    #test de la somme de chaque colonne
    for j in range(n):
        if carre.somme_col(j) != s:
            return False

    #test de la somme de chaque diagonale
    if sum([carre.valeurs[k][k] for k in range(n)]) != s:
            return False
    if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:
            return False

    return True

c2 = Carre([[1,1],[1,1]])
c3 = Carre([[2,9,4],[7,5,3],[6,1,8]])
c4 = Carre([[4,5,16,9],[14,7,2,11],[3,10,15,6],[13,12,8,1]])

print("c2 magique?", est_magique(c2))
print("c3 magique?", est_magique(c3))
print("c4 magique?", est_magique(c4))
