# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 17:55:48 2022

@author: CPEGM

Sujet n°38

"""
from random import randint


# Exercice 1
def tri_selectif(T):
    for i in range(len(T) - 1):
        for j in range(i+1, len(T)):
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]
    return T

# Exercice 2


def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre etait ", nb_mystere)
