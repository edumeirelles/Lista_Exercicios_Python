# Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

for i in range(1,4):
    while True:
        try:
            x = int(input(f'Digite o {i}º número: '))
            lista.append(x)
        except ValueError:
            print('Número Inválido.')
        else:
            break

lista.sort(reverse=True)

print(lista)