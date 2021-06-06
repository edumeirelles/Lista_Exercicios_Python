# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num = []

for i in range(0,2):
    while True:
        try:
            x = int(input('Digite um número inteiro: '))
            num.append(x)
        except ValueError:
            print('Número Inválido.')
        else:
            break
while True:
    try:
        x = float(input('Digite um número real: ').replace(',','.'))
        num.append(x)
    except ValueError:
        print('Número Inválido.')
    else:
        break

print(f'Resulatdo 1: {(num[0]*2)*(num[1]/2):.0f}')
print(f'Resultado 2: {(num[1]*3) + num[2]:.2f}')
print(f'Resultado 3: {num[2] ** 3:.2f}')
