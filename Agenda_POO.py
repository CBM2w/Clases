class Agenda():

    def __init__(self):
        self.agenda = {}

    def añadir_modificar(self):
        nombre = input('Introduce el nombre del contacto: ')
        
        for e in self.agenda:
                if e == nombre:
                    print('Ya existe este contacto y el número es ' + self.agenda[e])
                    modificar = input('¿Quiere modificar el número? s/n')
                    if modificar == 's':
                        nuevo_telefono = input('Introduzca el nuevo teléfono: ')
                        self.agenda[e] = nuevo_telefono
        if nombre not in self.agenda:
            telefono = input('Introduzca el teléfono: ')
            correo = input('Introduce el correo electrónico: ')
            self.agenda[nombre] = telefono,correo
    
    def buscar(self):
        cadena = input('Introduce tu búsqueda: ')
        for e in self.agenda:
            if e.lower().startswith(cadena.lower()):
                print(e,self.agenda[e])
            else:   
                print('No hay resultados de la búsqueda.')

    def borrar(self):
        nombre = input('Introduce el nombre del contacto: ')
        if nombre in self.agenda:
            del self.agenda[nombre]
        else:
            print('El contacto no existe.')

    def listar(self):
        for e in self.agenda:
                print(e,' ',self.agenda[e])

    def finalizar_programa(self):
        exit()

    def menu(self):
        while True:
            print('1. Añadir/modificar')
            print('2. Buscar')
            print('3. Borrar')
            print('4. Listar')
            print('5. Finalizar programa')

            opcion = input('Introduzca la opción elegida: ')
            if opcion == '1':
                self.añadir_modificar()
            elif opcion == '2':
                self.buscar()
            elif opcion == '3':
                self.borrar()
            elif opcion == '4':
                self.listar()
            elif opcion == '5':
                self.finalizar_programa()

agenda_contactos = Agenda()
agenda_contactos.menu()





