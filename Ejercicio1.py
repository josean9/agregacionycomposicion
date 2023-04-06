"""Enunciado: modelar lo siguiente. Una empresa es propietaria de varios edificios y
 emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y 
 una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio 
 tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los
  edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son 
  propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.

Una vez definidas estas entidades, imagine que su programa es una película estadounidense 
de catástrofes, en la que se destruye New York. Implemente este evento para que todas 
las entidades del juego tengan en cuenta las consecuencias de este cataclismo."""
class Ciudad():
    def __init__(self, nombreCiudad):
        self.nombreCiudad = nombreCiudad
        self.edificios = []
class Empresa(Ciudad):
    def __init__(self, nombreCiudad, nombreEmpresa):
        super().__init__(nombreCiudad)
        self.nombreEmpresa = nombreEmpresa
        self.edificios = super().edificios
        self.empleados = []
ciudad1= Ciudad("New York")
ciudad1.edificios.append("A")
empresa1 = Empresa("New York", "YooHoo!")
"""class Edificio():
class Empleado():"""
