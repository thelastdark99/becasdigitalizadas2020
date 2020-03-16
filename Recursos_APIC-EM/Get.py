import requests,json,time,urllib3
from tabulate import *

urllib3.disable_warnings()

def Get_Host(ticket):
    try:
        Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
        headers={
            "Content-Type":"application/json",
            "X-Auth-Token":ticket
            }
    
        respuesta=requests.get(Url,headers=headers,verify=False)
        outFormat=respuesta.json()
        
        resq=outFormat["response"]
        Host_list=[]
        Host=[]
        Encabezado=["Numero","IP","MAC","Tipo","Conectado a ID","Conectado a IP","Conectado a MAC","Conectado a Nombre","VLAN_ID","Ult.Update","Origen","Punto Presencia","Punto Apego","Sub Tipo","ID"]
    
        for e in resq:
            Host.append(e.values())
        for v in Host:
            Host_list.append(v)
        
        return print("\nEstos son los Host Disponibles: \n\n",tabulate(Host_list,Encabezado,showindex=True))
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")
def Get_Device_Network(ticket):
    try:
        Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
        headers={
            "Content-Type":"application/json",
            "X-Auth-Token":ticket
            }
    
        respuesta=requests.get(Url,headers=headers,verify=False)
        outFormat=respuesta.json()
    
        Device_list=[]
        Encabezado=["Number","Family","  SerialNumber  ","  Type  ","MAC","IP","CountInterface"]
        c=0
    
        for key in outFormat['response']:
            network=[c,key['family'],key['serialNumber'],key['type'],key['macAddress'],key['managementIpAddress'],key['interfaceCount']]
            c+=1
            Device_list.append(network)
        return print("\nEstos son los dispositivos de red disponibles: \n\n",tabulate(Device_list,Encabezado))
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")

  
def Get_Interfaces_Info(ticket):
    try:
        IP=input("Introduce la IP de la interfaz para obtener informacion: ")
        Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/interface/ip-address/"+IP
        
        headers={
                "Content-Type":"application/json",
                "X-Auth-Token":ticket
                }
    
        respuesta=requests.get(Url,headers=headers,verify=False)
        outFormat=respuesta.json()
        
        Encabezado=["Descripcion","Estado","Tipo","Clase","Velocidad Max","Estado Admin","MAC","Index","Nombre Puerto","PID","Serie","ID Vlan","ID Dispositivo","duplex","Modo Puerto","Tipo Puerto","Ult.Update","Vlan Voz","IP","Mascara","Soporte Isis","Mapeado Fisico ID","Mapeado Fisico Nombre","Tipo Medio","ID Vlan Nativa","Soporte OSPF","Numero Serie","Uuid","ID"]
        resq=outFormat["response"][0]
        interfaces=[]
        i=[]
        
        for e in resq:
            i.append(resq.get(e))
        interfaces.append(i)
        
        return print("\nEsta es la informacion de la interfaz: \n\n",tabulate(interfaces,Encabezado))
    except:
        return print("No existen datos de la interfaz del dispositivo con IP: ",IP)


