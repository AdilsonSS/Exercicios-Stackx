'''As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze.
Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.'''

quantidade = int(input('Quantas maçãs: '))

if quantidade < 12:
    print('O preço total é R$ ', quantidade * 0.30)
elif quantidade >= 12:
    print('O preço total é R$ ', quantidade * 0.25)
