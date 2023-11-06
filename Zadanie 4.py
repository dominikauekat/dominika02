# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:30:16 2023

@author: student
"""
def czy_suma_wieksza_lub_rowna(a, b, c):
    return (a + b) >= c

wynik = czy_suma_wieksza_lub_rowna(2, 2, 5)

print(wynik)  

if wynik:
    print("Suma dwóch pierwszych liczb jest większa lub równa trzeciej")
else:
    print("Suma dwóch pierwszych liczb jest mniejsza niż trzecia")