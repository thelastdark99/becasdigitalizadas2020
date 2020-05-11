from ncclient import manager
import xml.dom.minidom,xmltodict,json
from tabulate import tabulate

username="cisco"
password="cisco123!"
conexion=manager.connect(host="192.168.1.202",port=830,username=username,password=password,hostkey_verify=False)
##################################################################################################################
while True:
    op=int(input("¿Que deseas hacer con las opciones OSPF?\n1.-Crear\n2.-Borrar\n3.-Mostrar\n4.-Salir\nOpcion: "))
    if op==1:
        while True:
            ID_ospf=input("ID de ruta ospf, cada id de ruta es una ruta con sus diferentes redes: ")
            ID_router=input("ID router, esta id debe de ser unica entre los vecinos que funcionen con ospf: ")
            Red=input("Red Destino: ")
            Wildcard=input("Wildcard: ")
            area=input("Indica el numero de area desde 0-99, con preferencia en el numero mas bajo: ")
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
            try:
                netconf_request=conexion.edit_config(target='running',config=filter_request)
                print(xml.dom.minidom.parseString(netconf_request.xml).toprettyxml())
            except:
                print("El ID del router ya existe en otra ruta ospf o ha ocurrido otro error desconocido")

            opci=input("\n¿Desea volver a crear una ruta/red(Recuerda para añadir redes a la misma ruta solo deves de indicar el mismo id?(Y/N): ")
            if opci=="Y" or opci=="y":
                continue
            if opci=="N" or opci=="n":
                break
        
    if op==2:
        while True:
            ID_ospf=input("ID de ruta ospf que desea borrar: ")
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
            try:
                netconf_request=conexion.edit_config(target='running',config=filter_request)
                print(xml.dom.minidom.parseString(netconf_request.xml).toprettyxml())
            except:
                print("\nLa ruta con el proceso/id indicado no esxiste")
            
            opci=input("\n¿Desea volver a borrar una ruta?(Y/N): ")
            if opci=="Y" or opci=="y":
                continue
            if opci=="N" or opci=="n":
                break
    
    if op==3:
        """
        No me funciona del todo bien porque me ha sido imposible poder hacerlo funcionar, si conseguia que funcionara con una ruta y varias
        redes dentro de esta luego no me funcionaba con varias rutas y varias redes o viceversa
        """
        
        filter_request="""
                <filter>
                    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                        <router>
                            <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf"/>
                        </router>
                    </native>
                </filter>
                """
        
        netconf_request=conexion.get(filter=filter_request)
        formatoxml1=xmltodict.parse(netconf_request.xml)
        filtro=formatoxml1['rpc-reply']['data']['native']['router']['ospf']
        print(filtro)
        
        try:
            network=filtro['network']
            try:
                redis=filtro['redistribute']['static']['redist-options']
            except:
                redis=None
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
        
        #OBTENEMOS INFORMACION ESPECIFICA
        datos1=[]
        
        Encabezado=["ID_OSPF","ID ROUTER","METRICA","RED","WILDCARD","AREA"]
        try:
            for e in range(len(filtro)):
                id_ospf=filtro["id"]
                id_router=filtro['router-id']
                metric=redis["metric-type"]
                try:
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
            for e in range(len(filtro)):
                id_ospf=filtro[e]["id"]
                id_router=filtro[e]['router-id']
                metric=redis2["metric-type"]
                try:
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
        print(tabulate(datos1,Encabezado))
    
    if op==4:
        print("Adios")
        break

