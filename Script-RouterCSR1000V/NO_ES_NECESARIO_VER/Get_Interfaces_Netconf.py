from ncclient import manager
import json,xmltodict
from tabulate import tabulate

#CONEXION
conexion=manager.connect(host="192.168.1.202",port=830,username="cisco",password="cisco123!",hostkey_verify=False)
##################################################################################################################

#FILTROS
filter1_reply="""
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        <name></name>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip></ip>
                    <netmask></netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</filter>
"""

filter2_reply="""
<filter>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name></name>
            <phys-address></phys-address>
        </interface>
    </interfaces-state>
</filter>
"""

##################################################################################################################

#CONSULTAS
netconf_reply1=conexion.get_config(source="running",filter=filter1_reply)
netconf_reply2=conexion.get(filter=filter2_reply)
##################################################################################################################

#CONVERTIMOS A XML
formatoxml1=xmltodict.parse(netconf_reply1.xml)
formatoxml2=xmltodict.parse(netconf_reply2.xml)
##################################################################################################################

#CONVERTIMOS A FORMATO JSON Y DICCIONARIO
formatojson=eval(json.dumps(formatoxml1))
formatojson2=eval(json.dumps(formatoxml2))
##################################################################################################################

#FILTRAMOS LA INFORMACION DEL DICCIONARIO
interface=formatojson["rpc-reply"]["data"]["interfaces"]["interface"]
interface2=formatojson2["rpc-reply"]["data"]["interfaces-state"]["interface"]

#OBTENEMOS INFORMACION ESPECIFICA
datos=[]
Encabezado=["NOMBRE","IP","MASCARA","MAC"]

for e in range(len(interface and interface2)):
    name=formatojson["rpc-reply"]["data"]["interfaces"]["interface"][e]["name"]
    ip=formatojson["rpc-reply"]["data"]["interfaces"]["interface"][e]["ipv4"]["address"]["ip"]
    netmask=formatojson["rpc-reply"]["data"]["interfaces"]["interface"][e]["ipv4"]["address"]["netmask"]
    mac=formatojson2["rpc-reply"]["data"]["interfaces-state"]["interface"][e]["phys-address"]
    e=(name,ip,netmask,mac)
    datos.append(e)

print(tabulate(datos,Encabezado,showindex=True))
##################################################################################################################
