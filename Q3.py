#QUESTA 3 P1
soma = 1
pi = 0
i = 1
sinal = 1
while (soma > (5 * (10 ** (-8)))):
    pi1= pi
    pi = pi + 4/(i * sinal)
    i += 2
    sinal  =sinal * (-1)
    soma = (pi1 - pi) * sinal

print('Soma = ' , soma)
print('pi = ' , pi)


