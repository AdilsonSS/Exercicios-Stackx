Salario = ValorPoupanca = RendaPoupanca = ValorFundoRendaFixa = RendaFundo = Meses = 0
RendaPoupanca = 1.02
RendaFundo = 1.05

Salario = float(input("Qual o salário: "))

ValorPoupanca = Salario * RendaPoupanca
print(ValorPoupanca)
Salario = Salario / 3
ValorFundoRendaFixa = Salario * RendaFundo
print(ValorFundoRendaFixa)

while True:
    Meses += 1
    print(f"O valor de investimentos do João é: , {ValorFundoRendaFixa:,.2f}, mês", Meses)
    if ValorFundoRendaFixa <= ValorPoupanca:
        ValorFundoRendaFixa = ValorFundoRendaFixa * RendaFundo
        continue
    else:
        break
