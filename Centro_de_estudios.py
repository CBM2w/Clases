# alumno, asignatura, práctica, vector de 3 notas de teoría
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

# Crear dos conjuntos, uno con los alumnos y otro con las asignaturas.
alumnos = set()
asignaturas = set()

for i in notas:
    alumnos.add(i[ALUMNO])

for i in notas:
    asignaturas.add(i[ASIGNATURA])

print(alumnos)
print(asignaturas)
print()

# 1. Nombre de los alumnos matriculados en cada asignatura (ordenado alfabéticamente por asignaturas).
alumnos_en_asignatura = {}

for e in notas:
    if e[ASIGNATURA] in alumnos_en_asignatura:
        alumnos_en_asignatura[e[ASIGNATURA]] += e[ALUMNO]+" "  
    else:
        alumnos_en_asignatura[e[ASIGNATURA]] = e[ALUMNO]+" "

print(alumnos_en_asignatura)
print()

# 2. Nombre de las asignaturas en las que se ha matriculado cada alumno.
asignaturas_por_alumno = {}

for e in notas:
    if e[ALUMNO] in asignaturas_por_alumno:
        asignaturas_por_alumno[e[ALUMNO]] += e[ASIGNATURA]  # DUDA
    else:
        asignaturas_por_alumno[e[ALUMNO]] = e[ASIGNATURA]

print(asignaturas_por_alumno)
print()

# 3. Lista de aprobados en cada asignatura.
aprobados = []
medias = []
for e in notas:
    medias.append((e[NOTAS][0] + e[NOTAS][1] + e[NOTAS][2]) / 3)

print(medias)

for asignatura in asignaturas:
    aprobados_en_asignatura = set()
    for i in range(len(notas)):
        if notas[i][ASIGNATURA] == asignatura and medias[i] >= 5.0:
            aprobados_en_asignatura.add(notas[i][ALUMNO])

    aprobados.append((asignatura,aprobados_en_asignatura))

print(aprobados)
print()
# 4. Listado de las 5 tuplas (alumno, asignatura, nota) con mayores notas.
medias_ordenadas = medias.copy()
medias_ordenadas.sort(reverse = True)
cinco_mejores = medias_ordenadas[:5]
print(cinco_mejores)

top_5 = []

for i in range(len(notas)):
    if medias[i] in cinco_mejores:
        top_5.append((notas[i][ALUMNO],notas[i][ASIGNATURA],medias[i]))

print(top_5)
print()
# 5. Alumnos que, en al menos una asignatura, han sacado un 'bien' en la práctica y sobresaliente en la teoría.
almunos_bien_sobresaliente = set()

for i in range(len(notas)):
    if notas[i][PRACTICA] == 'bien' and medias[i] >= 9.0:
        almunos_bien_sobresaliente.add(notas[i][ALUMNO])

print(almunos_bien_sobresaliente)
print()
