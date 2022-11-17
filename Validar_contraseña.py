def validar():
    contraseña = input('Introduce una contraseña: ')

    numeros = ['0','1','2','3','4','5','6','7','8','9']

    str = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    letras = []
    letras_min = []
    for l in str:
        letras.append(l)
        letras_min.append(l.lower())

    caracteres_especiales = ['.','_']
    c=True
    while c:
        if len(contraseña) < 8:
            print('La contraseña elegida no es segura.')
            contraseña = input('Introduce una contraseña: ')
        else:
            for e in contraseña:
                if e not in numeros and e not in letras and e not in letras_min and e not in caracteres_especiales:
                    print('La contraseña no es válida')
                    contraseña = input('Introduce una contraseña: ')
                else:
                    c_may = 0
                    c_min = 0
                    c_num = 0
                    c_car = 0
                    if e in letras:
                        c_may += 1
                    elif e in letras_min:
                        c_min += 1
                    elif e in numeros:
                        c_num += 1
                    elif e in caracteres_especiales:
                        c_car += 1

            if c_may > 0 and c_min > 0 and c_num > 0 and c_car > 0:
                print('Contraseña válida')
                c=False
            else:
                print('La contraseña no es válida')
                contraseña = input('Introduce una contraseña: ')
                
    return contraseña