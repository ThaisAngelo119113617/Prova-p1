def fibo(n):
    if (n ==1):
        resultado = 0
    elif(n == 2):
        resultado = 1
    else:
        resultado = fibo(n-1)+ fibo(n-2)
    return resultado


def main():
    n = int(input('entre com a posiçao do ultimo termo:'))

    print(fibo(n))



main()
