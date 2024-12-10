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

          stfin, stdout, stderr = client.exec_command('ls') # Una forma de aplicamos el comando "ls" con .exec_command() y nos retorna un estandar in, out y err

          time.sleep(1) # De tenemos por un segundo para asegurar que todos los out se hayan capturado

          result = stdout.read().decode() # Con esto leemos el estandar out con .read() y lo convertimos en string con .decode()

          print(result)

          client.close() # Cerramos conexion

     except paramiko.ssh_exception.AuthenticationException as e:
          print(ra)