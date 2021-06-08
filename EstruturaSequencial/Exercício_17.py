# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R 
# 80,00 ou em galões de 3,6 litros, que custam R$25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: 
# comprar apenas latas de 18 litros; comprar apenas galões de 3,6 litros; misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

print('=== CALCULADORA DE TINTA ===\n')

while True:
    try:
        area = float(input('Qual a área a ser pintada?: ').replace(',','.'))
        print()
    except ValueError:
        print('\nValor Inválido.\n')
    else:
        break

litros = (area / 6) * 1.1
latas_1 = math.ceil(litros / 18)
galoes_1 = math.ceil(litros / 3.6)
preco_lata = float(latas_1 * 80)
preco_galao = float(galoes_1 * 25)
print('Somente latas de 18 litros\n')
print(f'\tLatas necessárias: {latas_1}')
print(f'\tPreço = R$ {preco_lata:.2f}\n')
print('Somente galões de 3,6 litros\n')
print(f'\tGalões necessários: {galoes_1}')
print(f'\tPreço = R$ {preco_galao:.2f}\n')
print('Misturando Latas e Galões')

if area <= 108:
# 1 lata de 18 litros pinta 108 m²

    print(f'\tGalões necessários: {galoes_1}')
    print(f'\tPreço = R$ {preco_galao:.2f}\n')
else:
    latas_2 = math.floor(litros / 18)
    galoes_2 = math.ceil((litros % 18) / 3.6)
    preco_lata_galao = float((latas_2 * 80) + (galoes_2 * 25))
    print
    print(f'\tSerão necessários {latas_2} latas e {galoes_2} galões.')
    print(f'\tPreço = R$ {preco_lata_galao:.2f}')