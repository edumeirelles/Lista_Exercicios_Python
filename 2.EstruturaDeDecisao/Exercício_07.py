# Faça um Programa que leia três números e mostre o maior e o menor deles.

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

print(f'O maior número é: {max(lista)}')
print(f'O menor número é: {min(lista)}')
