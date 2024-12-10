import time
import paramiko
import scp
from getpass import getpass

host = '148.212.51.14'
user = 'usuario3'
ra = "Autentificacion Fallida"

while ra == "Autentificacion Fallida":
     password = getpass('Password: ')
     try:
          client = paramiko.SSHClient()

          client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

          client.connect(host, username=user, password=password)
          
          ra = "Autentificacion Correcta"
          print(ra)

          stfin, stdout, stderr = client.exec_command('pwd')
          print(stdout.read().decode())
          
          scp_client = scp.SCPClient( client.get_transport() ) # Generamos una conexion scp.() que recibe de argumento un objeto transport()
          
          # El metodo .put('Direccion de archivo a mandar','Direccion del lugar donde colocar el archivo en el servidor') recibe 2 argumentos
          scp_client.put(
               'Python\Librerias\Libreria Paramiko Conexion Servidores\README_scp_put_python.md',
               'Oscar/'
          )

          # El metodo .get('Direccion de archivo a recibir','Direccion del lugar donde colocar el archivo en mi PC') recibe 2 argumentos

          scp_client.get(
               'Oscar/Demo_scp_get_python.py',
               'Python\Librerias\Libreria Paramiko Conexion Servidores'
          )

          session = client.get_transport().open_session()
          if session.active:

               session.exec_command('cd Oscar && ls -l')

               result = session.recv(1024).decode()

               print(result)

          scp_client.close() # Cerramos conexion sftp
          client.close() # Cerramos conexion

     except paramiko.ssh_exception.AuthenticationException as e:
          print(ra)