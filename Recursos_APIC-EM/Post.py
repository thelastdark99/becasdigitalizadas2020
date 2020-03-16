import json,requests,urllib3
from tabulate import *
from Curso_de_Programacion_De_Redes.Funcionalidadades.Get import *
from symbol import except_clause

urllib3.disable_warnings() #Desactiva lo warning provocads por SSL

def Ticket(user,passwd):
    url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    
    headers={
        "Content-Type":"application/json"
        }
    
    body={
        "username":user,
        "password":passwd
        }
    respuesta=requests.post(url,json.dumps(body),headers=headers,verify=False)
    outFormat=respuesta.json()#la respuesta en formato json
    
    if respuesta.status_code == 401:
        print(respuesta.status_code,"--> Las credenciales son ERRONEAS")
        exit()
    if respuesta.status_code == 200:
        ticket=outFormat["response"]["serviceTicket"]
        print("Tu Ticket es: ",ticket)
        return ticket
    else:
        raise Exception(respuesta.status_code,"--> Visita para mas informacion: 'https://devnetsbx-netacad-apicem-3.cisco.com/swagger#!/'",respuesta.text)

def Location(ticket):
    try:
        while True:
            Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location"
            
            dire=input("Introduce una direccion: ")
            des=input("Introduce una etiqueta: ")
            nom=input("Introduce un nombre: ")
            
            headers={
                "Content-Type":"application/json",
                "X-Auth-Token":ticket
                }
            
            body={
                  "civicAddress": dire,
                  "description": des,
                  "id": "",
                  "locationName": nom
                }
            
            respuesta=requests.post(Url,json.dumps(body),headers=headers,verify=False)
            outFormat=respuesta.json()
            
            tid=outFormat["response"]["taskId"]
            print("Localizacion creada con exito, el numero es (No ID): ",tid)
            
            op=input("¿Le gustaria crear otra nueva Localizacion?(Y/N): ")
            if op == "Y" or op== "y":
                continue
            
            op=input("¿Le gustaria Obtener Datos de las Localizaciones ahora?(Y/N): ")
            if op == "Y" or op== "y":
                Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location/"
                respuesta=requests.get(Url,headers=headers,verify=False)
                outFormat=respuesta.json()
    
                list_loc=[]
                Encabezado=["Numero","Direccion","Direccion Geografica","Descripcion","Nombre","ID"]
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
                return print("\nAdios")
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")
        

def Update_Location(ticket):
    try:
        while True:
            Uid=input("Inserta el ID de la localizacion a actualizar: ")
            Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location"
            
            headers={
                    "Content-Type":"application/json",
                    "X-Auth-Token":ticket
                    }
            
            dire=input("Introduce una direccion: ")
            des=input("Introduce una descripcion: ")
            nom=input("Introduce un nombre: ")
            
            body={
                      "civicAddress": dire,
                      "description": des,
                      "id": Uid,
                      "locationName": nom,
                }
            
            respuesta=requests.put(Url,json.dumps(body),headers=headers,verify=False)
            outFormat=respuesta.json()
            
            if respuesta.status_code==400:
                print("No existe el ID de localizacion: ",Uid)
                op=input("¿Deseas volver a intentarlo?(Y/N): ")
                if op== "Y" or op=="y":
                    continue
                else:
                    return print("No ha sido posible una actualizacion de la localizacion con la ID: ",Uid)
            else:
                op=input("\nLocalizacion Actualizada con Exito\n¿Te gustaria actualizar alguna mas?(Y/N): ")
                if op == "Y" or op=="y": 
                    continue
                op=input("\n¿Te gustaria comprobar los cambios?(Y/N): ")
                if op == "Y" or op=="y":
                    Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location/"+str(Uid)
                    respuesta=requests.get(Url,headers=headers,verify=False)
                    outFormat=respuesta.json()
                    d=[]
                    l=[]
                    datos=outFormat["response"]
                    for e in datos:
                        l.append(datos.get(e))
                    d.append(l)
                    return print("\nEsta es la infomacion de la localizacion: \n\n",tabulate(d,headers=["Direccion","Direccion Geografica","Descripcion","Nombre","Id"]) )
                else:
                    return print("Cambios realizados con Exito :)")
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")

def Delete_Location(ticket):
    try:
        while True:
            Uid=input("Inserta el ID de la localizacion a eliminar: ")
            Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location/"+str(Uid)
                    
            headers={
                    "Content-Type":"application/json",
                    "X-Auth-Token":ticket
                    }
            respuesta=requests.delete(Url,headers=headers,verify=False)
            if respuesta.status_code==400:
                print("No existe el ID de localizacion: ",Uid)
                op=input("¿Deseas volver a intentarlo?(Y/N): ")
                if op== "Y":
                    continue
                else:
                    return 0
            else:
                op=input("\nLocalizacion Borrada con Exito\n¿Te gustaria borrar alguna mas?(Y/N): ")
                if op == "Y" or op=="y": 
                    continue
                op=input("\n¿Te gustaria comprobar los cambios?(Y/N): ")
                if op == "Y" or op=="y":   
                    Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/location/"
                    respuesta=requests.get(Url,headers=headers,verify=False)
                    outFormat=respuesta.json()
        
                    list_loc=[]
                    Encabezado=["Numero","Direccion","Direccion Geografica","Descripcion","Nombre","ID"]
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
                    return print("Cambios realizados con Exito :)")
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")


