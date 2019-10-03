def raizes():
    a = int(input('Entre com o valor do coeficiente a: '))
    b = int(input('Entre com o valor do coeficiente b: '))
    c = int(input('Entre com o valor do coeficiente c: '))
    delta = int((b ** 2 ) - (4 * a * c))
    print('Delta = ' , delta )
    x1 = ((b ** 2 ) + ((delta )**(1/2)))/ (2 * a)
    x2 = ((b ** 2 ) -((delta )**(1/2)))/ (2 * a)
    if(delta >= 0):
        print('As raizes sao: ' , x1, '  e ' ,  x2)
        print(' 0')
    elif(delta < 0):
        print('As raizes sao : ' , x1, ' e ', x2)
        print(' 1 ')


raizes()
