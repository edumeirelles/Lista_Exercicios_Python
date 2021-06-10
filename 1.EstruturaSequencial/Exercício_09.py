# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

while True:
    try:
        f = float(input('Temperatura em Fahrenheit: '))
        while f <= -459.67:
            print('Temperatura Inválida.')
            f = float(input('Temperatura em Fahrenheit: '))
    except ValueError:
        print('Temperatura Inválida.')
    else:
        break
    
c = (f-32) * 5/9
print(f'A temperatura em Celcius é {c:.1f}')