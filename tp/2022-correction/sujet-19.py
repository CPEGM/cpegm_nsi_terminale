# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 21:05:59 2022

@author: CPEGM

Sujet n°19

"""

# Exercice 1

def multiplication(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    res = 0
    if (n1 > 0 and n2 > 0) or (n1 < 0 and n2 < 0):
        for k in range(abs(n2)):
            res += abs(n1)
        return res
    else:
        for k in range(abs(n2)):
            res -= abs(n1)
        return res


# Exercice 2

def chercher(T,n,i,j):
    if i < 0 or j >= len(T) :
        print("Erreur")
        return None
    if i > j :
        return None
    m = (i+j) // 2
    if T[m] < n :
        return chercher(T, n, m, j)
    elif T[m] > n :
        return chercher(T, n, i, m)
    else :
        return m
