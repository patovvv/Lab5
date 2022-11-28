from Personaje import Personaje
from random import *

class Humano(Personaje):
    def __init__(self, nombre='Guts', raza='Humano', arma='Matadragones', vida=97, damage=13, bonificacion=0,familia='Banda de los halcones'):
        super().__init__(nombre, raza, arma, vida, damage, bonificacion)
        self.__familia=familia

    def __str__(self):
        return super().__str__()+" Familia: {}".format(self.GetFamilia())

    def GetFamilia(self):
        return self.__familia
    def SetFamilia(self,familia):
        self.__familia=familia

    
    #Metodo "SuperBono" paso a llamarse "HabilidadEspecial" para facilidad de compilacion
    def HabilidadEspecial(self):
        while True:
            try:
                Vacio()
                a="Humano - {}".format(self.GetNombre())
                print(a)
                print("Habilidad especial: Super Bono")
                Vacio()

                dmage=int(input("Ingrese un numero entre 5 y 15: "))

                while dmage<5 or dmage>15:
                    dmage=int(input("Solo numeros entre 5 y 15... tambien puede incluirlos: "))
                    
                valor=dmage-2
                self.SetDamage(self.GetDamage()+valor)
                texto="El daño de {} aumento en {}, el nuevo daño total es: {}".format(self.GetNombre(),valor,self.GetDamage())
                print(texto)
                Vacio()
                break                
            except:
                print("Ingrese solo numeros...")

    def Historia(self):
        return super().Historia()

    def Victoria(self):
        return super().Victoria()

    def Derrota(self):
        return super().Derrota()
def Vacio():
    print("")




