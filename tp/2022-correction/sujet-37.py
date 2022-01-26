# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 18:15:02 2022

@author: CPEGM

Sujet n°37

"""

# Exercice 1


def verifie(T):
    for k in range(len(T)-1):
        if T[k] <= T[k+1]:
            continue
        else:
            return False
    return True


# Exercice 2
urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales',
        'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba',
        'Extra Vomit', 'Lady Baba', 'Extra Vomit']


def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat


def vainqueur(election):
    # vainqueur = ...
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax:
            nmax = election[candidat]
            # vainqueur = ...   cette variable vainqueur est inutile
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale
