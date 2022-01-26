# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:02:43 2022

@author: CPEGM

Sujet n°8

"""

# Exercice 1

def recherche(v, L):
    for k in range(len(L)):
        if L[k] == v:
            return k
    return -1


# Exercice 2
# Attention la version a été modifiée par rapport à l'original

def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l)-1
    while a < l[i-1] and i >= 0:
        l[i] = l[i-1]
        l[i-1] = a
        i = i - 1
    return l
