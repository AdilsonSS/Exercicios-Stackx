imposto =0.07
SalarioBruto = float(input('Digite o salario bruto:'))

if SalarioBruto <=350:
    SalarioLiquido = SalarioBruto - (SalarioBruto * imposto) + 100
    print('O salário liquido é: ', SalarioLiquido)
elif SalarioBruto >350 and SalarioBruto <=600:
    SalarioLiquido = SalarioBruto - (SalarioBruto * imposto) + 75
    print('O salário liquido é: ', SalarioLiquido)
elif SalarioBruto >600 and SalarioBruto <=900:
    SalarioLiquido = SalarioBruto - (SalarioBruto * imposto) + 50
    print('O salário liquido é: ', SalarioLiquido)
else:
    SalarioLiquido = SalarioBruto - (SalarioBruto * imposto) + 35
    print('O salário liquido é: ', SalarioLiquido)