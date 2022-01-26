# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:50:38 2022

@author: CPEGM

Sujet n°25

"""

# Exercice 1


def selection_enclos(T, n):
    res = []
    for elt in T:
        if elt['enclos'] == n:
            res.append(elt)
    return res


animaux = [{'nom': 'Medor', 'espece': 'chien', 'age': 5, 'enclos': 2},
           {'nom': 'Titine', 'espece': 'chat', 'age': 2, 'enclos': 5},
           {'nom': 'Tom', 'espece': 'chat', 'age': 7, 'enclos': 4},
           {'nom': 'Belle', 'espece': 'chien', 'age': 6, 'enclos': 3},
           {'nom': 'Mirza', 'espece': 'chat', 'age': 6, 'enclos': 5}]

# Exercice 2

# Le noyau redemmarre quand in fait le test pour le tableau 1 et 3...
# Voir quel est le problème sur la récursivité


def trouver_intrus(tab, g, d):
    '''
    Renvoie la valeur de l'intrus situé entre les indices g et d
    dans la liste tab où
        tab vérifie les conditions de l'exercice,
        g et d sont des multiples de 3.
    '''
    if g == d:
        return tab[g]

    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if tab[indice] == tab[indice + 1]:
            return trouver_intrus(tab, indice, d)
        else:
            return trouver_intrus(tab, g, indice)
