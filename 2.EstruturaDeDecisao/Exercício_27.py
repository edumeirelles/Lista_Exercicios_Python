# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

print('=== FRUTARIA ===')
print()
print(' -Tabela de preços- ')
print('Morango - Até 5kg: R$ 2,50 - Acima de de 5kg: R$ 2,20')
print('Maçã - Até 5kg: R$ 1,80 - Acima de 5kg: R$ 1,50')

while True:
    try:
        mo = float(input('Digite a quantidade de morango em kg: '))
        if mo <= 5:
            valor_mo = 2.5 * mo
        else:
            valor_mo = 2.2 * mo
    except ValueError:
        print('Valor inválido.')
    else:
        break

while True:
    try:
        ma = float(input('Digite a quantidade de maçã em kg: '))
        if ma <= 5:
            valor_ma = 1.8 * ma
        else:
            valor_ma = 1.5 * ma
    except ValueError:
        print('Valor inválido.')
    else:
        break

if valor_ma + valor_mo > 25 or ma + mo > 8:
    valor_final = (valor_mo + valor_ma) * 0 + 9
else:
    valor_final = valor_ma + valor_mo
print('Valor a Pagar: R$', format(valor_final,'.2f').replace('.',','))





