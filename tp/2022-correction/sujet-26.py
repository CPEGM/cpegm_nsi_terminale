# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 17:03:35 2022

@author: CPEGM

Sujet n°26

"""

# Exercice 1


def RechercheMin(T):
    return min(T)


# Exercice 2


def separe(tab):
    i = 0
    j = len(tab) - 1
    while i < j:
        if tab[i] == 0:
            i = i + 1
        else:
            tab[i], tab[j] = tab[j], tab[i]
            j = j - 1
    return tab
