# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []

for i in range(1,5):
    while True:
        try:
            x = float(input(f'Digite a nota do {i}º bimestre: ').replace(',','.'))
            while x > 10 or x < 0:
                print('Nota inválida.')
                x = float(input(f'Digite a nota do {i}º bimestre: ').replace(',','.'))
            notas.append(x)      
        except ValueError:
            print('Nota inválida.') 
        else:
            break

media = sum(notas) / len(notas)
print('Média =', format(media,'.1f').replace('.',','))
