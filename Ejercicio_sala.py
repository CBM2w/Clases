NUM_COLUMNAS = 10; NUM_FILAS = 12; LIBRE = True; OCUPADO = not LIBRE
CARO = 2; NORMAL = 1; BARATO = 0
precio_butaca = [30, 50, 90]

sala_ocupación = []

for i in range(NUM_FILAS):
    sala_ocupación.append([])
    sala_ocupación[i] = [LIBRE for j in range(NUM_COLUMNAS)]

#print(sala_ocupación)
#print()

sala_tipos = []

for i in range(NUM_FILAS):
    sala_tipos.append([])
    if i <= 3:
        sala_tipos[i] = [CARO for j in range(NUM_COLUMNAS)]
    elif 4 <= i <= 7:
        sala_tipos[i] = [NORMAL for j in range(NUM_COLUMNAS)]
    else:
        sala_tipos[i] = [BARATO for j in range(NUM_COLUMNAS)]

#print(sala_tipos)
#print()

for i in range(NUM_FILAS):
    if i < 3:
        if i == 0:
            for j in range(-2, 2):
                sala_tipos[i][j] = BARATO
        elif i == 1:
            for k in range(-2, 2):
                sala_tipos[i][k] = NORMAL
            for l in range(-1, 1):
                sala_tipos[i][l] = BARATO 
        else:
            for j in range(-1, 1):
                sala_tipos[i][j] = NORMAL   

#print(sala_tipos)
#print()

def imprime_sala(sala):

    for elemento in sala:
        print(elemento)

#imprime_sala(sala_tipos)

def libre(fila, columna, sala):
    return sala[fila][columna]

def precio(fila, columna, sala):
    return precio_butaca[sala[fila][columna]]

def libera(fila, columna, sala):
    sala[fila][columna] = LIBRE

def ocupa(fila, columna, sala):
    sala[fila][columna] = OCUPADO

def butacas_libres(sala):
    butacas = 0

    for i in range(NUM_FILAS):
        for j in range(NUM_COLUMNAS):
            if libre(i, j, sala):
                butacas += 1

    return butacas

def lleno(sala):
    return butacas_libres(sala) == 0

def vacio(sala):
    return butacas_libres(sala) == NUM_FILAS * NUM_COLUMNAS

def primera_libre(tipo):

    for i in range(NUM_FILAS):
        for j in range(NUM_COLUMNAS):
            if libre(i,j,sala_ocupación) and sala_tipos[i][j]==tipo:
                return i,j
                
#print(primera_libre(2))

def dos_asientos(tipo):

     for i in range(NUM_FILAS):
        for j in range(NUM_COLUMNAS):
            if j+1 < NUM_COLUMNAS:
                if libre(i,j,sala_ocupación) and libre(i,j+1,sala_ocupación):
                    if sala_tipos[i][j]==tipo and sala_tipos[i][j+1]==tipo:
                        return (i,j), (i,j+1)
            else:
                print('Fila llena')

#print(dos_asientos(2))

def ocupar_dos_asientos(tipo):
    asientos = dos_asientos(tipo)

    for i in range(len(asientos)):
        ocupa(asientos[i][0], asientos[i][1], sala_ocupación)
    
def recaudacion():
    dinero = 0

    for i in range(NUM_FILAS):
        for j in range(NUM_COLUMNAS):
            if sala_tipos[i][j] == 0:
                dinero += precio_butaca[0]
            elif sala_tipos[i][j] == 1:
                dinero += precio_butaca[1]
            else:
                dinero += precio_butaca[2]

    return dinero