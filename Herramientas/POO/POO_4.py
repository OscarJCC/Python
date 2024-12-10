class Persona():
     
     def __init__(self,nombre,edad,Lugar_residencia):
          self.Nombre = nombre
          self.Edad = edad
          self.Lu_R = Lugar_residencia
          
     def descripcion(self):
          print("Nombre:",self.Nombre,"\nEdad:",self.Edad,"\nResidencia:",self.Lu_R)
          
class Empleado(Persona):
     
     def __init__(self,salario,antiguedad,n_empleado,e_empleado,r_empleado):
          
          super().__init__(n_empleado,e_empleado,r_empleado) #La funcion super llama al constructor que se esta heredando de la clase,
                                                             #Ya que la clase ya tiene un constructor y lo toma como prioridad
          
          self.Salario = salario
          self.Antiguedad = antiguedad
          
     def descripcion(self):
          
          super().descripcion() #Aqui nos permite reutilizar el metodo heredada y poder agregarle mas cosas
          
          print("Salario:",self.Salario,"\nAntiguedad:",self.Antiguedad)
          
Antonio = Empleado(1800,15,"Antonio",18,"Mexico")
                  
Antonio.descripcion()

print(isinstance(Antonio,Persona))# Nos permite comprobar si el objeto pertenece a una cierta clase

