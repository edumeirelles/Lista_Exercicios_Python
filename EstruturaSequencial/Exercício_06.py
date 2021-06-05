# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import pi

while True:
    try:
        r = float(input('Digite o raio do círculo: ').replace(',','.'))
        a = pi * (r ** 2)
        print('Um circulo de raio', format(r, '.2f').replace('.',','), 'tem área de', format(a,'.2f').replace('.',','))
    except ValueError:
        print('Valor inválido.')
    else:
        break