""""En el último ejercicio de la sección sobre la herencia, se mostraron los límites
de la herencia múltiple: acoplamientos de clases cuyo vínculo no es tan obvio, 
atajos tomados en el código que tienen mucho riesgo de error. Este ejercicio utiliza 
otro enfoque del problema: la asociación (ya sea composición o agregación). 

Enunciado: comenzando con el mismo código que el ejercicio sobre herencia múltiple, 
cree una clase que agrupe el comportamiento común entre las clases Ventana y ParedCortina.

Enunciado: modifique las clases Ventana y ParedCortina para que usen esta nueva 
clase-interfaz Cristal.

Enunciado: modifique el código para que el programa funcione de nuevo.
"""
from enum import Enum
class Orientacion(Enum):
    NORTE = "NORTE"
    SUR = "SUR"
    ESTE = "ESTE"
    OESTE = "OESTE"
class Proteccion(Enum):
    PERSIANA = "PERSIANA"
    ESTOR = "ESTOR"
class Cristal():
    pass
class Pared():
    def __init__(self, orientacion):
        orientacion = Orientacion(orientacion.upper())
        self.orientacion = orientacion
    ventanas = []
    def masVentanas(self, ventana):
        self.ventanas.append(ventana)
    def __str__(self):
        return "Pared {}".format(self.orientacion)
class Ventana():
    def __init__(self, pared, ancho, proteccion):
        self.pared = pared
        self.ancho = ancho
        self.proteccion = Proteccion(proteccion.upper())
        if self.proteccion != Proteccion.ESTOR and self.proteccion != Proteccion.PERSIANA:
            raise ValueError("La proteccion debe ser persiana o estor")
        self.pared.masVentanas(self)
    def __str__(self):
        return "Ventana en {}".format(self.pared)
class Casa():
    def __init__(self, paredes):
        self.paredes = paredes
    def superficie_acristalada(self):
        superficie = 0
        for pared in self.paredes:
            for ventana in pared.ventanas:
                superficie += ventana.ancho
        return superficie
# Instanciación de las paredes 
pared_norte = Pared("NORTE") 
pared_oeste = Pared("OESTE") 
pared_sur = Pared("SUR") 
pared_este = Pared("ESTE") 
# Instanciación de las ventanas 
ventana_norte = Ventana(pared_norte, 0.5, "persiana") 
ventana_oeste = Ventana(pared_oeste, 1, "estor") 
ventana_sur = Ventana(pared_sur, 2, "persiana") 
ventana_este = Ventana(pared_este, 1, "estor") 
# Instanciación de la casa con las 4 paredes 
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este]) 
print(casa.superficie_acristalada()) 