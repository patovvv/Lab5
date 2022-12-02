from Personaje import Personaje
from random import *

class Enano(Personaje):
    def __init__(self, nombre='Elrond', raza='Enano', arma='super fuerza', vida=91, damage=9, bonificacion=0,clan='Nogrod'):
        super().__init__(nombre, raza, arma, vida, damage, bonificacion)
        self.__clan=clan
    
    def __str__(self):
        return super().__str__()+' Clan: {}'.format(self.GetClan())

    def GetClan(self):
        return self.__clan
    def SetClan(self,clan):
        self.__clan=clan

    #Metodo "AumentaVida" paso a llamarse "HabilidadEspecial" para facilidad de compilacion
    def AumentaVida(self):
        while True:
            try:
                a="Enano - {}".format(self.GetNombre())
                print(a)
                print("Habilidad especial: Aumenta vida")
                valor=int(input("Ingrese un numero entre 50 y 100: "))
                while valor<50 or valor>100:
                    valor=int(input("Solo numeros entre 50 y 100... tambien puede incluirlos: "))
                valorr=valor//2
                self.SetVida(self.GetVida()+valorr)
                texto="La vida de {} a aumentado en {}, la nueva vida total es: {}".format(self.GetNombre(),valorr,self.GetVida())
                print(texto)    
                Vacio()     
                break           
            except:
                Vacio()
                print("Ingrese solo numeros...")


    def Historia(self):
        return super().Historia()

    def Victoria(self):
        texto="{} a salido victorioso!".format(self.GetNombre())
        print(texto)
        Vacio()
        print(self)

    def Derrota(self):
        text="{} a perdido...".format(self.GetNombre())
        texto="Los Enanos han intentado evitar la guerra de los 300 años, pero no han conseguido escapar de esta. Esto marcara la esclavitud de la raza Enana...Hasta que ocurra una posible futura revolucion"
        print(text)
        print(texto)
def Vacio():
    print("")
    