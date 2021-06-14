# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

while True:
    try:
        ano = int(input('Digite um ano: '))
    except ValueError:
        print('Ano inválido.')
    else:
        break

if ano % 4 == 0 :
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
