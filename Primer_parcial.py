ALUMNO = 0; ASIGNATURA = 1; PRACTICA = 2; NOTAS = 3

notas = [
    ['Brutus', 'Algebra', 'mal', [3.2, 5.1, 0.8]],
    ['Brutus', 'Discreta', 'regular', [5.2, 3.7, 5.0]],
    ['Brutus', 'Programacion', 'mal', [0.5, 3.2, 4.0]],
    ['Flavia', 'Algebra', 'bien', [7.2, 5.6, 7.1]],
    ['Flavia', 'Discreta', 'regular', [4.9, 8.5, 5.2]],
    ['Flavia', 'Programacion', 'bien', [9.5, 8.3, 10.0]],
    ['Jovina', 'Programacion', 'bien', [7.4, 9.3, 8.2]],
    ['Secundus', 'Algebra', 'mal', [3.1, 5.5, 6.1]],
    ['Secundus', 'Discreta', 'bien', [7.3, 6.7, 8.5]],
    ['Secundus', 'Programacion', 'mal', [4.5, 3.3, 4.2]],
    ['Sextus', 'Algebra', 'bien', [9.3, 9.8, 9.9]],
    ['Sextus', 'Programacion', 'bien', [8.9, 9.3, 8.9]]    
]

# 1.
def alumnos_asignaturas():
    alumnos = set()
    asignaturas = set()

    for e in notas:
        alumnos.add(e[ALUMNO])
        asignaturas.add(e[ASIGNATURA])

    return alumnos,asignaturas

# 2.
medias = []

for e in notas:
    media = (e[NOTAS][0] + e[NOTAS][1] + e[NOTAS][2]) / 3
    medias.append(media)

def sobresaliente_bien():
    resultado = set()

    for e in range(len(notas)):
        if notas[e][PRACTICA] == 'bien' and medias[e] >= 9:
            resultado.add(notas[e][ALUMNO])

    return resultado


DIRECTOR = 0; VALORACION = 1; ANIO = 2; ACTORES = 3

peliculas = {
    'Dune' : ('Denis Villeneuve', 8.3, 2021, 
              {'Jason Momoa', 'Josh Brolin', 'Tomothée Chalamet'}),
    'Aquaman' : ('James Wan', 6.9, 2018,
              {'Jason Momoa', 'Amber Heard', 'Willem Dafoe'}),
    'Fast & Fourious 7' : ('James Wan', 7.1, 2015,
              {'Vin Diesel', 'Paul Walker', 'Dwayne Johnson'}),
    'Ridick' : ('David Twohy', 6.4, 2013,
              {'Vin Diesel', 'Karl Urban'}),
    'La chica danesa' : ('Tom Hooper', 7.1, 2015,
              {'Eddie Redmayne', 'Alicia Vikander', 'Amber Heard'}),
    'La teoría del todo' : ('James Marsh', 7.7, 2014,
              {'Eddie Redmayne', 'Felicity Jones'}),
    'Avatar' : ('James Cameron', 7.8, 2009,
               {'Sam Worthington', 'Zoe Saldana', 'Sigourney Weaver'})
}

# 3. 
nombres_peliculas = []

for nombre in peliculas:
    nombres_peliculas.append(nombre)

nombres_peliculas_ordenadas = nombres_peliculas.sort()

# 4. 
def pelis_2015_7():
    resultado = []

    for nombre in peliculas:
        if peliculas[nombre][ANIO] >= 2015 and peliculas[nombre][VALORACION] >= 7:
            resultado.append((nombre,peliculas[nombre]))

    return resultado

# 5.
actores = set()

for nombre in peliculas:
    actores = actores | peliculas[nombre][ACTORES]

def valoracion_maxima(actor):
    val_max = -1

    for nombre in peliculas:
        valoracion = peliculas[nombre][VALORACION]
        if actor in actores and valoracion > val_max:
            val_max = valoracion
    
    return val_max

resultado = []

for actor in actores:
    valoracion_max = valoracion_maxima(actor)
    resultado.append((actor,valoracion_max))

print(resultado)
