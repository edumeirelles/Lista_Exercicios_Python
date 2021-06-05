# Faça um Programa que converta metros para centímetros.

while True:
    try:
        x = float(input('Digite a medida em metros: ').replace(',','.'))
        y = x * 100
        print(format(x,'.2f').replace('.',','), f'metros equivalem a {y:.0f} centímetros ')
    except ValueError:
        print('Entrada Inválida.')
    else:
        break