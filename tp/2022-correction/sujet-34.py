# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 19:11:09 2022

@author: CPEGM

Sujet n°34

"""

# Exercice 1
ch='je suis en terminale et je passe le bac et je souhaite poursuivre des etudes pour devenir expert en informatique'

def occurence_max(chaine):
    occurence = [0] * 26
    for elt in chaine:
        if elt != " ":
            occurence[ord(elt) - ord('a')] += 1
    max, pos= occurence[0], 0
    for k in range(1, len(occurence)):
        if occurence[k] > max:
            max, pos = occurence[k], k
    return chr(pos + ord('a'))


# Exercice 2
def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
        d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(len(image)):
        for j in range(len(image[0])):
            L[i][j] = 255 - image[i][j]
    return L


def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
        d'une liste de listes contenant des 0 si la valeur
        du pixel est strictement inferieure au seuil
        et 1 sinon'''

'''
Ici la consigne de l'énoncé diverge de la correction qui est donnée
en exemple dans le sujet... Encore une coquille dans l'énoncé...
'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] < seuil :
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L
