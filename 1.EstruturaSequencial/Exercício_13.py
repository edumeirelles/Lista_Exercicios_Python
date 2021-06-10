# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print('=== CALCULADORA DE PESO IDEAL ===\n')

while True:
    print('Selecione seu sexo:\n')
    print('\t1 - Mulher')
    print('\t2 - Homem')
    print('\t0 - Fechar Programa\n')
    op = input('Digite a opção: ')

    while op != '1' and op != '2' and op != '0':
        print('Opção Inválida. Tente Novamente.')
        op = input('Digite a opção: ')

    if op == '1':
        while True:
            try:
                x = float(input('Digite a altura: ').replace(',','.'))
                peso_ideal = 62.1 * x - 44.7
                print('Peso Ideal:', format(peso_ideal,'.2f').replace('.',','))
                print()
            except ValueError:
                print('Altura Inválida.')
            else:
                break
    elif op == '2':
        while True:
            try:
                x = float(input('Digite a altura: ').replace(',','.'))
                peso_ideal = 72.7 * x - 58
                print('Peso Ideal:', format(peso_ideal,'.2f').replace('.',','))
                print()
            except ValueError:
                print('Altura Inválida.')
            else:
                break
    else:
        print()
        print('Obrigado por usar a Calculadora de Peso Ideal')
        break