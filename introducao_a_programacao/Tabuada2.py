num = int(input('Digite um numero: '))
print('TABUADA MULTIPLICAÇÃO DE ', num)
print('-' * 12)
for x in range(10):
    # print(s)
    # print(x)
    s = num * (x + 1)
    # print(num, '+ ', x, ' = ', s )

    print('{} X {:2} = {:2}'.format(num, (x + 1), s))
print('-' * 12)
