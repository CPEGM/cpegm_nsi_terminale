# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 18:58:53 2022

@author: CPEGM

Sujet n°35

"""
# Exercice 1
def moyenne (tab):
    '''
    moyenne(list) -> float
    Entrée : un tableau non vide d'entiers
    Sortie : nombre de type float
    Correspondant à la moyenne des valeurs présentes dans le tableau
    '''
    m = 0
    for elt in tab:
        m += elt
    return m / len(tab)

assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5

# Exercice 2
def dichotomie(tab, x):
    """
        tab : tableau trie dans l'ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if tab == []:
        return False,1

    # cas ou x n'est pas compris entre les valeurs extremes
    if (x < tab[0]) or (x > tab[len(tab) - 1]):
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
