from ncclient import manager
import xml.dom.minidom
conexion=manager.connect(host="192.168.1.202",port=830,username="cisco",password="cisco123!",hostkey_verify=False)

while True:
    Number=int(input("Numero de interfaz que se desea borrar: "))
    
    filter_request="""
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface>
                        <Loopback operation="delete">
                            <name>"""+str(Number)+"""</name>
                        </Loopback>
                </interface>
            </native>
        </config>
        """
    
    netconf_request=conexion.edit_config(target='running',config=filter_request)
    print(xml.dom.minidom.parseString(netconf_request.xml).toprettyxml())
    print("Interfaz borrada con exito")
    
    op=input("\n¿Desea volver a añadir una interfaz nueva?(Y/N): ")
    if op=="Y" or op=="y":
        continue
    else:
        break
    
    
    