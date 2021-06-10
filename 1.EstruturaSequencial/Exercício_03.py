# Faça um Programa que peça dois números e imprima a soma.

while True:
    try:
        x = int(input('Digite o primeiro número: '))   
    except ValueError:
        print('Número Inválido. Digite um número inteiro.')    
    else:
        while True:
            try:
                y = int(input('Digite o segundo número: '))
                print(f'Soma = {x + y}')
            except ValueError:
                print('Número Inválido. Digite um número inteiro.')
            else:
                break
        break
