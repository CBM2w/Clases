labr=[" "," ","X","X","X","X","X","X","X","X","X"],["X"," ","X","X","X","X"," "," "," "," "," "],["X"," ","X","X","X","X"," ","X","X","X"," "],["X"," "," "," "," ","X"," "," ","X"," "," "],["X","X","X","X"," ","X","X"," ","X"," ","X"],["X","X","X","X"," "," "," "," ","X"," ","X"],["X","X","X","X","X","X","X","X"," "," ","X"],["X","X","X","X","X","X","X","X"," ","X","X"],["X","X","X","X","X","X","X","X"," "," ","X"],["X","X","X","X","X","X","X","X","X"," "," "]

for e in labr:
    print(e)

def recorrido(laberinto):
    posx = 0
    posy = 0
    visitadas = [(0, 0)]
    resuelto = False
    movido = False

    while not resuelto:
        movimiento = input('Movimiento: ')
        movido = False
        
        for e in laberinto:
            print(e)

        if movimiento == 's':
            if posx+1 <= 9 and not movido:
                if laberinto[posx+1][posy] == ' ': #and (posx+1,posy) not in visitadas:
                    posx += 1
                    visitadas.append((posx, posy))
                    print('Movimiento hacia abajo.')
                    print(posx,posy)
                    movido=True
                else:
                    print('El espacio no está vacío.')
            else:
                print('Out of range.')

        if movimiento == 'd':
            if posy+1 <= 10 and not movido:
                if laberinto[posx][posy+1] == ' ': #and (posx,posy+1) not in visitadas:
                    posy += 1
                    visitadas.append((posx, posy))
                    print('Movimiento hacia la derecha.')
                    print(posx,posy)
                    movido=True
                else:
                    print('El espacio no está vacío.')
            else:
                print('Out of range.')
        
        if movimiento == 'w':
            if posx-1 >= 0 and not movido:
                if laberinto[posx-1][posy] == ' ': #and (posx-1,posy) not in visitadas:
                    posx -= 1
                    visitadas.append((posx, posy))
                    print('Movimiento hacia arriba.')
                    print(posx,posy)
                    movido=True
                else:
                    print('El espacio no está vacío.')
            else:
                print('Out of range.')

        if movimiento == 'a':
            if posy-1 >= 0 and not movido:
                if laberinto[posx][posy-1] == ' ': #and (posx,posy-1) not in visitadas:
                    posy -= 1
                    visitadas.append((posx, posy))
                    print('Movimiento hacia la izquierda.')
                    print(posx,posy)
                    movido=True
                else:
                    print('El espacio no está vacío.')
            else:
                print('Out of range.')
            
        if posx == len(laberinto) - 1 and posy == len(laberinto[0]) - 1:
            break
    
    return visitadas

print(recorrido(labr))