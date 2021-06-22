# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

while True:
    try:
        x = float(input('Digite um número: '))
    except ValueError:
        print('Número inválido')
    else:
        break

r = round(x)
if x == r:
    print('O número digitado é inteiro.')
else:
    print('O número digitado é decimal.')
