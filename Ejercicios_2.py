import random as r

def adivinar():
    n1 = int(input('Introduce un número: '))
    n2 = int(input('Introduce otro número mayor que n1: '))

    l_inf = n1
    l_sup = n2

    num = r.randint(n1,n2)

    num_adv = int(input('Número adivinar: '))

    intentos = 1

    while True:
        if num_adv < num:
            l_inf = num_adv
            num_adv = int(input('Número adivinar debe estar entre ' + str(l_inf) + ',' + str(l_sup) + ': '))
            intentos += 1
        elif num_adv > num:
            l_sup = num_adv
            num_adv = int(input('Número adivinar debe estar entre ' + str(l_inf) + ',' + str(l_sup) + ': '))
            intentos += 1
        else:
            print('Número adivinado')
            break
    
    return intentos

#print(adivinar())



        