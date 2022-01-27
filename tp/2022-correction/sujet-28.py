# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:44:15 2022

@author: CPEGM

Sujet n°28

"""

# Exercice 1
def moyenne(T):
    res = 0.0
    for elt in T:
        res += elt
    return res / len(T)

# Exercice 2
def dec_to_bin(a):
    bin_a = str(a % 2)
    a = a//2
    while a > 0 :
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a
