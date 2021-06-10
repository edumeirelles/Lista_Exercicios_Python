# Faça um Programa que peça dois números e imprima o maior deles.

num = []

for i in range(1,3):
    while True:
        try:
            x = int(input(f'Digite o {i}º número: '))
            num.append(x)
            
        except ValueError:
            print('Número Inválido.')
        else:
            break

print('O maior número é:',max(num))
