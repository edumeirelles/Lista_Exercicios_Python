# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

print('Para uma equação de segundo grau na forma ax² + bx + c:')
print()

while True:
    try:
        a = float(input('Digite o valor de a: '))
    except ValueError:
        print('Valor inválido')
    else:
        while True:
            try:
                b = float(input('Digite o valor de b: '))
            except ValueError:
                print('Valor inválido')
            else:
                while True:
                    try:
                        c = float(input('Digite o valor de c: '))
                    except ValueError:
                        print('Valor inválido')
                    else:
                        break
                break
        break

delta = b**2 - 4 * a * c

if delta < 0:
    print('A equação não possui raízes reais')
elif delta == 0:
    x = -b / 2 * a
    print(f'A equação possui uma raíz real x = {x}')
else:
    x1 = (-b + delta)/(2 * a)
    x2 = (-b - delta)/(2 * a)
    print(f'A equação possui duas raízes reais, sendo x\N{SUBSCRIPT ONE} = {x1} e x\N{SUBSCRIPT TWO} = {x2}')