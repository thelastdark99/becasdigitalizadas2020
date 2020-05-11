import requests,json,urllib3

urllib3.disable_warnings()

#No he podido modificar dadtos porque con el put me los sobreescribia y no he encontradso la soluccion

while True:
    #DATOS QUE VAMOS A CREAR/MODIFICAR
    print("INFORMACION DE LA INTERFAZ A CREAR\n") 
    clase=int(input("Que tipo de ACL deseas crear: \n1.-Standard\n2.-Extended\n3.-Salir\nSelecciona Opcion: "))
    Name=input("¿Como se va a llamar la ACL?(Puede ser tanto nombre como numero): ")
    Sec=int(input("Indica el numero de secuencia de la regla: "))
    Accion=input("Que accion desea realizar?(permit/deny): ")
    if clase==3:
        print("Adios")
        break
    URL="https://192.168.1.202/restconf/data/native/ip/access-list/"

    if clase==1:
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
    if clase==2:
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
    
    #CREDENCIALES
    username="cisco"
    password="cisco123!"
    basicAuth=(username,password)
    
    
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
    
    op=int(input("¿Desea añadir una nueva regla a la ACL creada o prefiere una nueva ACL?\n1.-Nueva Regla\n2.-Nueva ACL\n3.-Salir\nOpcion: "))
    if op==1:
        print(Name)
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
                    insert={
                        'action': Accion, 
                        'protocol': Protocol,
                        'host': Red}
            
                if origen == 3:
                    insert={
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
"""
solicitud=requests.get(URL1,auth=basicAuth,headers=headers,verify=False)
solicitud2=requests.get(URL1,auth=basicAuth,headers=headers,verify=False)
outformat=solicitud.json()
outformat2=solicitud2.json()

print(outformat2)
"""
"""
solicitud=requests.post(URL1,auth=basicAuth,data=json.dumps(body_Config),headers=headers,verify=False)
print(solicitud)
"""
"""
try:
    try:
        solicitud=requests.post(URL1,auth=basicAuth,data=json.dumps(body_Config),headers=headers,verify=False)
    except:
        solicitud=requests.post(URL1,auth=basicAuth,data=json.dumps(body_Config2),headers=headers,verify=False)
    
    if solicitud.status_code>=200 and solicitud.status_code<=399:
        print("Codigo de respuesta: ",solicitud.status_code,". Los datos se han creado con exito")
    else:
        print("Codigo de respuesta: ",solicitud.status_code,". Los datos NO se han podido crear")
except:
    try:
        solicitud=requests.put(URL1,auth=basicAuth,data=json.dumps(body_Config),headers=headers,verify=False)
    except:
        solicitud=requests.put(URL1,auth=basicAuth,data=json.dumps(body_Config2),headers=headers,verify=False)
    
    if solicitud.status_code>=200 and solicitud.status_code<=399:
        print("Codigo de respuesta: ",solicitud.status_code,". Los datos se han modificado con exito")
    else:
        print("Codigo de respuesta: ",solicitud.status_code,". Los datos NO se han podido modificar")
"""

