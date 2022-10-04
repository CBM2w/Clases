def crear_dic():
    dic = {}
    return dic

def añadir(clave,valor,dic):
    dic[clave] = valor

diccionario = crear_dic()
añadir('azul','blue',diccionario) 
print(diccionario)
'''
def comprobar(clave,valor,dic):
    if clave not in dic:
        dic[clave] = valor
    else:
        print('Ya existe el elemento.')
'''
def comprobar(clave,dic):
    comprob = True
    for key in dic:
        if key == clave:
            comprob = False
    return comprob
            
    
def añadir_e(clave,valor,dic):
    if comprobar(clave,dic):
        dic[clave] = valor
    else:
        print('Ya existe el elemento.')

añadir_e('rojo','red',diccionario)
print(diccionario)
añadir_e('rojo','red',diccionario)
print(diccionario)

def alterar_valor(clave,valor,dic):
    if comprobar(clave,dic) == False:
        dic[clave] = valor
    else:
        print("No existe, obj añadido al diccionario")
        añadir(clave,valor,dic)

alterar_valor('rojo','green',diccionario)
print(diccionario)
alterar_valor('morado','purple',diccionario)
print(diccionario)

