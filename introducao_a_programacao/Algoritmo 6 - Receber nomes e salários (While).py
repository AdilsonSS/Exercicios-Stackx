"""Faça um programa que receba o salário de um funcionário chamado Carlos.
Sabe-se que outro funcionário, João, tem salário equivalente a um terço do salário de Carlos.
Carlos aplicará seu salário integralmente na caderneta de poupança, que rende 2% ao mês,
e João aplicará seu salário integralmente no fundo de renda fixa, que rende 5% ao mês.
O programa deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencente a Carlos."""


SalarioCarlos = float(input('Digite o salario do Carlos: '))
SalarioJoao = SalarioCarlos / 3
Poupanca = 0.02
Rendafixa = 0.05
Mes = 0
while (SalarioJoao <SalarioCarlos):
    SalarioCarlos = SalarioCarlos + (SalarioCarlos * Poupanca)
    SalarioJoao = SalarioJoao + (SalarioJoao * Rendafixa)
    Mes = (Mes + 1)
    print('Salario do Joao: {:.2f}'.format(SalarioJoao))
    print('Salario do Carlos: {:.2f}'.format(SalarioCarlos))
    print('Quantidade de meses: ', Mes)
