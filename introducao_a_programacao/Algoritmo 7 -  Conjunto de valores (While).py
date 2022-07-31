import math
num = int(input('Digite um numero: '))
#quadrado, cubo, raiz = float

while num > 0:
    print('Quadrado: ', (num * num))
    print('Raiz quadrada: ', math.sqrt(num))
    print('Cubo: ', (num**3))
    num = int(input('Digite um numero qualquer ou zero para sair: '))

