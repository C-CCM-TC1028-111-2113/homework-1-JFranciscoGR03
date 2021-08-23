def main():
    #escribe tu código abajo de esta línea
    num= int(input("Dame un número: "))
    lista= list(str(num))
    dig= (int(i) for i in lista)
    pares= 0
    
    for num in dig:
        if num%2== 0:
            pares+=1
        else:
            pares+=0

    print("El número de dígitos pares es:", pares)


if __name__ == '__main__':
    main()
