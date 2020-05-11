from ncclient import manager
from tabulate import tabulate
import xml.dom.minidom,xmltodict,json
#N me funciona del todo bien porque me ha sido imposible poder hacerlo funcionar, si conseguia que funcionara con una ruta y varias
#redes dentro de esta luego no me funcionaba con varias rutas y varias redes o viceversa
username="cisco"
password="cisco123!"

conexion=manager.connect(host="192.168.1.202",port=830,username=username,password=password,hostkey_verify=False)

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