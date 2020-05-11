from netmiko import ConnectHandler
def configurar(usuario,contraseña,ip):
    #Con las credenciales obtenidas deberemos de iniciar la conexion mediante ssh o telnet, indicaremos tipo de dispo,ip u Nombre Host,puerto de conexion,credenciales
    conexionSSH=ConnectHandler(device_type="cisco_ios",
                            host=ip,
                            port=22,
                            username=usuario,
                            password=contraseña)
    
    
    
    #Usamos un metodo llamado send_command para podervenviar comandos del modo enbale,este metodo lo usaremos en nuestra variable que inicia conexion SSH y le pasaremos el comando introducido anteriormente
    Reloj=conexionSSH.send_command("clock set 00:00:00 1 January 2000")
    #Imprimimos resultados en una salida entendible
    print(format(Reloj))
    
    
    configuraciones=["no netconf-yang","netconf-yang","no restconf","restconf"]
    
    Net_Rest=conexionSSH.send_config_set(configuraciones)
    print(format(Net_Rest),"\n")
