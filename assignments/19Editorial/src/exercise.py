def main():
    #escribe tu código abajo de esta línea
    import math
    palabras= int(input("Dame el número de palabras: "))
    
    paginas= math.ceil((palabras / 475))
    costo= (paginas*60)
    costoD= costo-(costo*0.1)
    
    print("El costo de la publicación es:", costoD)


if __name__ == '__main__':
    main()
