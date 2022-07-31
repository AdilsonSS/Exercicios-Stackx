'''Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.'''

n1 = int(input('Digite primeiro numero: '))
n2 = int(input('Dige o segundo numero: '))
while n2 == n1:
    print('Os números tem que ser diferentes')
    n2 = int(input('Dige o segundo numero: '))
n3 = int(input('Dige o terceiro numero: '))
while n3 == n2 or n3 == n1:
    print('Os números tem que ser diferentes')
    n3 = int(input('Dige o terceiro numero: '))
lista = [n1, n2, n3]
print('Números em ordem crescente: ', sorted(lista))

