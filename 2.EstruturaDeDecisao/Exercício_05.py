# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
notas = []
for i in range(1,3):
    while True:
        try:
            x = float(input(f'Digite a {i}ª anota: ').replace(',','.'))
            while x > 10 or x < 0:
                print('Nota Inválida.')
                x = float(input(f'Digite a {i}ª anota: ').replace(',','.'))
            notas.append(x)
        except ValueError:
            print('Nota Inválida.')
        else:
            break

media = sum(notas) / len(notas)
print(f'\nMédia = {media}')

if media == 10:
    print('Aprovado com Distinção')
elif 10 > media >= 7:
    print('Aprovado')
else:
    print('Reprovado')