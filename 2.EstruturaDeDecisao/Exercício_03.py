# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

x = input('Digite o Sexo: ').upper()
while x != 'F' and x != 'M':
    print('Sexo Inválido')
    x = input('Digite o Sexo: ').upper()
if x == 'F':
    print('F - Feminino')
else:
    print('M - Masculino')
    