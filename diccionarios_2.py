def cuadrados():
    n = int(input('Introduce un número: '))
    dic = {}

    for i in range(1,n+1):
        dic[i] = i**2

    return dic

#print(cuadrados())

def leer_cadena():
    cadena = input('Introduce una cadena: ')
    dic = {}

    for letra in cadena:
        if letra.lower() in dic:
            dic[letra.lower()] += 1
        else:
            dic[letra.lower()] = 1
    return dic

#print(leer_cadena())

def frutas():
    dic = {'Pera':4,'Manzana':6}


    bucle = True
    while bucle:
        fruta = input('Introduce una fruta: ')
        if fruta in dic:
            n = int(input('Introduce el numero de frutas: '))
            precio = n * dic[fruta]
            print(precio)
        else:
            print('no existe')
            
        pregunta = input('¿Quieres meter otra fruta?(si/ no): ')

        if pregunta == 'si':
            pass
        elif pregunta == 'no':
            bucle=False
        else:
            pregunta = input('¿Quieres meter otra fruta?(si/ no): ')
    
        

frutas()
