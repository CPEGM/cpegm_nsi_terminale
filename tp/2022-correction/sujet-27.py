# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 17:09:31 2022

@author: CPEGM

Sujet n°27

"""

# Exercice 1


def taille(d, c):
    n = 0

    return n


a = {'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['', ''], 'D': ['C', 'E'],
     'C': ['', ''], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'],
     'H': ['', '']}

print(taille(a, 'F'))

# Exercice 2


def tri_iteratif(tab):
    for k in range(len(tab)-1, 0, -1):
        imax = ...
        for i in range(0, ...):
            if tab[i] > ...:
                imax = i
        if tab[imax] > ...:
            ..., tab[imax] = tab[imax], ...
    return tab
