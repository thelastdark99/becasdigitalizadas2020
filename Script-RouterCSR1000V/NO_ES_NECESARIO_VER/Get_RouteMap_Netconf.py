from ncclient import manager
import json,xmltodict
from tabulate import tabulate


#CONEXION
conexion=manager.connect(host="192.168.1.202",port=830,username="cisco",password="cisco123!",hostkey_verify=False)
##################################################################################################################

#FILTROS
filter1_reply="""
<filter>
    <routing-state xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
        <routing-instance>
            <ribs>
                <rib>
                    <routes>
                        <route>
                        </route>
                    </routes>
                </rib>
            </ribs>
        </routing-instance>
    </routing-state>
</filter>
"""


##################################################################################################################

#CONSULTAS
netconf_reply1=conexion.get(filter=filter1_reply)
#netconf_reply2=conexion.get(filter=filter2_reply)
##################################################################################################################

#CONVERTIMOS A XML
formatoxml1=xmltodict.parse(netconf_reply1.xml)
##################################################################################################################

#CONVERTIMOS A FORMATO JSON Y DICCIONARIO
formatojson=eval(json.dumps(formatoxml1))
##################################################################################################################

#FILTRAMOS LA INFORMACION DEL DICCIONARIO
interface=formatojson["rpc-reply"]["data"]["routing-state"]["routing-instance"]["ribs"]["rib"]["routes"]["route"]
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
