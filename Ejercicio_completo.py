import os
def agenda():
    agenda = {}

    while True:
        print('1. Añadir/modificar')
        print('2. Buscar')
        print('3. Borrar')
        print('4. Listar')
        print('5. Finalizar programa')
    
        opcion = input('Introduzca la opción elegida: ')
        os.system("cls")
        if opcion == '1':
            nombre = input('Introduzca el contacto: ')
            for e in agenda:
                if e == nombre:
                    print('Ya existe este contacto y el número es ' + agenda[e])
                    modificar = input('¿Quiere modificar el número? s/n')
                    if modificar == 's':
                        nuevo_telefono = input('Introduzca el nuevo teléfono: ')
                        agenda[e] = nuevo_telefono
            if nombre not in agenda:
                telefono = input('Introduzca el teléfono: ')
                agenda[nombre] = telefono
        
        elif opcion == '2':
            cadena = input('Introduzca su búsqueda: ')
            for e in agenda:
                if e.lower().startswith(cadena.lower()):
                    print(e,agenda[e])
                else:   
                    print('No hay resultados de la búsqueda.')

        elif opcion == '3':
            nombre = input('Introduzca el contacto: ')
            if nombre in agenda:
                del agenda[nombre]
            else:
                print('El contacto no existe.')

        elif opcion == '4':
            for e in agenda:
                print(e,' ',agenda[e])

        elif opcion == '5':
            break


agenda()