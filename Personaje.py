class Personaje:
    def __init__(self,nombre='',raza='',arma='',vida=100,damage=0,bonificacion=0):
        self.__nombre=nombre
        self.__raza=raza
        self.__vida=vida
        self.__damage=damage
        self.__arma=arma
        self.__bonificacion=bonificacion
    def __str__(self):
        return 'Nombre: {}, Raza: {}, Arma: {}, Vida: {}, Daño: {}, Bonificacion: {},'.format(self.GetNombre(),self.GetRaza(),self.GetArma(),self.GetVida(),self.GetDamage(),self.GetBono())

    def GetNombre(self):
        return self.__nombre
    def GetRaza(self):
        return self.__raza
    def GetArma(self):
        return self.__arma
    def GetVida(self):
        return self.__vida
    def GetDamage(self):
        return self.__damage
    def GetBono(self):
        return self.__bonificacion

    def SetNombre(self,nombre):
        self.__nombre=nombre
    def SetRaza(self,raza):
        self.__raza=raza
    def SetArma(self,arma):
        self.__arma=arma
    def SetVida(self,vida):
        self.__vida=vida
    def SetDamage(self,damage):
        self.__damage=damage
    def SetBono(self,bonificacion):
        self.__bonificacion=bonificacion

    

    #revisar funcion
    def MensajeInicial(self):
        print('Instrucciones:\nSe seleccionaran dos personajes aleatorios y estos pelearan por 10 rondas, en caso de alguno quedar con vida 0 o menor, este perdera. Si en la decima ronda ninguno a quedado con 0 vida entonces ganara el que tenga mas vida total.\nEn algunas ocasiones se le pedira ingresar un numero para poder continuar.')

    def Historia(self):
        pass
    def Victoria(self):
        pass
    def Derrota(self):
        pass



