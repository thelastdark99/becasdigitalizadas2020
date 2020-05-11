
import requests,json,urllib3
from tabulate import tabulate

#DESACTIVAR LOS AVISOS POR SSL
urllib3.disable_warnings()
username="cisco"
password="cisco123!"
##################################################################################################################

#URL DONDE OBTENEMOS LA INFROMACION DEL SERVIDOR(API REQUEST)
URL1="https://192.168.1.202/restconf/data/ietf-interfaces:interfaces/interface/"
URL2="https://192.168.1.202/restconf/data/ietf-interfaces:interfaces-state/interface"
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

#SOLICITUDES
respuesta1=requests.get(URL1,auth=basicAuth,headers=headers,verify=False)
respuesta2=requests.get(URL2,auth=basicAuth,headers=headers,verify=False)
##################################################################################################################

#PARSEO A FORMATO JSON
outformat1=respuesta1.json()
outformat2=respuesta2.json()
##################################################################################################################

#FILTROS
interface=outformat1["ietf-interfaces:interface"] 
interface2=outformat2["ietf-interfaces:interface"]
##################################################################################################################

#OBTENEMOS INFORMACION ESPECIFICA Y CREAMOS UNA TABLA CON ESTA
datos=[]
Encabezado=["NOMBRE","IP","MASCARA","MAC"]

for e in range(len(interface and interface2)):
    name=interface[e]["name"]
    ip=interface[e]['ietf-ip:ipv4']["address"][0]["ip"]
    netmask=interface[e]['ietf-ip:ipv4']["address"][0]["netmask"]
    mac=interface2[e]["phys-address"]
    e=(name,ip,netmask,mac)
    datos.append(e)

print("\n",tabulate(datos,Encabezado,showindex=True))
##################################################################################################################