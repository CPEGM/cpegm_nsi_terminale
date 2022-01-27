# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 17:09:31 2022

@author: CPEGM

Sujet n°27

"""

# Exercice 1


def taille(arbre, lettre):
    if arbre[lettre] == ['', '']:
        return 1
    else:
        if arbre[lettre][0] == '':
            return 1 + taille(arbre, arbre[lettre][1])
        elif arbre[lettre][1] == '':
            return 1 + taille(arbre, arbre[lettre][0])
        else:
            return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])

a = {'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['', ''], 'D': ['C', 'E'],
     'C': ['', ''], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'],
     'H': ['', '']}

# Exercice 2
def tri_iteratif(tab):
    for k in range(len(tab)-1, 0, -1):
        imax = 0
        for i in range(0, k):
            if tab[i] > tab[imax]:
                imax = i
        if tab[imax] > tab[k]:
            tab[k], tab[imax] = tab[imax], tab[k]
    return tab

assert  tri_iteratif([41, 55, 21, 18, 12, 6, 25]) == [6, 12, 18, 21, 25, 41, 55]
