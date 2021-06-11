# Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

x = input('Qual turno você estuda?(M para Matutino, V para Vespretino ou N para Noturno): ').upper()

while x != 'V' and x != 'M' and x != 'N':
    print('Turno Inválido.')
    x = input('Qual turno você estuda?(M para Matutino ou V para Vespretino): ').upper()

if x == 'V':
    print('Boa Tarde! Você estuda no turno Vespertino!')
elif x == 'M':
    print('Bom dia! Você estuda no turno Matutino!')
else:
    print('Boa Noite! Você estuda no turno Noturno')