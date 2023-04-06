"""Enunciado: modelar lo siguiente. Una empresa es propietaria de varios edificios y
 emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y 
 una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio 
 tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los
  edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son 
  propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.

Una vez definidas estas entidades, imagine que su programa es una película estadounidense 
de catástrofes, en la que se destruye New York. Implemente este evento para que todas 
las entidades del juego tengan en cuenta las consecuencias de este cataclismo."""
class Empleado():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre
class Edificio():
    def __init__(self, nombre, ciudad, empleados=[]):
        self.nombre = nombre
        self.ciudad = ciudad
        self.empleados = empleados
    def __del__(self):
        print("Se ha destruido el edificio {}".format(self.nombre))
        for empleado in self.empleados:
            
            print(empleado.__del__)
        del self
    def __str__(self):
        return self.nombre
class Empresa():
    def __init__(self, nombre, edificios=[]):
        self.nombre = nombre
        self.edificios = edificios
    def __del__(self):
        print("Se ha destruido la empresa {}".format(self.nombre))
        for edificio in self.edificios:
            
            print(edificio.__del__())
        del self
    def __str__(self):
        return self.nombre