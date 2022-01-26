# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:28:47 2022

@author: CPEGM

Sujet n°11

"""

# Exercice 1

def recherche(tab, n):
    for k in range(len(tab)):
        if tab[k] == n:
            return k
    return -1

# Exercice 2

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for elt in message:
        if elt in ALPHABET:
            indice = (position_alphabet(elt) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + elt
    return resultat
