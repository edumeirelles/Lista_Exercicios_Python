# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

while True:
    try:
        x = int(input('Digite um número: '))
        print(f'O número digitado foi {x}')
    except ValueError:
        print('Número inválido. Digite um número inteiro.')
    else:
        break

