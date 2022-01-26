# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:11:38 2022

@author: CPEGM

Sujet n°6

"""

# Exercice 1

def maxi(L):
    res = (L[0], 0)

    for k in range(1, len(L)):
        if L[k] > res[0]:
            res = (L[k], k)
    return res


# Exercice 2

def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False:
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j += 1
        if j == g:
            trouve = True
        i += 1
    return trouve
