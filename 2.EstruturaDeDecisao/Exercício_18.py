# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def data(dd, mm, aaaa):

    if mm == 2:
        if aaaa % 4 != 0 and dd > 28:
            print('Data inválida')
        elif aaaa % 4 == 0 and dd > 29:
            print('Data inválida')
        else:
            mm = 'Fevereiro'
            print(dd, 'de', mm, 'de', aaaa)

    elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
        if dd > 30:
            print('Data inválida')
        else:
            if mm == 4:
                mm = 'Abril'            
            if mm == 6:
                mm = 'Junho'            
            if mm == 9:
                mm = 'Setembro'           
            if mm == 11:
                mm = 'Novembro'
            print(dd, 'de', mm, 'de', aaaa)

    else:
        if dd > 31 or mm > 12:
            print('Data inválida')
        else:
            if mm == 1:
                mm = 'Janeiro'
            if mm == 3:
                mm = 'Março'
            if mm == 5:
                mm = 'Maio'
            if mm == 7:
                mm = 'Julho'
            if mm == 8:
                mm = 'Agosto'
            if mm == 10:
                mm = 'Outubro'
            if mm == 12:
                mm = 'Dezembro'
            print(dd, 'de', mm, 'de', aaaa)

while True:
    try:
        d = int(input('Diagite o dia no formato DD: '))
    except ValueError:
        print('Dia incorreto.')
    else:
        while True:
            try:
                m = int(input('Diagite o mês no formato MM: '))
            except ValueError:
                print('Mês incorreto.')
            else:
                while True:
                    try:
                        a = int(input('Diagite o ano no formato AAAA: '))
                    except ValueError:
                        print('Ano incorreto.')
                    else:
                        break
                break
        break

data(d,m,a)