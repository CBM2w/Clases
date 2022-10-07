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

#print(mayusculas('HolaSoyCarla'))

def crear_hashtag(cadena):
    hashtag = '#'

    if cadena[0].isupper():
        hashtag += cadena[0]
    else:
        hashtag += cadena[0].upper()

    for i in range(1,len(cadena)):
        if cadena[i].islower() and cadena[i] != ' ' and cadena[i-1] != ' ':
            hashtag += cadena[i]
        elif cadena[i] != ' ' and cadena[i].isupper() and cadena[i-1] != ' ':
            hashtag += cadena[i].lower()
        elif cadena[i] != ' ' and cadena[i].isupper() and cadena[i-1] == ' ':
            hashtag += cadena[i]
        elif cadena[i] != ' ' and cadena[i].islower() and cadena[i-1] == ' ':
            hashtag += cadena[i].upper()
    print(hashtag)
    return hashtag

#crear_hashtag('Hola Buenas tArdes')
    

def num_diferente(array):
    num_dif = 0
    dic = {}

    for num in array:
        dic[num] = array.count(num)
    for num in array:
        if dic[num] == 1:
            num_dif = num

    return dic,num_dif

#print(num_diferente([1,1,1,2,1,1,1,1]))

def num_par_impar(array):
    num_dif = 0
    dic = {}

    for num in array:
        rest = num%2
        if str(rest) in dic:
            dic[str(rest)] += 1
        else:
            dic[str(rest)] = 1
        
    print(dic)
    for num in array:
        if dic["0"] == 1:
            if num % 2 == 0:
                num_dif = num
        elif dic["1"] == 1:
            if num % 2 == 1:
                num_dif = num
    
    return dic,num_dif

print(num_par_impar([1,1,1,2,3,3,3]))