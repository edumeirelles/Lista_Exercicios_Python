# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

notas = []

for i in range(1,4):
    while True:
        try:
            x = float(input(f'Digite a {i}ª nota: ').replace(',','.'))
            while x > 10 or x < 0:
                print('Nota Inválida.')
                x = float(input(f'Digite a {i}ª nota: ').replace(',','.'))
            notas.append(x)
        except ValueError:
            print('Nota Inválida.')
        else:
            break

media = sum(notas) / len(notas)

if media == 10:
    print('Média =', format(media,'.1f').replace('.',','))
    print('Aprovado com distinção!')
elif 10 > media >= 7:
    print('Média =', format(media,'.1f').replace('.',','))
    print('Aprovado.')
else:
    print('Média =', format(media,'.1f').replace('.',','))
    print('Reprovado')

        