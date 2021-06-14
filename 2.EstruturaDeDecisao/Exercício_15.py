# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lados = []

for i in range(1,4):
    while True:
        try:
            l = float(input(f'Digite a medida do {i}º lado do triângulo: '))
            lados.append(l)
        except ValueError:
            print('Valor inválido.')
        else:
            break

if lados[0] + lados[1] <= lados[2]:
    print('Os lados informados não formam um triângulo!')
else:
    if lados[0] + lados[1] + lados[2] == lados[0] * 3:
        print('Os lados informados formam um triângulo equilátero')
    elif lados[0] == lados[1] or lados[0] == lados[2] or lados[1] == lados[2]:
        print('Os lados informados formam um triângulo isóceles')
    else:
        print('Os lados informados formam um triângulo escaleno')