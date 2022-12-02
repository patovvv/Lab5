from Enano import *
from Elfo import *
from Humano import *
from random import *
import time

obj_enano=Enano()
obj_elfo=Elfo()
obj_humano=Humano()
global lista
lista=[obj_enano,obj_elfo,obj_humano]

def Atacar(a,b):
    time.sleep(1)   

    if a==obj_humano or b==obj_humano:
        obj_humano.SuperBono()
    
    if a==obj_elfo:
        obj_elfo.QuitaVida(b)       
    if b==obj_elfo:
        obj_elfo.QuitaVida(a)
        
    if a==obj_enano or b==obj_enano:
        obj_enano.AumentaVida()

    i=0
    for i in range(10):
        i=i+1
        print("Ronda",i)
        print("_________")

        aleatorio=randint(1,4)

        if aleatorio==1:#P1 ataca a P2 y P2 no logra contraatacar
            text="{} a atacado a {}".format(a.GetNombre(),b.GetNombre())
            print(text)
            time.sleep(1)

            text1="{} no logro contraatacar a {}...".format(b.GetNombre(),a.GetNombre())
            print(text1)
            time.sleep(1)
            b.SetVida((b.GetVida()-a.GetDamage()))##personaje 1 ataca a personaje 2
            VerificarVida(b,a)
            if v==0:
                break
            time.sleep(1)

        if aleatorio==2:#P1 ataca a P2 y P2 contraataca
            text="{} a atacado a {}".format(a.GetNombre(),b.GetNombre())
            print(text)
            b.SetVida((b.GetVida()-a.GetDamage()))##personaje 1 ataca a personaje 2

            time.sleep(1)
            VerificarVida(b,a)
            if v==0:
                break
            time.sleep(1)
            
            text1="{} logro contraatacar a {}...".format(b.GetNombre(),a.GetNombre())
            print(text1)
            a.SetVida((a.GetVida()-b.GetDamage()))#personaje 2 ataca a personaje 1
            time.sleep(1)
            VerificarVida(a,b)
            if v==0:
                break
            time.sleep(1)

        if aleatorio==3:#P2 ataca a P1 y P1 no puede contraatacar
            text="{} a atacado a {}".format(b.GetNombre(),a.GetNombre())
            print(text)
            a.SetVida((a.GetVida()-b.GetDamage()))##personaje 1 ataca a personaje 2
            time.sleep(1)
            VerificarVida(a,b)
            if v==0:
                break

            text1="{} no logro contraatacar a {}...".format(a.GetNombre(),b.GetNombre())
            print(text1)
            time.sleep(1)

        if aleatorio==4:#P2 ataca a P1 y P1 contraataca 
            text="{} a atacado a {}".format(b.GetNombre(),a.GetNombre())
            print(text)
            a.SetVida((a.GetVida()-b.GetDamage()))##personaje 1 ataca a personaje 2
            time.sleep(1)
            VerificarVida(a,b)
            if v==0:
                break

            text1="{} logro contraatacar a {}...".format(a.GetNombre(),a.GetNombre())
            print(text1)
            b.SetVida((b.GetVida()-a.GetDamage()))#personaje 2 ataca a personaje 1
            time.sleep(1)
            VerificarVida(b,a)
            if v==0:
                break

        Vacio()
        text2="{} recibio {} de daño y {} recibio {}".format(a.GetNombre(),b.GetDamage(),b.GetNombre(),a.GetDamage())
        print(text2)
        time.sleep(1)
        text3="La vida de {} a bajado a {} hp y la de {} a bajado a hp {}".format(a.GetNombre(),a.GetVida(),b.GetNombre(),b.GetVida())
        print(text3)
        time.sleep(1)
        Vacio()
        Espacio()
        Vacio()
    GanadorR10(a,b)
    
def Juego():
    personaje1=randint(0,2)
    a=lista[personaje1]
    lista.pop(personaje1)

    personaje2=randint(0,1)
    b=lista[personaje2]
    Vacio()
    time.sleep(1.5)   
    textonombres="{} vs {}".format(a.GetNombre(),b.GetNombre())
    print(textonombres)
    print("__________________")
    Vacio()
    
    time.sleep(1)   
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
    if a.GetVida()>b.GetVida():
        print("Finalizando las 10 rondas de batalla")
        print("Calculando ganador...")
        time.sleep(2)
        texto="El ganador es {} con un total de {} hp".format(a.GetNombre(),a.GetVida())
        print(texto)
        
    if b.GetVida()>a.GetVida():
        print("Finalizando las 10 rondas de batalla")
        print("Calculando ganador...")
        time.sleep(2)
        texto="El ganador es {} con un total de {} hp".format(b.GetNombre(),b.GetVida())
        print(texto)


def VerificarVida(a,b):
    global v
    v=1
    if a.GetVida()<=0:
        a.SetVida(0)
        texto="{} a quedado con {} vida...".format(a.GetNombre(),a.GetVida())
        print(texto)
        v=0
        b.Victoria()
        a.Derrota()
        Vacio()
        Espacio()
        Vacio()
        Vacio()
    else:
        pass
   
while True:
    try:
        
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
            time.sleep(1)           
            print(obj_elfo)  
            time.sleep(1)   
            print(obj_humano)
            time.sleep(1)   
            Vacio()
            Espacio()
            Vacio()

        if opcion==3:
            time.sleep(1)  
            Vacio() 
            print("Saliendo del juego...Gracias por participar!")
            Vacio()
            menu=1
            break
    except:
        Vacio()
        time.sleep(1)   
        print("Ingrese solo numero segun las opciones mostradas...")
        Vacio()