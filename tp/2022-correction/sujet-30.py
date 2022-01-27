# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:08:04 2022

@author: CPEGM

Sujet n°30

"""

# Exercice 1

# Exercice 2
def rom_to_dec (nombre):

    """ Renvoie l’écriture décimale du nombre donné en chiffres romains """

    dico = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    if len(nombre) == 1:
        return dico[nombre]

    else:
        ### on supprime le premier caractère de la chaîne contenue dans la variable nombre
        ### et cette nouvelle chaîne est enregistrée dans la variable nombre_droite
        nombre_droite = nombre[1:]

        if dico[nombre[0]] >= dico[nombre[1]]:
            return dico[nombre[0]] + rom_to_dec(nombre_droite)
        else:
            return -dico[nombre[0]] + rom_to_dec(nombre_droite)

assert rom_to_dec("CXLII") == 142
