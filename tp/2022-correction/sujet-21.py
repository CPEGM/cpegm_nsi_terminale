# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:34:32 2022

@author: CPEGM

Sujet n°21

"""

# Exercice 1
def multiplication(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    res = 0
    if (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
        for k in range(abs(n2)):
            res += abs(n1)
        return res
    else:
        for k in range(abs(n2)):
            res -= abs(n1)
        return res


# Exercice 2
def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """

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
    return False

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))
