# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:28:27 2023

@author: student
"""
import random

def czy_parzysta(liczba):
    return liczba % 2 == 0
losowa = random.randint(1,100)
wynik = czy_parzysta(losowa)

if wynik:
    print(f"Liczba {losowa} jest parzysta")
else:
    print(f"Liczba {losowa} jest nieparzysta")