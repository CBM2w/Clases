class Triangulo():

    def __init__(self):
        self.lado1 = int(input('Introduce el lado 1: '))
        self.lado2 = int(input('Introduce el lado 2: '))
        self.lado3 = int(input('Introduce el lado 3: '))

    def __str__(self):
        return 'Lado 1: ' + str(self.lado1) + '\n Lado 2: ' + str(self.lado2) + '\n Lado 3: ' + str(self.lado3)

    def mayor_lado(self):
        lados = [self.lado1, self.lado2, self.lado3]
        lados.sort(reverse = True)
        return lados[0]

    def tipo_triangulo(self):
        
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print('Triángulo equilátero')
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:
            print('Triángulo escaleno')
        else:
            print('Triángulo isósceles')


triangulo = Triangulo()
print(triangulo.mayor_lado())
triangulo.tipo_triangulo()