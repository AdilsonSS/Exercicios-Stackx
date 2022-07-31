

Laco1 = 1
Laco2 = True
Laco3 = True

while Laco1 <=10:
    # Quadro do laço principal
    SalarioMinimo = 450
    SalarioInicial = 0
    SalarioFinal = 0
    AuxilioAlimentacao = 0


    Codigo = input('Digite o código funcionário: ')
    HoraTrabalhada = float(input('Digite as horas trabalhadas: '))

    #--------------------Categoria G ou O
    while Laco2:
        Categoria = input('Digite a categoria: ')
        if Categoria == 'O' or Categoria == 'G':
            Laco2 = False
        else:
            print('As caegorias possíveis são O e G. Digite novamente...')
            continue
        break
    # --------------------Turno
    while Laco3:
        Turno = input('Digite o Turno: ')
        if Turno == 'M' or Turno == 'V' or Turno =='N':
            Laco3 = False
        else:
            print('Os turnos possíveis são: V ou M ou N. Digite novamente...')
            continue
        break
    # ----------Condicional para categoria G e turno N
    if Categoria == 'G' and Turno == 'N':
        ValorHora = SalarioMinimo * 0.18
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    # ----------Condicional para categoria G e Turno M ou V
    if Categoria == 'G' and Turno == 'M' or Turno == 'V':
        ValorHora = SalarioMinimo * 0.15
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    # ----------Condicional para categoria O e Turno N
    if Categoria == 'O' and Turno == 'N':
        ValorHora = SalarioMinimo * 0.13
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    # ----------Condicional para categoria O e Turno M ou V
    if Categoria =='O' and Turno == 'M' or Turno == 'V':
        ValorHora = SalarioMinimo * 0.10
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    # --------Quadro Resumo
    print("Codigo:", Codigo, "Horas Trabalhadas: ", HoraTrabalhada, "Categoria: ", Categoria, "Turno: ", Turno)
    print("Valor da hora:", ValorHora, "Salario Inicial: ", SalarioInicial, "Auxilio Alimentação: ", AuxilioAlimentacao, "Salário Final: ", SalarioFinal)

    print('numero laço principal: ', Laco1)
    Laco1 = Laco1 + 1
    Laco2 = True
    Laco3 = True
print('Fim')



