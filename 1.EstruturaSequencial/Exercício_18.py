# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

import math

print('Calculadora de velocidade de download\n')
while True:

    try:
        tam_mb = float(input('Qual o tamanho do arquivo em MB?: ').replace(',','.'))
    except ValueError:
        print('Valor Inválido.')
    else:
        while True:
            try:
                vel = float(input('Qual a velocidade da conexão em Mbps?: ').replace(',','.'))
            except ValueError:
                print('Valor Inválido.')
            else:
                break
        break

vel_mb = vel / 8

tempo = (tam_mb / vel_mb) / 60
print(f'O tempo estimado é de {tempo:.2f} minutos')