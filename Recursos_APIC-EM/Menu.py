##############################################################################################################################
#Modulos importados y Funciones importadas

import requests,urllib3,time,json
from tabulate import *
from os import system
from Curso_de_Programacion_De_Redes.Funcionalidadades.Post import *
from Curso_de_Programacion_De_Redes.Funcionalidadades.Get import *

##############################################################################################################################
#Login para crear un Ticket
print("Necesito un Login: ")
username=input("Usuario: ")#"devnetuser"
password="Xj3BDqbU"#input("Contraseña: ")#"Xj3BDqbU"
ticket=Ticket(username,password)

#############################################################################################################################################################################################
#Menu que se mostrara repetidamente para usar los recursos APIC-EM
while True:
    #Mostrando l menu usando el metodo Tabulate
    Encabezado=["IVENTORY","INVENTORY/GEOLOCATION","FLOW ANALYSIS","IP GEOLOCATION","FILE"]
    Opciones=[["1.-Obtener Un Listado De Hosts","4.-Crear Una Localizacion","8.-Analisis De Flujo","9.-Geolocalizacion","10.-Obtener Nombres De Espacios"],["2.-Obtener Dispositivos De Red","5.-Actualizar Datos De Una Localizacion","","","11.-Crear Nombre de Espacio/Subir Ficheros"],["3.-Obtener Informacion De Una Interfaz","6.-Borrar Una Localizacion","","","12.-Obtener Ficheros"],["","7.-Obtener Datos De Una Localizacion","","","13.-Actualizar Ficheros"],[" "," "," "," ","14.-Borrar Ficheros"],[" "," "," "," ","15.-Mostrar Contenido de Ficheros"]]
    print("\n                                                                                   RECURSOS APIC-EM\n\n",tabulate(Opciones,Encabezado))

    opcion=int(input("\nElige una opcion: "))
    
    if opcion == 1:
        resultado=Get_Host(ticket)
        time.sleep(1)
        system("cls")
        
    elif opcion == 2:
        resultado=Get_Device_Network(ticket)
        time.sleep(1)
        system("cls")
    
    elif opcion == 3:
        resultado=Get_Interfaces_Info(ticket)
        time.sleep(1)
        system("cls")
    
    elif opcion == 4:
        resultado=Location(ticket)
        time.sleep(1)
        system("cls")
    
    elif opcion == 5:
        resultado=Update_Location(ticket)
        time.sleep(1)
        system("cls")
    
    elif opcion == 6:
        resultado=Delete_Location(ticket)
        time.sleep(1)
        system("cls")

    elif opcion == 7:
        resultado=Get_Location(ticket)
        time.sleep(1)
        system("cls")
    
    elif opcion == 8:
        flowAnalysisId=Flow_Id(ticket)
        resultado=Flow_Device(ticket,flowAnalysisId)
        time.sleep(1)
        system("cls") 
    
    elif opcion == 9:
        resultado=Get_Geo(ticket)
        time.sleep(1)
        system("cls")
    
    elif opcion == 10:
        resultado=Get_NameSpace(ticket)
        time.sleep(1)
        system("cls")
    
    elif opcion == 11:
        resultado=New_NS_and_File(ticket)
        time.sleep(1)
        system("cls")
    
    elif opcion == 12:
        resultado=Get_FileNS(ticket)
        time.sleep(1)
        system("cls")
    
    elif opcion == 13:
        resultado=Update_NS_and_File(ticket)
        time.sleep(1)
        system("cls")
    
    elif opcion == 14:
        resultado=Delete_NS_and_File(ticket)
        time.sleep(1)
        system("cls")
        
    elif opcion == 15:
        resultado=Show_File(ticket)
        time.sleep(1)
        system("cls")
    
    else:
        print("OPCION INTRODUCIDA ERRONEA\nPor favor vuelve a introducir una opcion valida:)")
        time.sleep(2)
        continue
#############################################################################################################################################################################################
