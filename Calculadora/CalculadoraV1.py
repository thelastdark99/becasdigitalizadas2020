#NOTA: No he aplicado bucles porque decias que hasta la siguiente semana no lo aplicaramos,pero si he tenido que aplicar condicionaes ya que si no no se como se deveria de elgir una opcion en el menu
#USAR try: y exception: para los errorres
#USAR modulos para las operaciones,guardamos cada operacion en un modulo que importaremos
#Usar BREAK y Continue en los bucles
#Logicamente implementar funciones


print("CALCULADORA")
print("SELECCIONA UNA OPERACION: \n1 SUMAR \t 6 Numero Par/Impar \n2 RESTAR \t 7 Interes simple  \n3 DIVIDIR\t 8 IMC \n4 MULTIPLICAR\t 9 Sucesion Fibonacci \n5 X^Y   \t 10 % & Descuentos")
print("")
r=0
op=int(input("Por favor introduce una opcion(0 SALIR): "))

if op == 1:
    n1=float(input("Indica un numero: "))
    n2=float(input("Indica otro numero: "))
    print("El resultado de la suma es: ",n1+n2)
    exit()
if op == 2:
    n1=float(input("Indica un numero: "))
    n2=float(input("Indica otro numero: "))
    print("El resultado de la resta es: ",n1-n2)
    exit()
    
if op == 3:
    n1=float(input("Indica un numero: "))
    n2=float(input("Indica otro numero: "))
    c=n1/n2
    r=n1%n2
    print("El resultado de la division es: ",c," y su resto es: ",r)
    exit()
    
if op == 4:
    n1=float(input("Indica un numero: "))
    n2=float(input("Indica otro numero: "))
    print("El resultado de la multiplicacion es: ",n1*n2)
    exit()
    
if op == 5:
    n1=float(input("Indica una base: "))
    n2=float(input("Indica un exponente: "))
    if n2 == 2:
        print("El resultado de √",n1,"es:",n1**n2,sep=" ")
    elif n2 == 3:
        print("El resultado de",n1,"al cubo es:",n1**n2,sep=" ")
    exit()
        
if op == 6: 
    n1=int(input("Indica un numero: "))
    if n1 % 2 == 1:
        print("El",n1,"es impar",sep=" ")
    else:
        print("El",n1,"es par",sep=" ")
    exit()

if op == 7:
    ingreso=float(input("Indica un ingreso inicial en euros: "))
    iAnual=int(input("Introduce un interes anual: "))
    iAnualDeci=iAnual/100
    nAnos=int(input("Introduce la cantidad de años: "))
    Interes=float(ingreso*iAnualDeci*nAnos)
    print("El interes Simple calculado es: ",Interes,"€ anuales.",sep=" ")
    exit()
if op == 8:
    peso=int(input("Por favor indica tu peso: "))
    estatura=float(input("Por favor indica tu altura: "))
    imc=peso/(estatura**2)
    if imc <= 16.0:
        print("Su IMC 'Indice de Masa Corporal' es de: " + str(float(round(imc,2))) + " y se encuentra en la categoria 'Delgadez Severa:Bajo Peso'")
    elif imc >= 16.0 and imc <= 17.0:
        print("Su IMC 'Indice de Masa Corporal' es de: " + str(float(round(imc,2))) + " y se encuentra en la categoria 'Delgadez Moderada:Bajo Peso'")
    elif imc >= 17.0 and imc <=18.5:
        print("Su IMC 'Indice de Masa Corporal' es de: " + str(float(round(imc,2))) + " y se encuentra en la categoria 'Delgadez Leve:Bajo Peso'")
    elif imc >= 18.5 and imc <=24.9:
        print("Su IMC 'Indice de Masa Corporal' es de: " + str(float(round(imc,2))) + " y se encuentra en la categoria 'Peso normal:Peso normal'")
    elif imc >= 25.0 and imc <=29.9:
        print("Su IMC 'Indice de Masa Corporal' es de: " + str(float(round(imc,2))) + " y se encuentra en la categoria 'Pre-Obeso:Sobrepeso'")
    elif imc >= 30.0 and imc <=34.9:
        print("Su IMC 'Indice de Masa Corporal' es de: " + str(float(round(imc,2))) + " y se encuentra en la categoria 'Obesidad Tipo I:Obesidad'")
    elif imc >= 35.0 and imc <=39.9:
        print("Su IMC 'Indice de Masa Corporal' es de: " + str(float(round(imc,2))) + " y se encuentra en la categoria 'Obesidad Tipo II:Obesidad'")
    else:
        print("Su IMC 'Indice de Masa Corporal' es de: " + str(float(round(imc,2))) + " y se encuentra en la categoria 'Obesidad Tipo III:Obesidad'")
    exit()
if op == 9:
    #En la version 2 añadire con un bucle la impresion de la sucesion de fibonaci mientras,solo muestra el numero que le precede en la sucesion
    n1=int(input("Indica un numero: "))
    def fibo(n1):
        if n1 == 0:
            return 0
        else:
            if n1 == 1:
                return 1
            else:
                return fibo(n1-2)+fibo(n1-1)
    print(fibo(n1))
    exit()
    
if op == 10:
    print("Elige una operacion de porcentaje: \n1 Calular la cantidad, a partir de un porcentaje sobre una total")
    print("2 Calular el total, a partir de la cantidad elegida y el porcentaje que representa sobre el total")
    print("3 Calcular el porcentaje que representa una cantidad respecto al total")
    opp=int(input("Elige una opcion: "))
    if opp==1:
        p=float(input("Introduce el %: "))
        t=float(input("Introduce el total: "))
        c=(t/100)*70
        print("La cantidad obtenida de un porcentaje",p,"% sobre un total",t,"es:",c,sep=" ")
    elif opp==2:
        c=float(input("Introduce la cantidad: "))
        p=float(input("Introduce el %: "))
        t=(c*100)/p
        print("El total obtenido de una cantidad",c,"sobre un porcentaje",p,"% es:",t,sep=" ")
    elif opp==3:
        c=float(input("Introduce la cantidad: "))
        t=float(input("Introduce el total: "))
        p=(c*100)/t
        print("El porcentaje obtenido de una cantidad",c,"sobre un total",t,"es:",p,"%",sep=" ")
    else:
        print("La opcion marcada no existe por favor introduzca otra opcion diferenteee")
    exit()
    
if op == 0:
    print("Gracias por usar la calculadora de Ivan Praena. Adios :)")
else:
    print("La opcion marcada no existe por favor introduzca otra opcion diferente")

    