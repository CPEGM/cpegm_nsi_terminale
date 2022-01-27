# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 13:58:22 2022

@author: CPEGM

Sujet n°2

"""

# Exercice 1
def moyenne(tab):


    res = 0.0
    for elt in tab:
        res += elt
    return res /len(tab)

# Exercice 2
# def tri(tab):
#     #i est le premier indice de la zone non triee, j le dernier indice.
#     #Au debut, la zone non triee est le tableau entier.
#     i= ...
#     j= ...
#     while i != j :
#         if tab[i]== 0:
#             i= ...
#         else :
#             valeur = tab[j]
#             tab[j] = ...
#             ...
#             j= ...
#     ...
