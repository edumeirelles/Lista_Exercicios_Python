# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool
#  é R$ 1,90.

print("=== POSTO DE COMBUSTÍVEL ===")
print()
print('Digite a opção desejada')
print('A - Álcool - R$: 1,90')
print('G - Gasolina - R$: 2,50')
op = input('Opção: ').upper()

while op != 'A' and op != 'G':
    print('Opção inválida! Digite "A" para Álcool ou "G" para Gasolina.')
    op = input('Opção: ').upper()

while True:
    try:
        litros = float(input('Digite a quantidade de combustível em litros: ').replace(',','.'))
    except ValueError:
        print('Quantidade inválida. Tente novamente.')
    else:
        break

if op == "A":
    if litros <= 20:
        desconto = 0.97
    else:
        desconto = 0.95
    preco = litros * desconto * 1.9
else:
    if litros <= 20:
        desconto = 0.96
    else:
        desconto = 0.94
    preco = litros * desconto * 2.5

print('Preço: R$'+ format(preco,'.2f').replace('.',','))

