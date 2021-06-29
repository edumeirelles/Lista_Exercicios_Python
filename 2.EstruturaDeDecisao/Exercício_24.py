# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

num = []
res = {}

for i in range (1,3):
    while True:
        try:
            x = float(input(f'Digite o {i}º número: '))
            num.append(x)
        except ValueError:
            print('Número Inválido.')
        else:
            break

print('Digite a operação desejada:')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
op = input('Opção: ')

while op != '1' and op != '2' and op != '3' and op != '4':
    print('Opção inválida. Tente novamente')
    op = input('Opção: ')

if op == "1":
    print(f'Soma = {sum(num)}')
    if sum(num) == round(sum(num)):
        if sum(num) % 2 == 0:
            print('A soma é par.')
        else:
            print('A soma é ímpar.')
        if sum(num) < 0:
            print('A soma é negativa.')
        elif sum(num) > 0:
            print('A soma é positiva.')
        else:
            print('A soma é igual a 0')
        print('A soma é um número inteiro')
    else:
        if sum(num) < 0:
            print('A soma é negativa.')
        elif sum(num) > 0:
            print('A soma é positiva.')
        else:
            print('A soma é igual a 0')
        print('A soma é um número decimal')

if op == "2":
    sub = num[0] - num[1]
    print(f'Subtração = {sub}')
    if sub == round(num[0] - num[1]):
        if sub % 2 == 0:
            print('A subtração é par.')
        else:
            print('A subtração é ímpar.')
        if sub < 0:
            print('A subtração é negativa.')
        elif sub > 0:
            print('A subtração é positiva.')
        else:
            print('A subtração é igual a 0')
        print('A subtração é um número inteiro')
    else:
        if sub < 0:
            print('A subtração é negativa.')
        elif sub > 0:
            print('A subtração é positiva.')
        else:
            print('A subtração é igual a 0')
        print('A subtração é um número decimal')

if op == "3":
    mult = num[0] * num[1]
    print(f'Multiplicação = {mult}')
    if mult == round(num[0] * num[1]):
        if mult % 2 == 0:
            print('A multiplicação é par.')
        else:
            print('A multiplicação é ímpar.')
        if mult < 0:
            print('A multiplicação é negativa.')
        elif mult > 0:
            print('A multiplicação é positiva.')
        else:
            print('A multiplicação é igual a 0')
        print('A multiplicação é um número inteiro')
    else:
        if mult < 0:
            print('A multiplicação é negativa.')
        elif mult > 0:
            print('A multiplicação é positiva.')
        else:
            print('A multiplicação é igual a 0')
        print('A multiplicação é um número decimal')

if op == "4":
    div = num[0] / num[1]
    print(f'Divisão = {div}')
    if div == round(num[0] / num[1]):
        if div % 2 == 0:
            print('A divisão é par.')
        else:
            print('A divisão é ímpar.')
        if div < 0:
            print('A divisão é negativa.')
        elif div > 0:
            print('A divisão é positiva.')
        else:
            print('A divisão é igual a 0')
        print('A divisão é um número inteiro')
    else:
        if div < 0:
            print('A divisão é negativa.')
        elif div > 0:
            print('A divisão é positiva.')
        else:
            print('A divisão é igual a 0')
        print('A divisão é um número decimal')