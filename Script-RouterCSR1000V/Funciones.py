from ncclient import manager
import xmltodict,xml.dom.minidom,requests,json,urllib3
from tabulate import tabulate
#DESACTIVAR LOS AVISOS POR SSL
urllib3.disable_warnings()

def Get_Interfaces_Netconf(conexion):
    #CONEXION
    #conexion=manager.connect(host="192.168.1.202",port=830,username="cisco",password="cisco123!",hostkey_verify=False)
    ##################################################################################################################

    #FILTROS
    filter1_reply="""
    <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
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
    ##################################################################################################################

    #OBTENEMOS INFORMACION ESPECIFICA
    datos=[]
    Encabezado=["NOMBRE","IP","MASCARA","MAC"]

    for e in range(len(interface and interface2)):
        name=formatojson2["rpc-reply"]["data"]["interfaces-state"]["interface"][e]["name"]
        ip=formatojson["rpc-reply"]["data"]["interfaces"]["interface"][e]["ipv4"]["address"]["ip"]
        netmask=formatojson["rpc-reply"]["data"]["interfaces"]["interface"][e]["ipv4"]["address"]["netmask"]
        mac=formatojson2["rpc-reply"]["data"]["interfaces-state"]["interface"][e]["phys-address"]
        e=(name,ip,netmask,mac)
        datos.append(e)

    return print(tabulate(datos,Encabezado,showindex=True))
    ##################################################################################################################

def Get_Interfaces_Restconf(ip,username,password):

    #URL DONDE OBTENEMOS LA INFROMACION DEL SERVIDOR(API REQUEST)
    URL1="https://"+ip+"/restconf/data/ietf-interfaces:interfaces/interface/"
    URL2="https://"+ip+"/restconf/data/ietf-interfaces:interfaces-state/interface"

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
    solicitud1=requests.get(URL1,auth=basicAuth,headers=headers,verify=False)
    solicitud2=requests.get(URL2,auth=basicAuth,headers=headers,verify=False)
    ##################################################################################################################
    
    if (solicitud1.status_code>=200 and solicitud1.status_code<=399) and (solicitud2.status_code>=200 and solicitud2.status_code<=399):
            print("Codigo de respuesta: \nSolicitud1:",solicitud1.status_code,"\Solicitud2: ",solicitud2.status_code,".\nLos datos se han modificado con exito")
    else:
        print("Codigo de respuesta: \nSolicitud1:",solicitud1.status_code,"\Solicitud2: ",solicitud2.status_code,".\nLos datos NO se han podido modificar")

    #PARSEO A FORMATO JSON
    outformat1=solicitud1.json()
    outformat2=solicitud2.json()
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

def Create_Interfaces_Netconf(conexion):
    while True:
        #VARIABLES PARA CREAR LA INTERFAZ
        Number=int(input("Numero de interfaz: "))
        op=input("¿Le gustaria añadir una descricion a la interfaz?(Y/N): ")
        if op=="Y" or op=="y":
            Description=input("Descripcion: ")
        else:
            Description=None
        Ip=input("IP: ")
        Netmask=input("Netmask: ")
        ##################################################################################################################

        #FILTRO
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
        ##################################################################################################################

        #SOLICITUD
        netconf_request=conexion.edit_config(target='running',config=filter_request)
        ##################################################################################################################

        #MOSTRAR MENSAJE DE ESTADO DE CONSULTA RPC
        print(xml.dom.minidom.parseString(netconf_request.xml).toprettyxml())
        ##################################################################################################################

        #OPCION ADICIONAL
        op=input("¿Desea volver a añadir una interfaz nueva?(Y/N): ")
        if op=="Y" or op=="y":
            continue
        else:
            break
        ##################################################################################################################

def Create_Interfaces_Restconf(ip,username,password):
    while True:
        ##################################################################################################################

        #DATOS QUE VAMOS A CREAR/MODIFICAR
        print("INFORMACION DE LA INTERFAZ A CREAR/MODIFICAR\n")
        Numero=int(input("introduce el numero de la interfaz que desea crear/modificar: "))
        IpInt=input("Indicar direccion IP de la interfaz: ")
        Netmask=input("Indicar segmento de red de la interfaz: ")

        ##################################################################################################################

        #URL DONDE OBTENEMOS LA INFROMACION DEL SERVIDOR(API REQUEST)
        URL="https://"+ip+"/restconf/data/ietf-interfaces:interfaces/interface=Loopback"+str(Numero)
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
                            "ip": IpInt,
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

def Delete_Interfaces_Netconf(conexion):
    while True:
        Number=int(input("Numero de interfaz que se desea borrar: "))
        ###################################################################################################################
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
        ###################################################################################################################
        netconf_request=conexion.edit_config(target='running',config=filter_request)
        print(xml.dom.minidom.parseString(netconf_request.xml).toprettyxml())
        print("Interfaz borrada con exito")

        op=input("\n¿Desea volver a borrar una interfaz nueva?(Y/N): ")
        if op=="Y" or op=="y":
            continue
        else:
            break

def Delete_Interfaces_Restconf(ip,username,password):
    while True:
        interfaz=int(input("Indica el numero de interfaz que desea borrar: "))

        URL="https://"+ip+"/restconf/data/ietf-interfaces:interfaces/interface=Loopback"+str(interfaz)
        basicAuth=(username,password)

        respuesta=requests.delete(URL,auth=basicAuth,verify=False)

        if respuesta.status_code>=200 and respuesta.status_code<=399:
            print("Codigo de respuesta: ",respuesta.status_code,". Los datos se han borrado con exito")
        else:
            print("Codigo de respuesta: ",respuesta.status_code,". Los datos NO se han podido borrar")

        op=input("\n¿Desea volver a eliminar una interfaz?(Y/N): ")
        if op=="Y" or op=="y":
            continue
        break


def Get_Table_Routing_Netconf(conexion):
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
    
    print("\n",tabulate(datos,Encabezado,showindex=True))
    ##################################################################################################################

def Get_Table_Routing_Restconf(ip,username,password):

    #URL
    URL="https://"+ip+"/restconf/data/ietf-routing:routing-state"
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
        Destino=interface[n]["destination-prefix"]
        InterfaceS=interface[n]["next-hop"]["outgoing-interface"]
        n+=2
        l=(Destino,InterfaceS)
        datos.append(l)
    
    print("\n",tabulate(datos,Encabezado,showindex=True))
    ##################################################################################################################

def Create_ACL_Netconf(conexion): 
    while True:
        ##################################################################################################################
        
        #INDICAR EL TIPO DE CLASE DE ACL
        clase=int(input("Que tipo de ACL deseas crear: \n1.-Standard\n2.-Extended\nSelecciona Opcion: "))
        ##################################################################################################################
        
        #PARAMETROS COMUNES
        Name=input("¿Como se va a llamar la ACL?(Puede ser tanto nombre como numero): ")
        sec=input("Indica el numero de secuencia de la regla: ")
        Accion=input("Que accion desea realizar?(permit/deny): ")
        Protocol="0"#Para que no me indique un error debo de ubicarlo aqui para a posterior sobreescribirlo
        ##################################################################################################################
        
        #LA CLASE 1 ES STANDARD, FUNCIONA CON LA FUENTE DE ORIGEN
        if clase==1:
            #DEFINIMOS LA FUENTE DE ORIGEN
            origen=int(input("Elige Origen:\n1.-Red\n2.-Host\n3.-Cualquiera\nOrigen: "))
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
        ##################################################################################################################
        
        #LA CLASE 2 ES EXTENDED, FUNCIONA CON FUENTES TANTO DE ORIGEN COMO DE DESTINO
        if clase==2:
            #DEFINIMOS LA FUENTE DE ORIGEN
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
            #DEFINIMOS LA FUENTE DE DESTINO
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
        ##################################################################################################################
        
        #DEFINIMOS LOS FILTROS
        filter_request1="""
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <ip>
                    <access-list>
                        <standard xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
                            <name>"""+Name+"""</name>
                            <access-list-seq-rule>
                                <sequence>"""+sec+"""</sequence>
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
                                <sequence>"""+sec+"""</sequence>
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
        ##################################################################################################################
        
        #INTENTOS Y PRUEBA DE ERRORES
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
        ##################################################################################################################
        
        #OPCIONALES
            op=input("\n¿Desea volver a introducir alguna regla mas?(Y/N)")
            if op=="Y" or op=="y":
                continue
            elif op=="N" or op=="n":
                break
            else:
                print("Opcion indicada no existe")
                break
        ##################################################################################################################
        except:
            print("No ha sido posible la creacion de la ACL")
            break

