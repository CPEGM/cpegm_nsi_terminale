# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:08:53 2022

@author: CPEGM

Sujet n°16

"""

# Exercice 1

def maxi(L):
    m, pos = L[0], 0
    for k in range(1, len(L)):
        if L[k] > m:
            m, pos = L[k], k
    return (m, pos)


# Exercice 2

def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2
