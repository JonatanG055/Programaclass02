from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre,apellido, edad,codigo):
        self.nombre = nombre
        self.apellido=apellido
        self.edad = edad
        self.codigo=codigo
        
    @abstractmethod
    def presentarse(self):
        pass

class Estudiante(Persona):
    def presentarse(self):
        return" hola soy {} {} tengo {} años soy tu compañero de clases, codigo {}".format(self.nombre,self.edad,self.apellido,self.codigo) 
class Compañero(Persona):
    def presentarse(self):
        return" hola soy {} {} tengo {} años soy tu compañero de clases, codigo:{}".format(self.nombre,self.edad,self.apellido,self.codigo) 
class Compañera(Persona):
   def presentarse(self):
        return" hola soy {} {}tengo {} años soy tu compañera de clases codigo:{}".format(self.nombre,self.edad,self.apellido,self.codigo) 
def presentarse_persona(persona):
    print(persona.presentarse())

estudiante = Estudiante("Alex"," Mejia", "codigo de estudiante")
estudiante1 = Compañero("","", 35,"u35665446")
Estudiante2 = Compañera("Sofía","Luna", 50,"U25646445")

presentarse_persona(estudiante) 
presentarse_persona(estudiante1)
presentarse_persona(Estudiante2) 
