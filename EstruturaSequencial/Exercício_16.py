# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

print('*.*.* CALCULADORA DE TINTA *.*.*\n')

while True:
    try:
        a = float(input('Qual a área a ser pintada?: ').replace(',','.'))
    except ValueError:
        print('Valor Inválido.')
    else:
        break

v = a / 3
l = math.ceil(v / 18)
p = float(l * 80)
print(f'Quantidades de latas = {l}\nPreço = R$ {p:.2f}')