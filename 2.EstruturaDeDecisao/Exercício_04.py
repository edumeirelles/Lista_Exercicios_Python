# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

x = input('Digite uma letra: ').upper()
alfabeto = ['A','Á','À','Â','Ã','B','C','D','E','É','È','Ê','D','F','G','H','I','Í','Ì','Î','J','K','L','M','N','O','Ó','Ò','Ô','Õ','P','Q','R','S','T','U','Ú','Ù','Û','V','W','X','Y','Z']
while len(x) > 1 or len(x) == 0 or x not in alfabeto :
    print('Letra Inválida.')
    x = input('Digite uma letra: ').upper()

if x in 'AÁÀÃÂEÉÈÊIÍÌÎOÓÒÔÕUÚÙÛ':
    print(f'A letra {x} é uma vogal.')
else:
    print(f'A letra {x} é uma consoante.')