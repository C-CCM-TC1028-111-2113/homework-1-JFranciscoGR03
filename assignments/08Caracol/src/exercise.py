def main():
    #escribe tu código abajo de esta línea
    minutos= float(input("Dame los minutos: "))
    centimetros= (((5.7*60) /10) * minutos)
    final= round(centimetros,1)
    
    print("Centímentros recorridos:", final)

if __name__ == '__main__':
    main()
