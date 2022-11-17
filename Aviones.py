NUM_FILAS = 3
NUM_COLUMNAS = 6
LIBRE = True
OCUPADO = not LIBRE

# Crear un avión.
avion = []

for j in range(NUM_FILAS):
    avion.append([])
    for i in range(NUM_COLUMNAS):
        avion[j].append(LIBRE)

for e in avion:
    print(e)
#print(avion)

# Función que devuelva si una posición está libre.
def libre(avion, fila, columna):
    return avion[fila][columna]

# Función reserva.
def reservar(avion, fila, columna):
    avion[fila][columna] = OCUPADO

if libre(avion,2,5):
    reservar(avion,2,5)

#print(avion)

def asiento_libre(avion):
    f = -1
    c = -1

    for fila in avion:
        f += 1
        for asiento in fila:
            c += 1
            if asiento:
                reservar(avion, f, c)
                return f,c

print(asiento_libre(avion))
#print(avion)

def num_asientos_libres(avion):
    libres = 0

    for fila in avion:
        for asiento in fila:
            if asiento:
                libres += 1

    return libres

print(num_asientos_libres(avion))

def avion_lleno(avion):
    # return num_asientos_libres == 0
    if num_asientos_libres(avion) == 0:
        return True
    else:
        return False

def avion_vacio(avion):
    return num_asientos_libres == NUM_FILAS * NUM_COLUMNAS

def ventanilla(avion,columna):
    return columna == 0 or columna == 5

def recaudacion(avion, precio_ventanilla, precio_pasillo):
    rec = 0

    for fila in range(len(avion)):
        for columna in range(len(avion[fila])):
            if not libre(avion,fila,columna):
                if ventanilla(avion,columna):
                    rec += precio_ventanilla
                else:
                    rec += precio_pasillo

    return rec

print(avion)
print(recaudacion(avion,300,400))