# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:34:43 2022

@author: CPEGM

Sujet n°14

"""

# Exercice 1
def correspond(p1, p2):
    etat = True
    if len(p1) != len(p2):
        return False
    else:
        for k in range(len(p1)):
            if p1[k] == p2[k] or p2[k] == '*':
                continue
            else:
                return False
    return etat


# Exercice 2
def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant
    à un plan d'envoi de messages entre `N` personnes A, B, C,
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon.
    '''
    personne = 'A'
    N = len(plan)
    for i in range(N-1):
        if plan[personne] == 'A':
            return False
        else:
            personne = plan[personne]
    return True

plan_a = {'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}
plan_b = {'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'}
plan_c = {'A':'B', 'F':'C', 'C':'D', 'E':'A', 'B':'F', 'D':'E'}
plan_d = {'A':'B', 'F':'A', 'C':'D', 'E':'C', 'B':'F', 'D':'E'}
