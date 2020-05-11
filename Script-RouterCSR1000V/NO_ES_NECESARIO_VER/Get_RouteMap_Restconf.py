import json,requests,urllib3
from tabulate import tabulate
urllib3.disable_warnings()

username="cisco"
password="cisco123!"
#URL
URL="https://192.168.1.202/restconf/data/ietf-routing:routing-state"
##################################################################################################################

#CABEZERA DE CONSULTA
headers={
    "Content-Type":"application/yang-data+json",
    "Accept":"application/yang-data+json"
    }
##################################################################################################################
#CREDENCIALES
basicAuth=(username,password)
##################################################################################################################

#SOLICITUD
solicitud1=requests.get(URL,auth=basicAuth,headers=headers,verify=False)
#netconf_reply2=conexion.get(filter=filter2_reply)
##################################################################################################################

#PARSEO A FORMATO JSON
outformat1=solicitud1.json()
##################################################################################################################

#FILTRAMOS LA INFORMACION DEL DICCIONARIO
interface=outformat1["ietf-routing:routing-state"]["routing-instance"][0]["ribs"]["rib"][0]["routes"]["route"]
##################################################################################################################

#OBTENEMOS INFORMACION ESPECIFICA
datos=[]
Encabezado=["RED DESTINO","INTERFAZ SALIDA"]

long=len(interface)
n=0
while n != long:
    Destino=interface[n]["destination-prefix"]#["rpc-reply"]["data"]["routing-state"]["routing-instance"]["ribs"]["rib"]["routes"]["route"]
    InterfaceS=interface[n]["next-hop"]["outgoing-interface"]#["rpc-reply"]["data"]["routing-state"]["routing-instance"]["ribs"]["rib"]["routes"]["route"]
    n+=2
    l=(Destino,InterfaceS)
    datos.append(l)

print(tabulate(datos,Encabezado,showindex=True))
##################################################################################################################

    