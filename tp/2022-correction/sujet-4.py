# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 15:07:43 2022

@author: CPEGM

Sujet 4

"""

# Exercice 1

def recherche(L):
    res = []
    for k in range(1, len(L)):
        if L[k] - L[k-1] == 1:
            res.append((L[k-1], L[k]))
    return res


# Exercice 2

def propager(M, i , j, val):
    if M[i][j] == 0:
        return

    M[i][j] = val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i-1, j, val)

    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M, i+1, j, val)

    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j-1, val)

    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1):
        propager(M, i, j+1, val)

M = [[0,0,1,0],[0,1,0,1],[1,1,1,0],[0,1,1,0]]
