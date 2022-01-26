# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:13:12 2022

@author: CPEGM

Sujet n°12

"""

# Exercice 1

def moyenne(tab):
    if tab == []:
        return 'erreur'
    else:
        res = 0
        for elt in tab:
            res += elt
        return res / len(tab)


# Exercice 2

def tri(tab):
    # i est le premier indice de la zone non triée, j le dernier indice
    # Au début, la zone non triée est le tableau entier.
    i = 0
    j =len(tab) - 1
    while i != j:
        if tab[i] == 0:
            i = i + 1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j - 1
    return tab
