# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:49:17 2023

@author: student
"""

def polacz_i_poteguj(list1, list2):
    polaczone_listy = list(set(list1 + list2))
    potegowane_listy = [element ** 3 for element in polaczone_listy]
    return potegowane_listy

lista_a = [1, 2, 3]
lista_b = [2, 3, 4]

wynik = polacz_i_poteguj(lista_a, lista_b)

print(wynik)  