def Create_ACL_Restconf(ip,username,password):
    ##################################################################################################################
    while True:
        #INDICAR EL TIPO DE LA CLASE DE ACL
        clase=int(input("Que tipo de ACL deseas crear: \n1.-Standard\n2.-Extended\n3.-Salir\nSelecciona Opcion: "))
        ##################################################################################################################
        if clase==3:
            print("Adios")
            break
        
        #PARAMETROS COMUNES 
        Name=input("¿Como se va a llamar la ACL?(Puede ser tanto nombre como numero): ")
        Sec=int(input("Indica el numero de secuencia de la regla: "))
        Accion=input("Que accion desea realizar?(permit/deny): ")
        ##################################################################################################################
        
        #URL QUE USAREMOS
        URL="https://"+ip+"/restconf/data/native/ip/access-list/"
        ##################################################################################################################
    
        #LA CLASE 1 ES STANDARD, FUNCIONA CON LA FUENTE DE ORIGEN
        if clase==1:
            #DEFINIMOS LA FUENTE DE ORIGEN
            origen=int(input("Elige Origen:\n1.-Red\n2.-Host\n3.-Cualquiera\nOrigen: "))
            if origen == 1:
                Red=input("Red: ")
                Net=input("Wildcard: ")
                insert1={
                    'ipv4-prefix': Red,
                    'mask': Net}
        
            if origen == 2:
                Red=input("Host: ")
                insert1={
                    'host': Red}
        
            if origen == 3:
                insert1={
                    'any': [None]}
        
        ##################################################################################################################
        
        #LA CLASE 2 ES EXTENDED, FUNCIONA CON FUENTES TANTO DE ORIGEN COMO DE DESTINO
        if clase==2:
            #DEFINIMOS LA FUENTE DE ORIGEN
            origen=int(input("Elige Origen:\n1.-Red\n2.-Host\n3.-Cualquiera\nOrigen: "))
            Protocol=input("Por favor especifique el protocolo que desea usar(ip,icmp,tcp,udp): ")
            if origen == 1:
                Red=input("Red: ")
                Net=input("Wildcard: ")
                insert1={
                    'action': Accion, 
                    'protocol': Protocol,
                    'ipv4-address': Red,
                    'mask': Net}
                
            if origen == 2:
                Red=input("Host: ")
                insert1={
                    'action': Accion, 
                    'protocol': Protocol,
                    'host': Red}
        
            if origen == 3:
                insert1={
                    'action': Accion, 
                    'protocol': Protocol,
                    'any': [None]}
            
            #DEFINIMOS LA FUENTE DE DESTINO
            destino=int(input("Elige Destino:\n1.-Red\n2.-Host\n3.-Cualquiera\nDestino: "))
            if destino == 1:
                Red=input("Red Destino: ")
                Net=input("Wilcard Destino: ")
                insert2={
                    "dest-ipv4-address":Red,
                    "dest-mask":Net}
                
            if destino == 2:
                Red=input("Host Destino: ")
                insert2={
                    "dst-host":Red
                    }
        
            if destino == 3:
                insert2={
                    'dst-any': [None]}
                
            insert1.update(insert2)
        ##################################################################################################################
        
        
        #DEFINIMOS LOS FILTROS
        headers={
            "Content-Type":"application/yang-data+json",
            "Accept":"application/yang-data+json"
            }
        
        
        body_Config={
            'Cisco-IOS-XE-acl:standard': [{
                'name': Name, 
                'access-list-seq-rule': [{
                    'sequence': Sec, Accion: {
                        'std-ace': insert1}}]}]}
        
        body_Config2={
            'Cisco-IOS-XE-acl:extended': [{
                'name': Name, 
                'access-list-seq-rule': [{
                    'sequence': Sec, 'ace-rule': insert1}]}]}
        ##################################################################################################################
        
        #CREDENCIALES
        basicAuth=(username,password)
        ##################################################################################################################
        
        #SOLICITUDES Y PRUEBAS DE ERRORES
        solicitud=requests.post(URL,auth=basicAuth,data=json.dumps(body_Config),headers=headers,verify=False)
        if solicitud.status_code==400:
            solicitud=requests.post(URL,auth=basicAuth,data=json.dumps(body_Config2),headers=headers,verify=False)
            
        if solicitud.status_code>=200 and solicitud.status_code<=399:
            print("Codigo de respuesta: \nSolicitud:",solicitud.status_code,"\nLos datos se han modificado con exito")
        else:
            if solicitud.status_code>=409:
                print("Codigo de respuesta: \nSolicitud:",solicitud.status_code,".\nLos datos NO se han podido modificar porque estan duplicados")
            else:
                print("Codigo de respuesta: \nSolicitud:",solicitud.status_code,".\nLos datos NO se han podido modificar")
        ##################################################################################################################
        
        #OPCIONALES PARA PODER SEGUIR CREANDO REGLAS EN LA MISMA ACL CREADA
        op=int(input("¿Desea añadir una nueva regla a la ACL creada o prefiere una nueva ACL?\n1.-Nueva Regla\n2.-Nueva ACL\n3.-Salir\nOpcion: "))
        if op==1:
            if clase==1:
                while True:
                    URL="https://192.168.1.202/restconf/data/native/ip/access-list/standard="+Name
                    Sec=int(input("Indica el numero de secuencia de la regla: "))
                    Accion=input("Que accion desea realizar?(permit/deny): ")
                    origen=int(input("Elige Origen:\n1.-Red\n2.-Host\n3.-Cualquiera\nOrigen: "))
                    if origen == 1:
                        Red=input("Red: ")
                        Net=input("Wildcard: ")
                        insert1={
                            'ipv4-prefix': Red,
                            'mask': Net}
        
                    if origen == 2:
                        Red=input("Host: ")
                        insert1={
                            'host': Red}
                
                    if origen == 3:
                        insert1={
                            'any': [None]}
                    
                    body_Config_seq={
                        'access-list-seq-rule': [{
                            'sequence': Sec, Accion: {
                                'std-ace': insert1}}]}
                        
                    solicitud=requests.post(URL,auth=basicAuth,data=json.dumps(body_Config_seq),headers=headers,verify=False)
                    if solicitud.status_code>=200 and solicitud.status_code<=399:
                        print("Codigo de respuesta: \nSolicitud:",solicitud.status_code,"\nLos datos se han modificado con exito")
                    else:
                        if solicitud.status_code>=409:
                            print("Codigo de respuesta: \nSolicitud:",solicitud.status_code,".\nLos datos NO se han podido modificar porque estan duplicados")
                        else:
                            print("Codigo de respuesta: \nSolicitud:",solicitud.status_code,".\nLos datos NO se han podido modificar")
                    
                    op=input("¿Desea añadir una nueva regla mas?(Y/N): ")
                    if op=="Y" or op=="y":
                        continue
                    else:
                        break
            if clase==2:
                while True:
                    URL="https://192.168.1.202/restconf/data/native/ip/access-list/extended="+Name
                    Sec=int(input("Indica el numero de secuencia de la regla: "))
                    Accion=input("Que accion desea realizar?(permit/deny): ")
                    Protocol=input("Por favor especifique el protocolo que desea usar(ip,icmp,tcp,udp): ")
                    origen=int(input("Elige Origen:\n1.-Red\n2.-Host\n3.-Cualquiera\nOrigen: "))
                    if origen == 1:
                        Red=input("Red: ")
                        Net=input("Wildcard: ")
                        insert1={
                            'action': Accion, 
                            'protocol': Protocol,
                            'ipv4-address': Red,
                            'mask': Net}
                        
                    if origen == 2:
                        Red=input("Host: ")
                        insert1={
                            'action': Accion, 
                            'protocol': Protocol,
                            'host': Red}
                
                    if origen == 3:
                        insert1={
                            'action': Accion, 
                            'protocol': Protocol,
                            'any': [None]}
                    
                    destino=int(input("Elige Destino:\n1.-Red\n2.-Host\n3.-Cualquiera\nDestino: "))
                    if destino == 1:
                        Red=input("Red Destino: ")
                        Net=input("Wilcard Destino: ")
                        insert2={
                            "dest-ipv4-address":Red,
                            "dest-mask":Net}
                        
                    if destino == 2:
                        Red=input("Host Destino: ")
                        insert2={
                            "dst-host":Red
                            }
                
                    if destino == 3:
                        insert2={
                            'dst-any': [None]}
                    
                    insert1.update(insert2)
                    
                    body_Config_seq={
                        'access-list-seq-rule': [{
                            'sequence': Sec, 'ace-rule': insert1}]}
                    
                    solicitud=requests.post(URL,auth=basicAuth,data=json.dumps(body_Config_seq),headers=headers,verify=False)
                    if solicitud.status_code>=200 and solicitud.status_code<=399:
                        print("Codigo de respuesta: \nSolicitud:",solicitud.status_code,"\nLos datos se han modificado con exito")
                    else:
                        if solicitud.status_code>=409:
                            print("Codigo de respuesta: \nSolicitud:",solicitud.status_code,".\nLos datos NO se han podido modificar porque estan duplicados")
                        else:
                            print("Codigo de respuesta: \nSolicitud:",solicitud.status_code,".\nLos datos NO se han podido modificar")
                    
                    op=input("¿Desea añadir una nueva regla mas?(Y/N): ")
                    if op=="Y" or op=="y":
                        continue
                    else:
                        break
                
        if op==2:
            continue
        if op==3:
            break

