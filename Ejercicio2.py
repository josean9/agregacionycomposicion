"""Enunciado: Teniendo en cuenta el siguiente código, explique por qué el mensaje Yang destruido, se muestra después del signo de interrogación. ¿Qué hay que hacer para que aparezca antes?

class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 
print(yang) 
>>> <__main__.Yang object at 0x1011da828> 
print(yang is yin.yang) 
>>> True 
del(yang) 
print("?") 
>>> ? 
Yang destruido"""
class soldado():
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre
    def __del__(self):
        print("Se ha destruido al soldado {}".format(self.nombre))
soldado1 = soldado("Martin")
print(soldado1.__del__())
soldado2 = soldado("Salim")
for i in range(10):
    print(i)
print(soldado1)
class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 

yin = Yin() 
yang = Yang()
yin.yang = yang 
print(yang) 
print(yang is yin.yang) 
del(yang) 
print("?")



print("""yang es destruido despues de la interrogacion ya que el metodo __del__ de la clase Yang es activado 
tras crear el objeto yang de la clase Yang obligatoriamente aunque no sea llamado, pero se activa una vex el codigo haya terminado, al igual
que el __del__ de la clase soldado, que si lo llamamos, se activa al principio, sino al fianl del codigo
 """)