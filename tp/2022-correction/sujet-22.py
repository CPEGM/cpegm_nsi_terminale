# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:42:43 2022

@author: CPEGM

Sujet n°22

"""
# Exercice 1
def renverse(mot):
    return mot[::-1]

# Exercice 2
def crible(N):
    """renvoie un tableau contenant tous les nombres premiers plus petit que N"""
    premiers = []
    tab = [True] * N
    tab[0], tab[1] = False, False
    for i in range(2, N):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2*i, N, i):
                tab[multiple] = False
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
