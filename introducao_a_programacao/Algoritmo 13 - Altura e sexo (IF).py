'''Tendo como entrada a altura e o sexo (codificado da seguinte forma:
1: feminino 2: masculino) de uma pessoa, construa um programa que calcule e imprima seu peso ideal, utilizando as seguintes Fórmulas:

para homens: (72.7 * Altura) – 58
para mulheres: (62.1 * Altura) – 44.7'''

altura = float(input('Informe a altura: '))
sexo = int(input('Informe o sexo: 1 - feminino, 2 - masculino: '))
if sexo == 1:
    peso = (62.1 * altura) - 44.7
elif sexo == 2:
    peso = (72.7 *altura) - 58
print('Seu peso ideal é: ', peso)