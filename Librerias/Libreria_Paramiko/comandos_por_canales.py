import time
import paramiko
from getpass import getpass

host = '148.212.51.14'
user = 'usuario3'
ra = "Autentificacion Fallida"

while ra == "Autentificacion Fallida":
     password = getpass('Password: ')

     try:
          client = paramiko.SSHClient() # Crea un objeto del timpo SSHClient()

          client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Con esto indicamos que nos autentificaremos con nuestras propias credenciales con contraseña o llave ssh

          client.connect(host, username=user, password=password) # Con esto nos autentificamos o entramos al servidor
          
          ra = "Autentificacion Correcta"
          print(ra)

          stfin, stdout, stderr = client.exec_command('pwd')
          print(stdout.read().decode())

          session = client.get_transport().open_session() # Esto nos permite abrir una nueva session y permite abrir un canal por donde aplicar el comando
          if session.active:

               # Aplicamos el comando "ls" con exec_command() a la sesion pero para obtener el retorno aplicamos a la sesion .recv("Numero de bits que queremos leer") y converimos a string con .decode()

               # Para relizar mas de 1 comando seguidos usar &&

               session.exec_command('cd Oscar/ && ls') 

               result = session.recv(1024).decode()

               print(result)

               # Los canales solo estan diseñados para recibir un comando y una ves ejecutado se cierran de forma automatica

          client.close() # Cerramos conexion

     except paramiko.ssh_exception.AuthenticationException as e:
          print(ra)