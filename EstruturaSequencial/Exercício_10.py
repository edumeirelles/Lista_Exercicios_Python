# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

while True:
    try:
        c = float(input('Temperatura em Celcius: '))
        while c <= -273.15:
            print('Temperatura Inválida.')
            c = float(input('Temperatura em Celcius: '))
    except ValueError:
        print('Temperatura Inválida.')
    else:
        break            
        
f = (c*9/5) + 32
print(f'A temperatura em Fahrenheit é {f:.1f}')