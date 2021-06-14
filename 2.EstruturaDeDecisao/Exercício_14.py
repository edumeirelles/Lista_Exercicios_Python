# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E

# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

notas = []
conceitos = ['A','B','C','D','E']

for i in range(1,3):
    while True:
        try:
            n = float(input(f'Digite a {i}ª nota: ').replace(',','.'))
            while n > 10 or n < 0:
                print('Nota inválida.')
                n = float(input(f'Digite a {i}ª nota: ').replace(',','.'))
            notas.append(n)
                
        except ValueError:
            print('Nota inválida.')
        else:
            break

media = sum(notas)/len(notas)
print('Média:', format(media,'.1f').replace('.',','))
if media >= 9:
    conceito = conceitos[0]
    print(f'Conceito {conceito}')
elif 9 > media >= 7.5:
    conceito = conceitos[1]
    print(f'Conceito {conceito}')
elif 7.5 > media >= 6:
    conceito = conceitos[2]
    print(f'Conceito {conceito}')
elif 6 > media >= 4:
    conceito = conceitos[3]
    print(f'Conceito {conceito}')
else:
    conceito = conceitos[4]
    print(f'Conceito {conceito}')

if conceito in 'ABC':
    print('Aluno APROVADO')
else:
    print('Aluno REPROVADO')