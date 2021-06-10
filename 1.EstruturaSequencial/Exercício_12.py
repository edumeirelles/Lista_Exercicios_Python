# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

while True:
    try:
        x = float(input('Digite a altura: ').replace(',','.'))
        peso_ideal = 72.7 * x - 58
        print('Peso Ideal:', format(peso_ideal,'.2f').replace('.',','))
    except ValueError:
        print('Número Inválido.')
    else:
        break