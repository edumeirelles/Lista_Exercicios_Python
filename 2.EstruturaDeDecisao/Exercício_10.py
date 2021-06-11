# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

x = input('Qual turno você estuda?(M para Matutino ou V para Vespretino): ').upper()

while x != 'V' and x != 'M':
    print('Turno Inválido.')
    x = input('Qual turno você estuda?(M para Matutino ou V para Vespretino): ').upper()

if x == 'V':
    print('Você estuda no turno Vespertino!')
else:
    print('Você estuda no turno Matutino!')