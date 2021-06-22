# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

import math
valor = input('Valor do saque: ').replace(',','.')
valor = int(valor)

if 10 <= valor <= 600:

  if valor <= 600:
    n100 = valor // 100
    s100 = valor % 100
  if s100 <= 99:
    n50 = s100 // 50
    s50 = s100 % 50
  if s50 <= 49:
    n10 = s50 // 10
    s10 = s50 % 10
  if s10 < 9:
    n5 = s10 // 5
    s5 = s10 % 5

    print(f'''
Valor Solicitado: R${valor:.2f}
O valor será sacado em:
''')

  if n100 != 0:
    print(f'{n100:.0f} Cédulas de R$100,00')    
  if n50 != 0:
    print(f'{n50:.0f} Cédulas de R$50,00')
  if n10 != 0:
    print(f'{n10:.0f} Cédulas de R$10,00')
  if n5 != 0:
    print(f'{n5:.0f} Cédulas de R$5,00')
  if s5 != 0:
    print(f'{s5:.0f} Cédulas de R$1,00')

else:
  print('Valor indisponível')