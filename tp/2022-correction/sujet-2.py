# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 14:28:19 2022

@author: CPEGM

Sujet n°2

"""

# Exercice 1

def moyenne(L):
    res = 0.
    coeff = 0
    for k in L:
        res += k[0] * k[1]
        coeff += k[1]
    return res / coeff

# Exercice 2

def pascal(n):
    C = [[1]]
    for k in range(1, n+1):
        Ck = [1]
        for i in range(1, k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C
