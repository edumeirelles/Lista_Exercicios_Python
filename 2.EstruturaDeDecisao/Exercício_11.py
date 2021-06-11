# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

nome = input('Digite o nome do colaborador: ')
while True:
    try:
        s = float(input(f'Digite o salário atual de {nome}: ').replace(',','.'))
    except ValueError:
        print('Valor inválido.')
    else:
        break

if s >= 1500:
    r = 1.05
elif 1500 > s >= 700:
    r = 1.1
elif 700 > s >= 280:
    r = 1.15
else:
    r = 1.2

ns = s * r

print(f'O salário de {nome} era', format(s,'.2f').replace('.',','))
print('O percentual de reajuste foi de', format((r - 1)*100,'.2f').replace('.',',')+'%')
print('O valor do aumento foi de', format(ns - s,'.2f').replace('.',','))
print(f'O novo salário de {nome} é R$', format(ns,'.2f').replace('.',','))
