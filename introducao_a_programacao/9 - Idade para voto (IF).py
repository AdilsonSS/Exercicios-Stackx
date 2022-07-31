'''AnoNascimento = int(input('Digite o ano de nascimento'))
AnoAtual = 2022
idade = AnoAtual - AnoNascimento
if idade > 16:
    print('Você poderá votar esse ano')
else:
    print('Você NÃO poderá votar esse ano')
'''
import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
A = date.strftime("%Y")
print(f"ano atual: -> {year}")