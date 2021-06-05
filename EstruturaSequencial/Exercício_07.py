# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

while True:
    try:
        l = float(input('Digite a medida do lado do quadrado: ').replace(',','.'))
        a = l ** 2
        print('O dobro da área do quadrado é', format(a * 2,'.2f').replace('.',','))
    except ValueError:
        print('Valor Inválido.')
    else:
        break