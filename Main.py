from Enano import *
from Elfo import *
from Humano import *
from random import *

obj_enano=Enano()
obj_elfo=Elfo()
obj_humano=Humano()
global lista
lista=[obj_enano,obj_elfo,obj_humano]

def Atacar(a,b):
    global opcion
    a.HabilidadEspecial()
    b.HabilidadEspecial()
    i=0
    for i in range(10):
        i=i+1
        print("Ronda",i)
        Vacio()
        
        text="{} a atacado a {}".format(a.GetNombre(),b.GetNombre())
        print(text)
        b.SetVida((b.GetVida()-a.GetDamage()))##personaje 1 ataca a personaje 2
        VerificarVida(b,a)
        if v==0:
            break
            
        Espacio()
        Vacio()
        

        text1="{} logra contraatacar...".format(b.GetNombre())
        print(text1)  
        a.SetVida((a.GetVida()-b.GetDamage()))#personaje 2 ataca a personaje 1
        VerificarVida(a,b)
        if v==0:
            break
        
        Espacio()
        Vacio()
        
        
        text2="{} recibio {} de daño y {} recibio {}".format(a.GetNombre(),b.GetDamage(),b.GetNombre(),a.GetDamage())
        print(text2)

        text3="La vida de {} a bajado a {} hp y la de {} a bajado a hp {}".format(a.GetNombre(),a.GetVida(),b.GetNombre(),b.GetVida())
        print(text3)
        Vacio()
        Espacio()
        Vacio()
        
def Juego():
    personaje1=randint(0,2)
    a=lista[personaje1]
    lista.pop(personaje1)

    personaje2=randint(0,1)
    b=lista[personaje2]
    Vacio()
    textonombres="{} vs {}".format(a.GetNombre(),b.GetNombre())
    print(textonombres)
    print("__________________")
    Vacio()
    
    
    texto= "{}, Vida inicial: {}, Daño: {}".format(a.GetNombre(),a.GetVida(),a.GetDamage())
    print(texto)
    
    texto1= "{}, Vida inicial: {}, Daño: {}".format(b.GetNombre(),b.GetVida(),b.GetDamage())
    print(texto1)
    Vacio()
    Vacio()
    Espacio()
    Vacio()
    Atacar(a,b)
       
def Vacio():
    print("")

def Espacio():
    enter=input("Ingrese la tecla enter para continuar...")

def GanadorR10(a,b):
    pass


def VerificarVida(a,b):
    global v
    v=1
    if a.GetVida()<=0:
        a.SetVida(0)
        texto="{} a quedado con {} vida...{} a ganado!!!".format(a.GetNombre(),a.GetVida(),b.GetNombre())
        print(texto)
        v=0
        Vacio()
        Espacio()
        Vacio()
        Vacio()
    else:
        pass
   
while True:
    try:
        global opcion
        Vacio()
        print('Bienvenido al juego Multiversus!')
        Vacio()
        print('1.Jugar\n2.Ver estadisticas de personaje\n3.Cerrar juego')
        opcion=int(input('Opcion: '))     
        if opcion==1:
            Juego()
            Vacio()
            print("Gracias por haber participado!")
            Vacio()
            Vacio()
        if opcion==2:
            Vacio()
            Vacio()
            print("Estadisticas de personajes!")
            Vacio()

            print(obj_enano)           
            print(obj_elfo)  
            print(obj_humano)

            Vacio()
            Espacio()
            Vacio()

        if opcion==3:
            menu=1
            break
    except:
        Vacio()
        print("Ingrese solo numero segun las opciones mostradas...")