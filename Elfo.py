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
    def HabilidadEspecial(self,b):
        a="Elfo - {}".format(self.GetNombre())
        print(a)
        print("Habilidad especial: Quita Vida")
        Vacio()
        b.SetVida(b.GetVida()*0.9)
        texto=("{} a invocado la habilidad 'Quita vida', la vida del enemigo a sido reducida en un 90%").format(self.GetNombre())
        print(texto)
        Vacio()

    def Historia(self):
        return super().Historia()

    def Victoria(self):
        return super().Victoria()

    def Derrota(self):
        return super().Derrota()
def Vacio():
    print("")