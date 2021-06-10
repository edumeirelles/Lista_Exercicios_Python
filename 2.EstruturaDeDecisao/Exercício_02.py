# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

while True:
    try:
        x = int(input('Digite um número: '))
        if x > 0:
            print(f'O número {x} é positivo.')
        elif x < 0:
            print(f'O número {x} é negativo.')
        else:
            print(f'O número {x} é neutro.')
    except ValueError:
        print('Número Inválido.')
    else:
        break