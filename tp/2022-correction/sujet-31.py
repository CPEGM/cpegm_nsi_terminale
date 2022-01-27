# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:00:19 2022

@author: CPEGM

Sujet n°31

"""

# Exercice 1
def recherche(a, t):
    cpt = 0
    for elt in t:
        if elt == a:
            cpt += 1
    return cpt

# Exercice 2
def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = s_versee - s_due
    i = len(pieces) - 1
    while a_rendre > 0 :
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i - 1
    return rendu
