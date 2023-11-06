# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:48:25 2023

@author: student
"""

def czy_zawiera(lista, wartosc):
    return wartosc in lista

lista_liczb = [1, 2, 3, 4, 5]
wartosc_do_sprawdzenia = 3


wynik = czy_zawiera(lista_liczb, wartosc_do_sprawdzenia)

print(wynik)  