def Get_Location(Ticket):
    try:
        headers={
                "Content-Type":"application/json",
                "X-Auth-Token":Ticket
                }
        while True:
            op=input("\n¿Desea obtener datos de alguna localizacion en especifico?(Y/N): ")
            if op == "Y" or op =="y":
                while True:
                    op=int(input("\nComo deseas obtener los datos de la localizacion \n1.-ID de la localizacion\n2.-Nombre de la Localizacion\nElige una opcion: "))
    
                    if op == 1:
                        while True:
                            Tid=input("Dime el ID exacto de la localizacion: ")
                            Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location/"+str(Tid)
        
                            respuesta=requests.get(Url,headers=headers,verify=False)
                            outFormat=respuesta.json()
                            
                            if respuesta.status_code==400 or respuesta.status_code==404:
                                print("No existe el ID de localizacion: ", Tid)
                                op=input("¿Deseas volver a intentarlo?(Y/N): ")
                                if op == "Y" or op=="y": 
                                    continue
                                if op == "N" or op=="n": 
                                    return print("Adios")
                                else:
                                    return print("Opcion marcada incorrecta")
                            
                            list_loc=[]
                            l=[]
                            Encabezado=["Direccion","Direccion Geografica","Descripcion","Nombre","ID"]
                            Encabezado2=["Direccion","Direccion Geografica","Nombre","ID"]
                            
                            dic=outFormat["response"]
                            
                            for v in dic:
                                l.append(dic.get(v))
                            list_loc.append(l)
                            
                            if not dic.get("description"):   
                                resultado=tabulate(list_loc,Encabezado2)
                            else:
                                return print("\nEstos son los datos de la localizacion indicada por ID: \n\n",tabulate(list_loc,Encabezado))
    
                    elif op == 2:
                        while True:
                            nombre=input("\nDime el nombre exacto de la localizacion: ")
                            Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location/location-name/"+str(nombre)
        
                            respuesta=requests.get(Url,headers=headers,verify=False)
                            outFormat=respuesta.json()
                            
                            if respuesta.status_code==404:
                                print("\nNo existe el Nombre de localizacion: ", nombre)
                                op=input("¿Deseas volver a intentarlo?(Y/N): ")
                                if op == "Y" or op=="y": 
                                    continue
                                if op == "N" or op=="n": 
                                    return print("Adios")
                                else:
                                    return print("Opcion marcada incorrecta")
        
                            list_loc=[]
                            l=[]
                            Encabezado=["Direccion","Direccion Geografica","Descripcion","Nombre","ID"]
                            Encabezado2=["Direccion","Direccion Geografica","Nombre","ID"]
                            
                            dic=outFormat["response"]
                            
                            for v in dic:
                                l.append(dic.get(v))
                            list_loc.append(l)
                            
                            if not dic.get("description"):   
                                return print("\nEstos son los datos de la localizacion indicada: \n\n",tabulate(list_loc,Encabezado2))
                            else:
                                return print("\nEstos son los datos de la localizacion indicada: \n\n",tabulate(list_loc,Encabezado))
        
                    else:
                        print("Opcion marcada erronea, vuelva a intertarlo")
                        continue
    
            if op == "N" or op=="n":
                Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location/"
    
                respuesta=requests.get(Url,headers=headers,verify=False)
                outFormat=respuesta.json()
    
                list_loc=[]
                Encabezado=["Number","Direccion","Direccion Geografica","Descripcion","Nombre","ID"]
                count=0
                for ele in outFormat["response"]:
                    count+=1
                    e=(count,
                       ele.get("civicAddress"),
                       ele.get("geographicalAddress"),
                       ele.get("description"),
                       ele["locationName"],
                       ele["id"]
                       )
                    list_loc.append(e)
                return print("\nEstas son todas las localizaciones: \n\n",tabulate(list_loc,Encabezado))
            else:
                print("OPCION MARCADA INCORRECTA, intentelo de nuevo")
                continue
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")

def Flow_Device(ticket,flowAnalysisId):
    try:
        url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis"
        check_url=url+flowAnalysisId
    
        headers={
                "Content-Type":"application/json",
                "X-Auth-Token":ticket
                }
    
        respuesta=requests.get(check_url,headers=headers,verify=False)
        outFormat=respuesta.json()
    
        Status=outFormat["response"]["request"]["status"]
        update=outFormat["response"]["lastUpdate"]
    
        print("\n##############################################################################################################################################\nEl estado de la consulta es: ",Status," Actualizado en: ",update)
        c=0
        while Status != "COMPLETED":
            respuesta=requests.get(check_url,headers=headers,verify=False)
            outFormat=respuesta.json()
            Status=outFormat["response"]["request"]["status"]
            update=outFormat["response"]["lastUpdate"]
            print("El estado de la consulta es: ",Status," Actualizado en: ",update)
            time.sleep(10)
            c+=1
            if Status=="FAILED" and c == 1:
                return print("Fallo inicial de analisis: ",Status)

            elif Status == "FAILED":
                Origen=outFormat["response"]["request"]["sourceIP"]
                Destino=outFormat["response"]["request"]["destIP"]
    
                print("\n##############################################################################################################################################\nEl origen es: ",Origen," y el destino es: ",Destino)
    
                Ele_Net=[]
                Encabezado=["Numero","Nombre","IP","Tipo","ROL"]
                count=0
    
                for ele in outFormat["response"]["networkElementsInfo"]:
                    count+=1
                    dev=(count,
                         ele.get("name"),
                         ele["ip"],
                         ele["type"],
                         ele("linkInformationSource"))
    
                    Ele_Net.append(dev)
    
                return print("\nDispositivos Intermediarios son: \n\n",tabulate(Ele_Net,Encabezado,"\nFallo terminal de analisis: ",Status))
    
        Origen=outFormat["response"]["request"]["sourceIP"]
        Destino=outFormat["response"]["request"]["destIP"]
    
        print("El origen es: ",Origen," y el destino es: ",Destino)
    
        Ele_Net=[]
        Encabezado=["Numero","Nombre","IP","Tipo","ROL"]
        count=0
    
        for ele in outFormat["response"]["networkElementsInfo"]:
            count+=1
            dev=(count,
                 ele.get("name"),
                 ele["ip"],
                 ele["type"],
                 ele.get("linkInformationSource"))
            Ele_Net.append(dev)
    
        return print("\nDispositivos Intermediarios son: \n\n",tabulate(Ele_Net,Encabezado))
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")


