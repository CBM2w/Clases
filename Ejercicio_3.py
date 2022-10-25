from symbol import break_stmt


def validar():
    nombre_usuario = input('Introduce nombre de usuario: ')

    numeros = ['0','1','2','3','4','5','6','7','8','9']

    str = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    letras = []
    for l in str:
        letras.append(l)

    while True:
        if len(nombre_usuario) < 6 or len(nombre_usuario) > 12:
            print('El nombre debe tener entre 6 y 12 caracteres.')
            nombre_usuario = input('Introduce nombre de usuario: ')
        else:
            for e in nombre_usuario:
                if e.upper() not in letras and e not in numeros:
                    print('Los caracteres solo pueden ser números o letras')
                    nombre_usuario = input('Introduce nombre de usuario: ')
                else:
                    return nombre_usuario 
                    break

print(validar())

