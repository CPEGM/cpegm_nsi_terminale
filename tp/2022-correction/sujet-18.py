# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:50:51 2022

@author: CPEGM

Sujet n°18

"""

# Exercice 1

def mini(t1, t2):
    min , pos= t1[0], 0
    for k in range(1, len(t1)):
        if min > t1[k]:
            min, pos= t1[k], k
    return min, t2[pos]

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

# Exercice 2
def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
        result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)
