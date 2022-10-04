def impar(lista):
    dic_list = {}

    for num in lista:
        if num in dic_list:
            dic_list[num] += 1
        else:
            dic_list[num] = 1
    
    result = 0

    for key in dic_list:
        if dic_list[key] % 2 == 1:
            result = key

    return result

#print(impar([1,2,3,1,2,3,1]))

def lista_cadena(cadena):
    lista = []

    if len(cadena) % 2 == 1:
        cadena += '_'
    
    for i in range(0,len(cadena),2):
        lista.append(cadena[i]+cadena[i+1])

    return lista

#print(lista_cadena('Holaa'))


def mayusculas(cadena):
    cadena_act = ''

    for l in range(len(cadena)):
        if l == 0:
            cadena_act += cadena[l]
        elif cadena[l].isupper():
            cadena_act += ' ' + cadena[l]
        else:
            cadena_act += cadena[l]

    return cadena_act

print(mayusculas('HolaSoyCarla'))
