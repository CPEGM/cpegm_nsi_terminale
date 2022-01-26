# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:03:01 2022

@author: CPEGM

Sujet n°15

"""

# Exercice 1

def nb_repetitions(c, L):
    cpt = 0
    for elt in L:
        if elt == c:
            cpt += 1
    return cpt


# Exercice 2

def binaire(a):
    bin_a = str(a % 2)
    a = a // 2
    while a != 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a
