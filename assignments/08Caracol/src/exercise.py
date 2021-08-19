def main():
    #escribe tu código abajo de esta línea
    minutos= float(input("Dame los minutos: "))
    mmsacms= (5.7*60) / 10
    centimetros= float(mmsacms * minutos)
    
    print("Centímentros recorridos:", centimetros)

if __name__ == '__main__':
    main()
