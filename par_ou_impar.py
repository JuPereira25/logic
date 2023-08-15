"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    
    integer_number = int(input('Enter an integer: '))

    if integer_number % 2 == 0:
        print(f'the number {integer_number} its pair')
    else:
        print(f'the number {integer_number} is odd')

except ValueError: #Usar quando não for possivel converter um valor do tipo que está sendo solicitado.
    print('The value entered is not an integer')