def Create_Delete_Show_OSPF_Netconf(conexion):
    while True:
        op=int(input("¿Que deseas hacer con las opciones OSPF?\n1.-Crear\n2.-Borrar\n3.-Mostrar\n4.-Salir\nOpcion: "))
        if op==1:
            while True:
                ##################################################################################################################
                
                #VARIABLES COMUNES
                ID_ospf=input("ID de ruta ospf, cada id de ruta es una ruta con sus diferentes redes: ")
                ID_router=input("ID router, esta id debe de ser unica entre los vecinos que funcionen con ospf(ejem:0.0.0.2): ")
                Red=input("Red Destino: ")
                Wildcard=input("Wildcard: ")
                area=input("Indica el numero de area desde 0-99, con preferencia en el numero mas bajo: ")
                ##################################################################################################################
                
                #FILTRO
                filter_request="""
                        <config>
                            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                                    <router>
                                        <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                                            <id>"""+ID_ospf+"""</id>
                                            <router-id>"""+ID_router+"""</router-id>
                                            <redistribute>
                                                <static>
                                                    <redist-options>
                                                        <metric-type>1</metric-type>
                                                        <subnets/>
                                                    </redist-options>
                                                </static>
                                            </redistribute>
                                            <network>
                                                <ip>"""+Red+"""</ip>
                                                <mask>"""+Wildcard+"""</mask>
                                                <area>"""+area+"""</area>
                                            </network>
                                        </ospf>
                                    </router>
                                </native>
                        </config>
                        """
                ##################################################################################################################
                
                #SOLICITUD Y PRUEBA DE FALLO
                try:
                    netconf_request=conexion.edit_config(target='running',config=filter_request)
                    print(xml.dom.minidom.parseString(netconf_request.xml).toprettyxml())
                except:
                    print("El ID del router ya existe en otra ruta ospf o ha ocurrido otro error desconocido")
                
                ##################################################################################################################
                
                #OPCIONAL
                opci=input("\n¿Desea volver a crear una ruta/red(Recuerda para añadir redes a la misma ruta solo deves de indicar el mismo id?(Y/N): ")
                if opci=="Y" or opci=="y":
                    continue
                if opci=="N" or opci=="n":
                    break
            
        if op==2:
            while True:
                ##################################################################################################################
                
                #BORRAR UNA RUTA ESPECIFICA
                #ID DE RUTA
                ID_ospf=input("ID de ruta ospf que desea borrar: ")
                ##################################################################################################################
                
                #FILTRO
                filter_request="""
                    <config>
                        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                                <router>
                                    <ospf operation="delete" xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                                        <id>"""+ID_ospf+"""</id>
                                    </ospf>
                                </router>
                            </native>
                    </config>
                    """
                ##################################################################################################################
                
                #SOLICITUD
                try:
                    netconf_request=conexion.edit_config(target='running',config=filter_request)
                    print(xml.dom.minidom.parseString(netconf_request.xml).toprettyxml())
                except:
                    print("\nLa ruta con el proceso/id indicado no esxiste")
                
                ##################################################################################################################
                
                #OPCIONAL
                opci=input("\n¿Desea volver a borrar una ruta?(Y/N): ")
                if opci=="Y" or opci=="y":
                    continue
                if opci=="N" or opci=="n":
                    break
        
        if op==3:
            ##################################################################################################################
            return print("""
            No me funciona del todo bien porque me ha sido imposible poder hacerlo funcionar, si conseguia que funcionara con una ruta y varias
            redes dentro de esta luego no me funcionaba con varias rutas y varias redes o viceversa. De Todas formas dejo el codigo para que le heches un vistazo
            """)
            ##################################################################################################################
            
            #FILTRO
            filter_request="""
                    <filter>
                        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                            <router>
                                <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf"/>
                            </router>
                        </native>
                    </filter>
                    """
            ##################################################################################################################
            
            #SOLICITUD
            netconf_request=conexion.get(filter=filter_request)
            ##################################################################################################################
            
            #PARSEAMOS A DICCIONARIO YA QUE JSON NO FUNCIONABA
            formatoxml1=xmltodict.parse(netconf_request.xml)
            ##################################################################################################################
            
            #FILTRAMOS MAS ESPECIFICAMENTE
            filtro=formatoxml1['rpc-reply']['data']['native']['router']['ospf']
            
            #INTENTO DE CUANDO SOLO ES UNA REGLA
            try:
                network=filtro['network']
                try:
                    redis=filtro['redistribute']['static']['redist-options']
                except:
                    redis=None
            #INTENTO DE CUANDO HAY VARIAS REGLAS
            except:
                for e in range(len(filtro)):
                    network_multi=filtro[e]['network']
                try:
                    try:
                        for e in range(len(filtro)):
                            redis2=filtro[e]['redistribute']['static']['redist-options']
                    except:
                        for e in range(len(filtro)):
                            e=+1
                            redis2=filtro[e]['redistribute']['static']['redist-options']
                            
                except:
                    redis2=None
            
            #LISTA DONDE GUARDA DATOS
            datos1=[]
            
            Encabezado=["ID_OSPF","ID ROUTER","METRICA","RED","WILDCARD","AREA"]
            try:
                #OBTENEMOS LA INFIORMACION DE UNA UNICA RUTA
                ##################################################################################################################
                for e in range(len(filtro)):
                    id_ospf=filtro["id"]
                    id_router=filtro['router-id']
                    metric=redis["metric-type"]
                    try:
                        #SI DISPONEMOS DE UNA SOLA RED EN LA REGLA O DE VARIAS
                        for n in range(len(network)):
                            red=network['ip']
                            wildcard=network['mask']
                            area=network['area']
                            e=(id_ospf,id_router,metric,red,wildcard,area)
                            datos1.append(e) 
                    except:
                        for n in range(len(network_multi)):
                            red=network_multi[n]['ip']
                            wildcard=network_multi[n]['mask']
                            area=network_multi[n]['area']
                            e=(id_ospf,id_router,metric,red,wildcard,area)
                            datos1.append(e) 
                    #e=(id_ospf,id_router,metric,red,wildcard,area)
                    #datos1.append(e)    
            
            except:
                ##################################################################################################################
                #OBTENEMOS LA INFORMACION DE VARIAS RUTAS
                for e in range(len(filtro)):
                    id_ospf=filtro[e]["id"]
                    id_router=filtro[e]['router-id']
                    metric=redis2["metric-type"]
                    try:
                        #SI DISPONEMOS DE UNA SOLA RED O VARIAS
                        for n in range(len(network_multi)):
                            red=network_multi[n]['ip']
                            wildcard=network_multi[n]['mask']
                            area=network_multi[n]['area']
                            e=(id_ospf,id_router,metric,red,wildcard,area)
                            datos1.append(e)       
                    
                    except:
                        for n in range(len(network)):
                            red=network['ip']
                            wildcard=network['mask']
                            area=network['area']
                            e=(id_ospf,id_router,metric,red,wildcard,area)
                            datos1.append(e) 
                    #e=(id_ospf,id_router,metric,red,wildcard,area)
                    #e+=l
                    #datos1.append(e)
                    ##################################################################################################################
            print(tabulate(datos1,Encabezado))
        
        if op==4:
            print("Adios")
            break
def Create_Delete_Show_OSPF_Restconf():
    print("Lo siento,pero no he podido terminar este ultimo por falta de tiempo")
