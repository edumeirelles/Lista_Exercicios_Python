# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso 
# (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

print('=== CLACULADORA DE EXCEDENTE DE PESCA ===\n')

while True:
    try:
        peso = float(input('Digite o peso dos peixes: ').replace(',','.'))
        print()
    except ValueError:
        print('\nPeso inválido.\n')
    else:
        break

excesso = 0
multa = 0

if peso > 50:
  excesso = peso - 50
  multa = float(excesso * 4)
else:
  excesso = 0
  multa = 0
print('O peso excedente é de', format(excesso,'.2f').replace('.',','), 'kg')
print()
print('A multa devida é de R$',format(multa,'.2f').replace('.',','))