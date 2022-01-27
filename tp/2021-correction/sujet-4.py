# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:33:16 2022

@author: CPEGM

Sujet n°4

"""

# Exercice 1
def moyenne(tab):
    if len(tab) == 1:
        return tab[0]
    else:
        res = 0
        for elt in tab:
            res += elt
        return res / len(tab)

# Exercice 2
def dichotomie(tab, x):
    """
        tab : tableau trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if tab == []:
        return False,1

    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or x > tab[len(tab) - 1]:
        return False,2

    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False, 3

