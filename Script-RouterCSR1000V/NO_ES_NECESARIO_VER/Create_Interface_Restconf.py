import requests,json,urllib3
from tabulate import tabulate

#DESACTIVAR LOS AVISOS POR SSL
urllib3.disable_warnings()
username="cisco"
password="cisco123!"
##################################################################################################################


while True:
    ##################################################################################################################
    
    #DATOS QUE VAMOS A CREAR/MODIFICAR
    print("INFORMACION DE LA INTERFAZ A CREAR/MODIFICAR\n")
    Numero=int(input("introduce el numero de la interfaz que desea crear/modificar: "))
    Ip=input("Indicar direccion IP de la interfaz: ")
    Netmask=input("Indicar segmento de red de la interfaz: ")
    
    ##################################################################################################################
    
    #URL DONDE OBTENEMOS LA INFROMACION DEL SERVIDOR(API REQUEST)
    URL="https://192.168.1.202/restconf/data/ietf-interfaces:interfaces/interface=Loopback"+str(Numero)
    ##################################################################################################################
    
    #CABEZERA Y CUERPO DE CONSULTA
    headers={
        "Content-Type":"application/yang-data+json",
        "Accept":"application/yang-data+json"
        }
    
    body_Config={
        "ietf-interfaces:interface": {
            "name": "Loopback"+str(Numero),
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": Ip,
                        "netmask": Netmask
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    }
    
    ##################################################################################################################
    
    #CREDENCIALES
    basicAuth=(username,password)
    ##################################################################################################################
    
    #SOLICITUD
    solicitud=requests.put(URL,auth=basicAuth,headers=headers,data=json.dumps(body_Config),verify=False)
    ##################################################################################################################
    
    #RESPUESTA
    if solicitud.status_code>=200 and solicitud.status_code<=399:
        print("Codigo de respuesta: ",solicitud.status_code,". Los datos se han modificado con exito")
    else:
        print("Codigo de respuesta: ",solicitud.status_code,". Los datos NO se han podido modificar")

    #OPCIONAL VOLVER A REALIZAR LA FUNCION
    op=input("\n¿Desea volver a crear o modificar una interfaz?(Y/N): ")
    if op=="Y" or op=="y":
        continue
    if op=="N" or op=="n":
        break
        
    ###################################################################################################################


