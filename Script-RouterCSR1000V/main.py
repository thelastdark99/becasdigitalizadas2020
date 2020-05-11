from tabulate import tabulate
from ncclient import manager
from Funciones import *
from Configurar_el_router import *
import time

Ip="192.168.1.202"#input("Indique la ip del router: ")
print("\nPor favor indique las credenciales de Login del router: \n")
Username="cisco"#input("Indique el nombre de Usuario: ")
Password="cisco123!"#input("Indique la Contraseña: ")

configure=input("¿Antes de empezar desea realizar la configuracion en el router para un optimo uso de los protocolos NETCONF/RESTCONF?(Y/N): ")
if configure == "Y" or configure=="y":
    configurar(Username, Password,Ip)
    print("\nConfiguracion realizada con exito\n")

conexion=manager.connect(host=Ip,port=830,username=Username,password=Password,hostkey_verify=False)

while True:
    protocol=int(input("\nPor favor indique el protocol que desea usar \n1.-NETCONF \n2.-RESTCONF \n3.-SALIR \nSeleccione Opcion: "))
    if protocol == 1:
        while True:
            
            opciones=[["1.-Obtener un Listado de las interfaces del router","2.-Crear Interfaces"],["3.-Borrar Interfaces","4.-Obtener la tabla de rutas(Red Destino)(Interfaz de salida)"],["5.-Crear ACL ","6.-Crear,Borrar,Mostrar Ruta OSPF "]]
            opcion=int(input("\nElige una de las siguientes opciones: \n\n"+tabulate(opciones)+"\n\nOpcion: "))
            
            if opcion==1:
                Get_Interfaces_Netconf(conexion)
                time.sleep(3)
                print("")
            elif opcion==2:
                Create_Interfaces_Netconf(conexion)
                time.sleep(3)
                print("")
            elif opcion==3:
                Delete_Interfaces_Netconf(conexion)
                time.sleep(3)
                print("")
            elif opcion==4:
                Get_Table_Routing_Netconf(conexion)
                time.sleep(3)
                print("")
            elif opcion==5:
                Create_ACL_Netconf(conexion)
                time.sleep(3)
                print("")
            elif opcion==6:
                Create_Delete_Show_OSPF_Netconf(conexion)
                time.sleep(3)
                print("")
            else:
                op=input("La opcion marcada no existe,¿Desea volver a intentarlo?")
                if op == "Y" or op == "y":
                    continue
                elif op == "N" or op == "n":
                    print("Adios")
                else:
                    print("Opcion marcada no existe")
            
            op=input("Desea seguir usando NETCONF?(Y/N): ")
            if op == "Y" or op == "y":
                continue
            elif op == "N" or op == "n":
                break
            
    elif protocol == 2:
        while True:
            opciones=[["1.-Obtener un Listado de las interfaces del router","2.-Crear Interfaces"],["3.-Borrar Interfaces","4.-Obtener la tabla de rutas(Red Destino)(Interfaz de salida)"],["5.-Crear ACL ","6.-Crear,Borrar,Mostrar Ruta OSPF"]]
            opcion=int(input("\nElige una de las siguientes opciones: \n\n"+tabulate(opciones)+"\n\nOpcion: "))
            
            if opcion==1:
                Get_Interfaces_Restconf(Ip,Username,Password)
                time.sleep(3)
                print("")
            elif opcion==2:
                Create_Interfaces_Restconf(Ip,Username,Password)
                time.sleep(3)
                print("")
            elif opcion==3:
                Delete_Interfaces_Restconf(Ip,Username,Password)
                time.sleep(3)
                print("")
            elif opcion==4:
                Get_Table_Routing_Restconf(Ip, Username, Password)
                time.sleep(3)
                print("")
            elif opcion==5:
                Create_ACL_Restconf(Ip, Username, Password)
                time.sleep(3)
                print("")
            elif opcion==6:
                Create_Delete_Show_OSPF_Restconf()
                time.sleep(3)
                print("")
            else:
                op=input("La opcion marcada no existe,¿Desea volver a intentarlo?")
                if op == "Y" or op == "y":
                    continue
                elif op == "N" or op == "n":
                    print("Adios")
                else:
                    print("Opcion marcada no existe")
            
            op=input("Desea seguir usando RESTCONF?(Y/N): ")
            if op == "Y" or op == "y":
                continue
            elif op == "N" or op == "n":
                break
    elif protocol==3:
        print("\nAdios")
        exit()
    else:
        op=input("La opcion marcada no existeee,¿Desea volver a intentarlo?(Y/N): ")
        if op == "Y" or op == "y":
            continue
        elif op == "N" or op == "n":
            print("Adios")
        else:
            print("Opcion marcada no existe")



        
        
        