# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []

while True:
    try:
        n1 = float(input('Digite a nota do 1º bimestre: ').replace(',','.'))
        while n1 > 10 or n1 < 0:
            print('Nota inválida.')
            n1 = float(input('Digite a nota do 1º bimestre: ').replace(',','.'))
        notas.append(n1)
    except ValueError:
        print('Nota inválida.') 
    else:
        while True:
            try:
                n2 = float(input('Digite a nota do 2º bimestre: ').replace(',','.'))
                while n2 > 10 or n2 < 0:
                    print('Nota inválida.')
                    n2 = float(input('Digite a nota do 2º bimestre: ').replace(',','.'))
                notas.append(n2)
            except ValueError:
                print('Nota inválida.')
            else:
                while True:
                    try:
                        n3 = float(input('Digite a nota do 3º bimestre: ').replace(',','.'))
                        while n3 > 10 or n3 < 0:
                            print('Nota inválida.')
                            n3 = float(input('Digite a nota do 3º bimestre: ').replace(',','.'))
                        notas.append(n3)
                    except ValueError:
                        print('Nota inválida.')
                    else:
                        while True:
                            try:
                                n4 = float(input('Digite a nota do 4º bimestre: ').replace(',','.'))
                                while n4 > 10 or n4 < 0:
                                    print('Nota inválida.')
                                    n4 = float(input('Digite a nota do 4º bimestre: ').replace(',','.'))
                                notas.append(n4)
                                media = sum(notas) / len(notas)
                                print('Média =', format(media,'.1f').replace('.',','))
                            except ValueError:
                                print('Nota inválida.')
                            else:
                                break
                        break
                break
        break
