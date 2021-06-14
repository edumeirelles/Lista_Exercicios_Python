# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dias_semana = ['Domingo', 'Segunda-Feira', 'Terça-Feira','Quarta-Feira','Quinta-Feira', 'Sexta-Feira','Sábado']


while True:
    try:
        x = int(input('Digite o número do dia da semana: '))
        while x > 7 or x < 1:
            print('Dia da semana inválido.')
            x = int(input('Digite o número do dia da semana: '))
        print(f'O {x}º dia da semana é {dias_semana[x-1]}')
    except ValueError:
        print('Dia da semana inválido.')
    else:
        break

