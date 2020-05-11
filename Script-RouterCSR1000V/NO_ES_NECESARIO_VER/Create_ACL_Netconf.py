from ncclient import manager
import xml.dom.minidom

conexion=manager.connect(host="192.168.1.202",port=830,username="cisco",password="cisco123!",hostkey_verify=False)
while True:
    print("INFORMACION DE LA ACL A CREAR/MODIFICAR\n")
    clase=int(input("Que tipo de ACL deseas crear: \n1.-Standard\n2.-Extended\nSelecciona Opcion: "))
    Name=input("¿Como se va a llamar la ACL?(Puede ser tanto nombre como numero): ")
    Sec=input("Indica el numero de secuencia de la regla: ")
    Accion=input("Que accion desea realizar?(permit/deny): ")
    Protocol="0"#Para que no me indique un error debo de ubicarlo aqui para a posterior sobreescribirlo
    
    if clase==1:
        origen=int(input("Elige Origen:\n1.-Red,\n2.-Host,\n3.-Cualquiera\nOrigen: "))
        if origen == 1:
            Red=input("Red: ")
            Net=input("Wildcard: ")
            insert="""
            <std-ace>
                <ipv4-prefix>"""+Red+"""</ipv4-prefix>
                <mask>"""+Net+"""</mask>
            </std-ace>
            """

        if origen == 2:
            Red=input("Host: ")
            insert="""
            <std-ace>
                <ipv4-prefix>"""+Red+"""</ipv4-prefix>
            </std-ace>
            """
    
        if origen == 3:
            insert="""
            <std-ace>
                <any/>
            </std-ace>
            """
    if clase==2:
        origen=int(input("Elige Origen:\n1.-Red\n2.-Host\n3.-Cualquiera\nOrigen: "))
        Protocol=input("Por favor especifique el protocolo que desea usar(ip,icmp,tcp,udp): ")
        if origen == 1:
            Red=input("Red: ")
            Net=input("Wildcard: ")
            insert1="""
                <ipv4-address>"""+Red+"""</ipv4-address>
                <mask>"""+Net+"""</mask>
            """
            
        if origen == 2:
            Red=input("Host: ")
            insert1="""
                <host>"""+Red+"""</host>
            """
    
        if origen == 3:
            insert1="""
                <any/>
            """
        
        destino=int(input("Elige Destino:\n1.-Red\n2.-Host\n3.-Cualquiera\nDestino: "))
        if destino == 1:
            Red=input("Red Destino: ")
            Net=input("Wilcard Destino: ")
            insert2="""
                <dest-ipv4-address>"""+Red+"""</dest-ipv4-address>
                <dest-mask>"""+Net+"""</dest-mask>
            """
            
        if destino == 2:
            Red=input("Host Destino: ")
            insert2="""
                <dst-host>"""+Red+"""</dst-host>
            """
    
        if destino == 3:
            insert2="""
                <dst-any/>
            """
        insert=insert1+insert2
    
    filter_request1="""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <ip>
                <access-list>
                    <standard xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
                        <name>"""+Name+"""</name>
                        <access-list-seq-rule>
                            <sequence>"""+Sec+"""</sequence>
                            <"""+Accion+""">
                                """+insert+"""
                            </"""+Accion+""">
                        </access-list-seq-rule>
                    </standard>
                </access-list>
            </ip>
        </native>
    </config>
    """
    
    filter_request2="""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <ip>
                <access-list>
                    <extended xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
                        <name>"""+Name+"""</name>
                        <access-list-seq-rule>
                            <sequence>"""+Sec+"""</sequence>
                            <ace-rule>
                                <action>"""+Accion+"""</action>
                                <protocol>"""+Protocol+"""</protocol>
                                """+insert+"""
                            </ace-rule>
                        </access-list-seq-rule>
                    </extended>
                </access-list>
            </ip>
        </native>
    </config>
    """
    try:
        try:
            netconf_request=conexion.edit_config(target='running',config=filter_request1)
            try:
                print(conexion.operations.rpc.test_rpc_rpcerror())
            except:
                print("\n",xml.dom.minidom.parseString(netconf_request.xml).toprettyxml())
        except:
            netconf_request=conexion.edit_config(target='running',config=filter_request2)
            try:
                print(conexion.operations.rpc.test_rpc_rpcerror())
            except:
                print("\n",xml.dom.minidom.parseString(netconf_request.xml).toprettyxml())
        
        op=input("\n¿Desea volver a introducir alguna regla mas?(Y/N)")
        if op=="Y" or op=="y":
            continue
        elif op=="N" or op=="n":
            break
        else:
            print("Opcion indicada no existe")
            break
    except:
        print("No ha sido posible la creacion de la ACL")
        break

#print(conexion.operations.rpc.test_rpc_rpcerror())
#raise Exception(conexion.operations.rpc.test_rpc_rpcerror())