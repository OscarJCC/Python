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

          sftp_client = client.open_sftp() # permite hace la conexion sftp para mandar y recibir archivos

          # El metodo .put('Direccion de archivo a mandar','Direccion del lugar donde colocar el archivo en el servidor/Nombre que quiero que tenga el archivo') recibe 2 argumentos
          sftp_client.put(
               'Python\Librerias\Libreria Paramiko Conexion Servidores\README_sftp_put_python.md',
               'Oscar/README_sftp_put_python.md'
          )

          # El metodo .get('Direccion de archivo a recibir','Direccion del lugar donde colocar el archivo en mi PC/Nombre que quiero que tenga el archivo') recibe 2 argumentos

          sftp_client.get(
               'Oscar/Demo_sftp_get_python.py',
               'Python\Librerias\Libreria Paramiko Conexion Servidores\Demo_sftp_get_python.py'
          )

          session = client.get_transport().open_session()
          if session.active:

               session.exec_command('cd Oscar && ls -l')

               result = session.recv(1024).decode()

               print(result)

          sftp_client.close() # Cerramos conexion sftp
          client.close() # Cerramos conexion

     except paramiko.ssh_exception.AuthenticationException as e:
          print(ra)