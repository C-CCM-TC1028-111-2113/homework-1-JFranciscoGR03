def main():
    #escribe tu código abajo de esta línea
    numero= int(input("Dame un número: "))
    pares= 0

    while(numero>0):
        if numero%2== 0:
            pares+=1
        else:
            pares+=0
        numero= numero//10

    print("El número de digitos pares es:", pares)


if __name__ == '__main__':
    main()
