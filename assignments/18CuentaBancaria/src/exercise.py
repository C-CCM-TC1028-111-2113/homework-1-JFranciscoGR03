def main():
    #escribe tu código abajo de esta línea
    saldoanterior= float(input("Dame el saldo del mes anterior: "))
    ingresos= float(input("Dame los ingresos: "))
    egresos= float(input("Dame los egresos: "))
    cheques= int(input("Dame el número de cheques: "))
    
    porcentaje_interes= 7.5
    saldo= (saldoAnterior+ingresos-egresos)-(cheques*13)
    interes= saldo * (porcentaje_interes/100)
    saldoFinal= saldo-interes
               
    print("El saldo final de la cuenta es:", saldoFinal)

if __name__ == '__main__':
    main()
