# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 19:24:41 2022

@author: CPEGM

Sujet n°7

"""

# Exercice 1

def conv_bin(n):
    T = []
    while n // 2:
        T.append(n%2)
        n = n//2
    T.append(n%2)
    return T[::-1], len(T)


# Exercice 2
def tri_bulles(T):
    n = len(T)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if T[j]> T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T
