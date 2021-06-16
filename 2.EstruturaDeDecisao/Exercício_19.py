# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

while True:
    try:
        x = int(input('Digite um inteiro menor que 1000: '))
    except ValueError:
        print('Número inválido:')
    else:
        break

while x > 1000:
    print('Número inválido.')
    x = int(input('Digite um inteiro menor que 1000: '))

if x < 1000: 
    c = x // 100
    sc = x % 100
if sc <= 99:
    d = sc // 10
    u = sc % 10
if c > 1:
    centena = 'centenas'
else:
    centena = 'centena'
if d > 1:
    dezena = 'dezenas'
else:
    dezena = 'dezena'
if u > 1:
    unidade = 'unidades'
else:
    unidade = 'unidade'
if c != 0 and d != 0 and u != 0:
    print(f'{c:.0f} {centena}, {d:.0f} {dezena} e {u:.0f} {unidade}')
elif c == 0 and d != 0 and u != 0:
    print(f'{d:.0f} {dezena} e {u:.0f} {unidade}')
elif c == 0 and d == 0 and u != 0:
    print(f'{u:.0f} {unidade}')
elif c != 0 and d != 0 and u == 0:
    print(f'{c:.0f} {centena} e {d:.0f} {dezena}')
elif c != 0 and d == 0 and u == 0:
    print(f'{c:.0f} {centena}')
elif c == 0 and d != 0 and u == 0:
    print(f'{d:.0f} {dezena}')
else:
    print(f'{c:.0f} {centena} e {u:.0f} {unidade}') 