def Get_Geo(Ticket):
    try:
        while True:
            ip=input("Dime la IP que quieres Geolocalizar: ")
            Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ipgeo/"+str(ip)
            
            headers={
                    "Content-Type":"application/json",
                    "X-Auth-Token":Ticket
                    }
            
            respuesta=requests.get(Url,headers=headers,verify=False)
            outFormat=respuesta.json()
            
            if respuesta.status_code==400 or respuesta.status_code==404:
                print("No existe el dispositivo con la IP: ", ip)
                op=input("¿Deseas volver a intentarlo?(Y/N): ")
                if op == "Y" or op=="y": 
                    continue
                if op == "N" or op=="n": 
                    return print("Adios")
                else:
                    return print("Opcion marcada incorrecta")
            
            list_loc=[]
            l=[]
            Encabezado=["Ciudad","Provincia","Cod.Provincia","Pais","Cod.Pais","Continente","Cod.Continente","Latitud","Longitud"]
            #Encabezado2=["Direccion","Direccion Geografica","Nombre","ID"]
            
            dic=outFormat["response"][str(ip)]
            
            for v in dic:
                l.append(dic.get(v))
            list_loc.append(l)
            
            return print("\nEsta es la localizacion Geografica de la ip: ",ip,"\n\n",tabulate(list_loc,Encabezado))
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")

def Get_NameSpace(Ticket):
    try:
        while True:
            Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/file/namespace"
            
            headers={
                    "Content-Type":"application/json",
                    "X-Auth-Token":Ticket
                    }
            
            respuesta=requests.get(Url,headers=headers,verify=False)
            outFormat=respuesta.json()
            
            list_Naspa=[]
            l=[]
            Encabezado=["Nombre De Espacios Disponibles"]
            #Encabezado2=["Direccion","Direccion Geografica","Nombre","ID"]
            
            dic=outFormat["response"]
            
            
            for v in dic:
                l=[v]
                list_Naspa.append(l)
    
            return print("\nEstos son los nombres de espacios disposnibles: \n\n",tabulate(list_Naspa,Encabezado))
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")

def Get_FileNS(Ticket):
    try:
        while True:
            NS=input("Introduce el Nombre de Espacio: ")
            Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/file/namespace/"+NS
            
            headers={
                    "Content-Type":"application/json",
                    "X-Auth-Token":Ticket
                    }
            
            respuesta=requests.get(Url,headers=headers,verify=False)
            outFormat=respuesta.json()
            
            resq=outFormat["response"]
            Encabezado=["Numero","Nombre de Espacio","Nombre","Path de Descarga","Tamaño","Formato","md5CK","sha1CK","Encriptado","ID"]
            files=[]
            f=[]
            print(resq)
            
            for el in resq:
                f.append(el.values())
            
            for e in f:
                files.append(e)
    
            print("\nEstos son los ficheros que contiene el Espacio de Nombre: \n\n",tabulate(files,Encabezado,showindex=True))
            op=input("\n¿Te gustaria obtener los ficheros de otro nombre de espacio mas?(Y/N): ")
            if op == "Y" or op=="y": 
                continue
            if op == "N" or op=="n": 
                return print("Adios")
            else:
                return print("Opcion marcada incorrecta")
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")

def Show_File(Ticket):
    try:
        while True:
                ID=input("Inserta el ID del archivo exacto que quieres visualizar: ")
                Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/file/"+ID
                
                headers={
                        "Content-Type":"application/json",
                        "X-Auth-Token":Ticket
                        }
                
                respuesta=requests.get(Url,headers=headers,verify=False)
                
                if respuesta.status_code==400 or respuesta.status_code==404:
                    print("No existe el archivo con el ID: ", ID)
                    op=input("¿Deseas volver a intentarlo?(Y/N): ")
                    if op== "Y" or op=="y":
                        continue
                    if op== "N" or op=="n":
                        return print("Adios")
                    else:
                        return print("Opcion introducida erronea")
                    
                
                outFormat=str(respuesta.text.encode("utf8"))
        
                return print("El contenido del archivo con ID: ",ID," es: \n\n",outFormat)
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")