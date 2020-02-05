import numpy as np
N=10
pila=np.zeros(N,int)
pilaaux=np.zeros(N,int)
V=np.zeros(N,int)
i=0
B=0
while i<N and B==0:
    nro=int(input("Ingrese un nro: "))
    if nro != 0:
        pila[i]=nro
        i+= 1
    else:
        B=1
Tope=i-1

print(pila)
print("Tope: ","[",Tope,"]")

def pila_vacia(tope):
    if tope== -1:
        PilaVacia=True
    else:
        PilaVacia=False
    return PilaVacia

def apilar(pila,tope,nro):
    if tope <=N:
        tope+= 1
        pila[tope]=nro
    return tope

def desapilar(pila,tope):
    PilaVacia=pila_vacia(tope)
    if PilaVacia== True:
        print("La pila esta vacia, no se puede desapilar")
    else:
        pila[tope]=0
        tope+= -1
    return tope

i=0
PilaVacia=pila_vacia(Tope)
while PilaVacia==False:
    V[i]=pila[Tope]
    pilaaux[i]=pila[Tope]
    i+= 1
    Tope=desapilar(pila,Tope)
    PilaVacia = pila_vacia(Tope)
Topeaux=i-1

i=0
B=0
PilaVacia=pila_vacia(Topeaux)
while PilaVacia==False:
    if V[i]!= pilaaux[Topeaux]:
        B= 1
    nro=pilaaux[Topeaux]
    i+= 1
    Tope=apilar(pila,Tope,nro)
    Topeaux= desapilar(pilaaux, Topeaux)
    PilaVacia= pila_vacia(Topeaux)

PilaVacia=pila_vacia(Tope)

print(V)
if B==0:
    print("El nro es Capicúa")
else:
    print("El nro no es Capicúa")
