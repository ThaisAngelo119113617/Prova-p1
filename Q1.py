def raizes():
    
    a = int(input('Entre com o valor do coeficiente a: '))
    
    b = int(input('Entre com o valor do coeficiente b: '))
    
    c = int(input('Entre com o valor do coeficiente c: '))
    
    delta = ((b ** 2 ) - (4 * a * c))
    
    print('Delta = ' , delta )
    
    if( delta >= 0 ):
 
        x1 = (( -b ) + ((delta )**(1/2)))/ (2 * a)
        
        x2 = (( -b ) -((delta )**(1/2)))/ (2 * a)
        
        print('As raizes sao: ' , x1, '  e ' ,  x2)
        
        print(' 0 ')
    
    elif( delta < 0 ):
        
        x1i = ((( -b ) + ((delta )**(1/2))) * i) / (2 * a) 

        x2i = ((( -b ) - ((delta )**(1/2))) * i) / (2 * a)

        print('As raizes sao : ' , x1i , ' e ', x2i )
        
        print(' 1 ')


raizes()
