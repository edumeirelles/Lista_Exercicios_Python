# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a. salário bruto. 
# b. quanto pagou ao INSS. 
# c. quanto pagou ao sindicato. 
# d. o salário líquido. 
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

while True:
    
    try:
        hora = float(input('Qual o valor da hora trabalhada?: ').replace(',','.'))
    except ValueError:
        print('Número inválido.')
    else:
        while True:
            try:
                numero_horas = float(input('Quantas horas de trabalho por mês?: ').replace(',','.'))
            except ValueError:
                print('Número inválido.')
            else:
                break
        break

salario_bruto = hora * numero_horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sind = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sind

print(f'+ Salário Bruto : R$ {salario_bruto:.2f}\n- IR = R$ {ir:.2f}\n- INSS = R$ {inss:.2f}\n- Sindicato = R$ {sind:.2f}\n= Salário Líquido = R$ {salario_liquido:.2f}')