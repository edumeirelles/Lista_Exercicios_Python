# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

while True:
    try:
        valor = float(input('Digite o valor da hora trabalhada: R$ ').replace(',','.'))
        while True:
            try:
                horas = float(input('Digite o número de horas trabalhadas: ').replace(',','.'))
                print('Salário = R$', format(valor * horas, '_.2f').replace('.',',').replace('_','.'))
            except ValueError:
                print('Valor Inválido.')
            else:
                break
    except ValueError:
        print('Valor Inválido.')
    else:
        break