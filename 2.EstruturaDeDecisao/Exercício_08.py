# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

lista = []

for i in range(1,4):
    while True:
        try:
            x = float(input(f'Digite o preço do produto {i}: ').replace(',','.'))
            lista.append(x)
        except ValueError:
            print('Número Inválido.')
        else:
            break

print(f'Você deverá comprar o produto {lista.index(min(lista))+1}')