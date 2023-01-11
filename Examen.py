#1 
lista = ['Nombre', 23, True, 7.3]

for e in range( 0,len(lista), 2):
    print(lista[len(lista)-1-e])

for i in range(len(lista)):
    if i == 0:
        valor_1 = lista[i]
        lista[i] = lista[len(lista)-1]
    elif i == len(lista)-1:
        lista[i] = valor_1

lista.remove(lista[-1])

lista_2 = []

for i in range(len(lista)):
    lista_2.append((lista[i], lista[i]))

print(lista_2)

dic_ejemplo = {'Alumnos': ["Carlos", "Ana", "Daniela", "Martín"],

'Curso': "Big Data",

'Edad': ('22', '21', '20', '22'),

'Presencial': True

}

def edades(alumno):

    i = dic_ejemplo['Alumnos'].index(alumno)
    edad = dic_ejemplo['Edad'][i]

    return edad

print(edades('Carlos'))

def claves(clave):

    for e in dic_ejemplo:
        if e == clave:
            return True
    return False

print(claves('centro'))
print(claves('Edad'))

def f(clave):
    
    tipo = type(dic_ejemplo[clave])
    long = len(dic_ejemplo[clave])

    return tipo, long

def conjunto():

    conj = set(dic_ejemplo['Edad'])
    long = len(conj)

    return conj, long

l = [18, 50, 210, 80, 145, 330, 70, 30]

for e in l:
    if e > 300:
        break
    if e % 10 == 0 and e < 200:
        print(e)
    
c = ["PEP 8", "PEP 248", "PEP 257"]

def total(lista):
    long = 0

    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] != ' ':
                long += 1
    
    return long

print(total(c))

import numpy as np
import pandas as pd
import random 

a = np.random.randint(0,11, size = (6,6))
print(a)

print(a.mean())
print(np.mean(a))

print(a.std())

c = []

for i in range(len(a)):
    c.append([])
    for m in a[i]:
       c[i].append(m*-1)
       
for e in c:
    print(e)

arr = np.arange(0,101)
print(np.where(arr % 9 == 0))


