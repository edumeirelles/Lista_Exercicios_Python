# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

from typing import Pattern


print('\n=== CALCULADORA DE FOLHA DE PAGAMENTO ===\n')
while True:
    try:
        vh = float(input('Digite o valor da hora trabalhada: ').replace(',','.'))
    except ValueError:
        print('Valor Inválido.')
    else:
        while True:
            try:
                ht = int(input('Digite o número de horas trabalhadas: '))
                print()
            except ValueError:
                print('Valor Inválido.')
            else:
                break
        break

sb = vh * ht
sind = sb * 0.03
inss = sb * 0.1
fgts = sb * 0.11

if sb > 2500:
    ir = sb * 0.2
elif 2500 >= sb > 1500:
    ir = sb * 0.1
elif 1500 >= sb > 900:
    ir = sb * 0.05
else:
    ir = 0

desc = sind + inss + ir

print(f'Salário Bruto: ({vh:.2f} * {ht})\t: R$',format(vh * ht,'.2f').replace('.',','))
print(f'(-) IR ({ir/sb*100:.0f}%):\t\t        : R$', format(ir,'.2f').replace('.',','))
print(f'(-) INSS ({inss/sb*100:.0f}%):\t\t\t: R$', format(inss,'.2f').replace('.',','))
print(f'(-) Sindicato ({sind/sb*100:.0f}%):\t\t: R$', format(sind,'.2f').replace('.',','))
print(f'FGTS ({fgts/sb*100:.0f}%):\t\t\t: R$', format(fgts,'.2f').replace('.',','))
print('Total de descontos:\t\t: R$', format(desc,'.2f').replace('.',','))
print('Salário Líquido:\t\t: R$', format(sb-desc,'.2f').replace('.',','))  



