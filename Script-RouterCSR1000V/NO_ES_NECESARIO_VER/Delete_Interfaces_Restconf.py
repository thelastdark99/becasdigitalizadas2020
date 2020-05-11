#Importamos los modulos para realizar consultas http (request) y el modulo para convertirlo a formato json(json)
import requests,urllib3
#Quitamos las advertencias SSL
urllib3.disable_warnings()

while True:
    interfaz=int(input("Indica el numero de interfaz que desea borrar: "))
    
    URL="https://192.168.1.202/restconf/data/ietf-interfaces:interfaces/interface=Loopback"+str(interfaz)
    basicAuth=("cisco","cisco123!")
    
    respuesta=requests.delete(URL,auth=basicAuth,verify=False)
    
    op=input("¿Desea volver a eliminar una interfaz?(Y/N): ")
    if op=="Y" or op=="y":
        continue
    if op=="N" or op=="n":
        if respuesta.status_code>=200 and respuesta.status_code<=399:
            print("Codigo de respuesta: ",respuesta.status_code,". Los datos se han borrado con exito")
        else:
            print("Codigo de respuesta: ",respuesta.status_code,". Los datos NO se han podido borrar")