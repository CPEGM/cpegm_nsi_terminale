# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:14:09 2022

@author: CPEGM

Sujet n°1

"""

# Exercice 1

def recherche( car, chaine):
    cpt = 0
    for k in chaine:
        if k == car:
            cpt += 1
    return cpt


# Exercice 2

Pieces = [100,50,20,10,5,2,1]

def rendu_glouton_r(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = Pieces[i]
    if p <= arendre:
        solution.append(Pieces[i])
        return rendu_glouton_r(arendre - p, solution, i)
    else:
        return rendu_glouton_r(arendre, solution, i+1)
