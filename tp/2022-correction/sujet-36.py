# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 18:30:12 2022

@author: CPEGM

Sujet n°36

"""

# Exercice 1


from math import sqrt, inf   # import de la fonction racine carree


def recherche(T, n):
    for k in range(len(T)-1, -1, -1):
        if T[k] == n:
            return k
    return len(T)


# Exercice 2


def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"


def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant a la plus
    courte distance du point depart."""
    point = tab[0]
    min_dist = inf  # Il faut importer inf pour définir l'infini
    for i in range(1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point


assert plus_courte_distance(
    [(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"
