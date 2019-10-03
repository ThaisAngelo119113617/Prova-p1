#RESPOSTAS DA P1

#QUESTAO 1

def raizes(a , b , c):
    a = float(input('Entre com o valor do coeficiente a: '))
    b = float(input('Entre com o valor do coeficiente b: '))
    c = float(input('Entre com o valor do coeficiente c: '))
    delta = (b ** 2) - (4 * a * c)
    if (delta >= 0):
        resultado = 0
    else:
        resultado = 1
    return resultado
    
#QUESTAO 3

cont2 = 3
div = 3
cont = 1
a1 = 0
b1 = 0
while((1 / div) - (1 / (div -2))> (5 * (10**(-8)))):
    a = (1/ cont)
    cont+= 4
    a1 += a
    b= (1 / cont2)
    cont2+= 2
    b1 += b
pi = 4 * (a1 - b1)
print(pi)


#QUESTAO 4
def nob(n1 , n2):
    n1 = int(input('Entre com o primeiro valor: '))
    n2  = int(input('Entre com o segundo valor'))
    n11 = int(n1 / 10)
    n12 = int(n1 % 10)
    n21 = int(n2 / 10)
    n22 = int(n2 % 10)
    resposta = n11 + n12 + n21 + n22
    return resposta


def main():
    nob(n1 , n2)


main()





        





