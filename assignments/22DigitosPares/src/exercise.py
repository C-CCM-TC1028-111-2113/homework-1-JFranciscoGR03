def main():
    #escribe tu código abajo de esta línea
    numero= int(input("Dame un número: "))
    even_num= 0
    odd_num= 0

    while(numero>0):
        if numero%2== 0:
            even_num+1
        numero= numero//10

    print("El número de digitos pares es:", even_num)


if __name__ == '__main__':
    main()
