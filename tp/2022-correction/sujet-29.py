# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:20:01 2022

@author: CPEGM

Sujet n°29

"""

# Exercice 1
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    u1, u2 = 1, 1
    for k in range(3, n+1):
        u2, u1 = u2 + u1, u2
    return u2

# Exercice 2
liste_eleves = ['a','b','c','d','e','f','g','h','i','j']
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

def meilleures_notes():
    note_maxi = max(liste_notes)
    nb_eleves_note_maxi = 0
    liste_maxi = []

    for compteur in range(len(liste_notes)):

        if liste_notes[compteur] == max(liste_notes):
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1
            liste_maxi.append(liste_eleves[compteur])

        ''' Cette partie de code ne sert strictement à rien pour répondre à la
        question posée.'''
        # if liste_notes[compteur] > note_maxi:
        #     note_maxi = liste_notes[compteur]
        #     nb_eleves_note_maxi = ...
        #     liste_maxi = [...]

    return (note_maxi, nb_eleves_note_maxi ,liste_maxi)
