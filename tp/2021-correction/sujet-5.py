# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:41:24 2022

@author: CPEGM

Sujet n°5

"""

# Exercice 1
def convertir(tab):
    res = 0
    for k in range(0, len(tab)):
        res += tab[k] * 2**(len(tab)-1-k)
    return res


# Exercice 2
def tri_insertion(L):
    n = len(L)

    # cas du tableau vide
    if tab == []:
        return L

    for j in range(1,n):
        e = L[j]
        i = j

    # A l'étape j, le sous-tableau L[0,j-1] est trié
    # et on insère L[j] dans ce sous-tableau en déterminant
    # le plus petit i tel que 0 <= i <= j et L[i-1] > L[j].
        while  i > 0 and L[i-1] > ...:
            i = ...

        # si i != j, on décale le sous tableau L[i,j-1] d’un cran
        # vers la droite et on place L[j] en position i
        if i != j:
            for k in range(j,i,...):
                L[k] = L[...]
            L[i] = ...
    return L
