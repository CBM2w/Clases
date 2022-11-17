class MatriculaErronea(Exception):

    def __init__(self,matricula):
        super().__init__('Matricula errónea')
        self.matricula = matricula


class Automovil():
    def comprobar(self,matricula):
        ret=True
        if len(matricula) != 7:
            ret=False
        else:
            numeros = ['0','1','2','3','4','5','6','7','8','9']
            str = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
            letras = []
            for l in str:
                letras.append(l)

            condicion = True
            for e in range(0,4):
                if matricula[e] not in numeros:
                    condicion = False
                    ret=False
            if condicion:
                for e in range(4,7):
                    if matricula[e] not in letras:
                        ret=False
        return ret

    def __init__(self, matricula):
        if self.comprobar(matricula):
            self.matricula = matricula
        else:
            raise MatriculaErronea(matricula)
    
    def get_matricula(self):
        return self.matricula
    
    def set_matricula(self, matricula):
        self.matricula = matricula

    def __str__(self):
        return self.matricula

coche = Automovil('6754D8G')   
print(coche)              
