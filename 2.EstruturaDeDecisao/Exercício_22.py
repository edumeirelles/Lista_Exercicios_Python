# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

while True:
    try:
        x = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Número inválido.')
    else:
        break

if x % 2 == 0:
    print(f'O número {x} é par')
else:
    print(f'O número {x} é ímpar.')