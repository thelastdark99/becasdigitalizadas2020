from ncclient import manager
import xml.dom.minidom
conexion=manager.connect(host="192.168.1.202",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

#Usaremos una variable que luego introduciremos en la respuesta para que nos muestre solo lo que queremos
#En la variable del filtro debemos de usar las etiquetas config
#Si queremos cambiar las interfaces o crear una nueva usamos lo siguiente

while True:
    Number=int(input("Numero de interfaz: "))
    op=input("¿Le gustaria añadir una descricion a la interfaz?(Y/N): ")
    if op=="Y" or op=="y":
        Description=input("Descripcion: ")
    else:
        Description=None
    Ip=input("IP: ")
    Netmask=input("Netmask: ")
    
    
    filter_request="""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                    <Loopback>
                        <name>"""+str(Number)+"""</name>
                        <description>"""+str(Description)+"""</description>
                        <ip>
                            <address>
                                    <primary>
                                        <address>"""+Ip+"""</address>
                                        <mask>"""+Netmask+"""</mask>
                                    </primary>
                            </address>
                        </ip>
                    </Loopback>
            </interface>
        </native>
    </config>
    """
    netconf_request=conexion.edit_config(target='running',config=filter_request)
    print(xml.dom.minidom.parseString(netconf_request.xml).toprettyxml())
    
    op=input("¿Desea volver a añadir una interfaz nueva?(Y/N): ")
    if op=="Y" or op=="y":
        continue
    else:
        break
