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
    def deletear(self):
        nm = self.nombre
        print("Se va ha destruir al empleado {}".format(self.nombre))
        del self
        return "Se ha destruido el empleado {}".format(nm)
    def __str__(self):
        return self.nombre
class Edificio():
    def __init__(self, nombre, ciudad, empleados=[]):
        self.nombre = nombre
        self.ciudad = ciudad
        self.empleados = empleados
    def deletear(self):
        mn = self.nombre
        print("Se va ha destruir el edificio {}".format(self.nombre))
        for empleado in self.empleados:
            
            empleado.deletear()
        del self
        return "Se ha destruido el edificio {}".format(mn)
    def __str__(self):
        return self.nombre
class Empresa():
    def __init__(self, nombre, edificios=[]):
        self.nombre = nombre
        self.edificios = edificios
    def deletear(self):
        nj = self.nombre
        print("Se va ha destruir la empresa {}".format(self.nombre))
        for edificio in self.edificios:
            edificio.deletear()
        del self
        return "Se ha destruido la empresa {}".format(nj)
    def __str__(self):
        return self.nombre
class Ciudad():
    def __init__(self, nombre, edificios=[]):
        self.nombre = nombre
        self.edificios = edificios
    def deletear(self):
        nc = self.nombre
        print("Se va ha destruir la ciudad {}".format(self.nombre))
        for edificio in self.edificios:
            edificio.deletear()
        del self
        return "Se ha destruido la ciudad {}".format(nc)
    def __str__(self):
        return self.nombre
empleado1 = Empleado("Martin")
empleado2 = Empleado("Salim")
empleado3 = Empleado("Xing")
empleado4 = Empleado("Paco")
empleado5 = Empleado("Juan")
empleado6 = Empleado("Pedro")
empleado7 = Empleado("Luis")
edificio1 = Edificio("A", "New York", [empleado1, empleado2])
edificio2 = Edificio("B", "New York", [empleado3])
edificio3 = Edificio("C", "Los Angeles", [empleado4, empleado5, empleado6, empleado7])
empresa1 = Empresa("YooHoo!", [edificio1, edificio2, edificio3])
ciudad1 = Ciudad("New York", [edificio1, edificio2])
print(empresa1.deletear())