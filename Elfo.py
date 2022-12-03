from Personaje import Personaje
from random import *

class Elfo(Personaje):
    def __init__(self, nombre='Licht', raza='Elfo', arma='magia', vida=92, damage=18, bonificacion=0,reino='Noche blanca'):
        super().__init__(nombre, raza, arma, vida, damage, bonificacion)
        self.__reino=reino

    def __str__(self):
        return super().__str__()+" Reino: {}".format(self.GetReino())

    def GetReino(self):
        return self.__reino

    def SetReino(self,reino):
        self.__reino=reino

    
    #Metodo "QuitaVida" paso a llamarse "HabilidadEspecial" para facilidad de compilacion
    def QuitaVida(self,b):
        a="Elfo - {}".format(self.GetNombre())
        print(a)
        print("Habilidad especial: Quita Vida")
        Vacio()
        b.SetVida(b.GetVida()*0.9)
        texto=("{} a invocado la habilidad 'Quita vida', la vida de {} a sido reducida en un 90%").format(self.GetNombre(),b.GetNombre())
        print(texto)
        Vacio()
        Espacio()

    def Historia(self):   
        texto="Los Elfos han intentado esclavizar a las demas razas por lo que han llevado una guerra durante 300 años. Pero por fin han sido derrotados, esto marcara un antes y despues en las futuras generaciones..."
        print(texto)
        

    def Victoria(self):
        Vacio()
        texto="{} a salido victorioso!".format(self.GetNombre())
        print(texto)
        Vacio()
        print(self)

    def Derrota(self):
        text="{} a perdido...".format(self.GetNombre())
        print(text)
        self.Historia()

def Vacio():
    print("")
def Espacio():
    enter=input("Ingrese la tecla enter para continuar...")