def Flow_Id(ticket):
    try:
        url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis"
        #Probar con las IP comentadas ya que las demas dan Error(No es por problemas de script ya que funcionan otras IP solo que no llegan al estado COMPLETED
        ip_Ori=input("IP de Origen: ")#"10.1.12.20"
        ip_Des=input("IP de Destino: ")#"10.1.15.100"
        
        headers={
            "Content-Type":"application/json",
            "X-Auth-Token":ticket
            }
        
        body={
          "destIP": ip_Des,
          "sourceIP": ip_Ori
          }
             
        if not ip_Ori:
            print("ERROR EN DIRECCION DE ORIGEN")
            exit()
        if not ip_Des:
            print("ERROR EN DIRECCION DE DESTINO")
        else:
            print("\n##############################################################################################################################################\nLas IP introducidas son: \nIP de Origen: ",ip_Ori,"\nIP de Destino: ",ip_Des)
        
        respuesta=requests.post(url,json.dumps(body),headers=headers,verify=False)
        outFormat=respuesta.json()
        flowAnalysisId="/"+str(outFormat["response"]["flowAnalysisId"])
        
        print("\n##############################################################################################################################################\nflowAnalysisId:",flowAnalysisId)
        return flowAnalysisId
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")

def New_NS_and_File(ticket):
    try:
        while True:
            NS=input("Nombre de Espacio(Si no existe se crea): ")
            ruta=input("Inserta la ruta absoluta del archivo: ")
            file=open(ruta,"rb")
            
            headers = {
                        'X-Auth-Token': ticket,
                        'scope': 'ALL'
                        #'Content-Type': 'multipart/form-data; boundary=--------------------------114331356951031401294059'
                        #"Accept":"text/plain"
                        }
            values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
            
            files={
                      "fileUpload":file
                }
            
            Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/file/"+NS+"?toEncrypt=true"
            
            respuesta=requests.post(Url,headers=headers,data=values,files=files)
            
            print("Los cambios se han realizado con exito")
            op=input("\n¿Te gustaria comprobar los cambios?(Y/N): ")
            
            if op == "Y" or op=="y":
                return Get_FileNS(ticket)
            
            if op == "N" or op=="n": 
                op=input("\n¿Te gustaria subir algun otro archivo o crear un nombre de espacio?(Y/N): ")
                if op == "Y" or op=="y":
                    continue
                if op == "N" or op=="n":
                    return print("Adios")
                else:
                    return print("Opcion marcada incorrecta, los cambios anteriores se han realizado con exito")
            else:
                return print("Opcion marcada incorrecta")
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")

def Update_NS_and_File(ticket):
    try:
        while True:
            NS=input("Nombre de Espacio existente: ")
            ID=input("Inserta el ID del archivo exacto que quieres modificar: ")
            ruta=input("Inserta la ruta absoluta del archivo original: ")
            file=open(ruta,"rb")
            
            headers = {
                        'X-Auth-Token': ticket,
                        'scope': 'ALL'
                        }
            values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
            
            files={
                      "fileUpload":file
                }
            
            Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/file/"+NS+"/"+ID
            print(Url)
            
            respuesta=requests.put(Url,headers=headers,data=values,files=files)
            
            if respuesta.status_code==409:
                op=input("\nEl nombre de Espacio introducido no existe\n¿Te gustaria volver a intentarlo?(Y/N): ")
                if op == "Y" or op=="y":
                    continue
                if op == "N" or op=="n":
                    return print("Adios")
                else:
                    print("Opcion marcada incorrecta, los cambios anteriores se han realizado con exito")
            elif respuesta.status_code==400:
                op=input("\nEl ID introducido no existe\n¿Te gustaria volver a intentarlo?(Y/N): ")
                if op == "Y" or op=="y":
                    continue
                if op == "N" or op=="n":
                    return print("Adios")
                else:
                    print("Opcion marcada incorrecta, los cambios anteriores se han realizado con exito")
            
            print("\nLos cambios se han realizado con exito")
            op=input("\n¿Te gustaria comprobar los cambios?(Y/N)(Fijate en el Tamaño): ")
    
            if op == "Y" or op=="y":
                return Get_FileNS(ticket)
            
            if op == "N" or op=="n": 
                op=input("\n¿Te gustaria modificar algun otro archivo?(Y/N): ")
                if op == "Y" or op=="y":
                    continue
                if op == "N" or op=="n":
                    return print("Adios")
                else:
                    print("Opcion marcada incorrecta, los cambios anteriores se han realizado con exito")
            else:
                return print("Opcion marcada incorrecta")
    except:
        return print("\nNo es posible obtener informacion del servidor Cod.Error: ",respuesta.status_code,"\nPara mas informacion visitar: https://developer.mozilla.org/es/docs/Web/HTTP/Status")
    
def Delete_NS_and_File(ticket):
    while True:
        Uid=input("Inserta el ID del Nombre de Espacio a eliminar: ")
        Url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/file/"+str(Uid)
                
        headers={
                "Content-Type":"application/json",
                "X-Auth-Token":ticket
                }
        respuesta=requests.delete(Url,headers=headers,verify=False)
        if respuesta.status_code==400 or respuesta.status_code==404:
            print("No existe el ID de Nombre de Espacio: ",Uid)
            op=input("¿Deseas volver a intentarlo?(Y/N): ")
            if op== "Y":
                continue
            else:
                return 0
        else:
            op=input("\n¿Te gustaria borrar otro archivo?(Y/N): ")
            if op == "Y" or op=="y":
                continue
            if op == "N" or op=="n":
                op=input("¿Te gustaria comprobar los cambios?(Y/N): ")
                if op == "Y" or op=="y":
                    return Get_FileNS(ticket)
            else:
                return print("Cambios realizados con Exito :)")