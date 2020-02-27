#NOTA: No he aplicado bucles porque decias que hasta la siguiente semana no lo aplicaramos,pero si he tenido que aplicar condicionaes ya que si no no se como se deveria de elgir una opcion en el menu
print("CALCULADORA")
print("SELECCIONA UNA OPERACION: \n1 SUMAR \t        8 M.C.M \t       \n2 RESTAR \t        9 M.C.D \n3 DIVIDIR \t        10 Interes simple \n4 MULTIPLICAR \t        11 IMC \n5 X^Y \t                12 Sucesion Fibonacci \n6 Numero Par/Impar \t13 MEDIA ARITMETICA \n7 Primo o Compuesto \t14 Descuento")
print("")

op=int(input("Por favor introduce una opcion(0 SALIR): "))

if op == 1:
    n1=float(input("Indica un numero: "))
    n2=float(input("Indica otro numero: "))
    print("El resultado de la suma es: ",n1+n2)

if op == 2:
    n1=float(input("Indica un numero: "))
    n2=float(input("Indica otro numero: "))
    print("El resultado de la resta es: ",n1-n2)
    
if op == 3:
    n1=float(input("Indica un numero: "))
    n2=float(input("Indica otro numero: "))
    c=n1/n2
    r=n1%n2
    print("El resultado de la division es: ",c," y su resto es: ",r)
    
if op == 4:
    n1=float(input("Indica un numero: "))
    n2=float(input("Indica otro numero: "))
    print("El resultado de la multiplicacion es: ",n1*n2)
    
if op == 5:
    n1=float(input("Indica una base: "))
    n2=float(input("Indica un exponente: "))
    if n2 == 2:
        print("El resultado de",n1,"al cuadrado es: ",n1**n2,sep=" ")
    elif n2 == 3:
        print("El resultado de",n1,"al cubo es: ",n1**n2,sep=" ")
        
if op == 6: 
    n1=int(input("Indica un numero: "))
    if n1 % 2 == 1:
        print("El numero",n1,"es impar",sep=" ")
    else:
        print("El numero",n1,"es par",sep=" ")
        
if op == 7: 
    n1=float(input("Indica un numero: "))
    contador=0
    for i in range(1,100):
        if(n1%i==0):
            contador+=1
    if (contador>2):
        print("Es compuesto")
    else:
        print("Es primo")
    
if op == 8:
    print("Hola")
   #import mcd
   #def MCM(n1,n2):
    #return (n1*n2/MCD(n1,n2))
    
if op == 9:
     n1=float(input("Indica un numero: "))
     print("El resultado de la suma es: ",n1**3)
     while(n1 != n2):
        if(n1>n2):
            n1 -= n2
        else:
            n2 -= n1
     print(n1)
if op == 10:
    ingreso=float(input("Indica un ingreso inicial en euros: "))
    iAnual=int(input("Introduce un interes anual: "))
    iAnualDeci=iAnual/100
    nAnos=int(input("Introduce la cantidad de años: "))
    Interes=float(ingreso*iAnualDeci*nAnos)
    print("El interes Simple calculado es: ",Interes,"€ anuales.",sep=" ")
if op == 11:
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
if op == 12:
    n1=float(input("Indica un numero: "))
    print("El resultado de la suma es: ",n1**3)
if op == 13:
    n1=float(input("Indica un numero: "))
    print("El resultado de la suma es: ",n1**3)
if op == 14:
    n1=float(input("Indica un numero: "))
    print("El resultado de la suma es: ",n1**3)
    
    
    ingreso=float(input("Indica un ingreso inicial en euros: "))
iAnual=int(input("Introduce un interes anual: "))
iAnualDeci=iAnual/100
nAnos=int(input("Introduce la cantidad de años: "))
Interes=float(ingreso*iAnualDeci*nAnos)
print("El interes Simple calculado es: ",Interes,"€ anuales.",sep=" ")
    
if op == 0:
    print("Gracias por usar la calculadora de Ivan Praena. Adios :)")

    