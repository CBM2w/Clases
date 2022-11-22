labr=[" "," ","X","X","X","X","X","X","X","X","X"],["X"," ","X","X","X","X"," "," "," "," ","X"],["X"," ","X","X","X","X"," ","X","X"," ","X"],["X"," "," "," "," ","X"," "," ","X"," ","X"],["X","X","X","X"," ","X","X"," ","X"," ","X"],["X","X","X","X"," "," "," "," ","X"," ","X"],["X","X","X","X","X","X","X","X"," "," ","X"],["X","X","X","X","X","X","X","X"," ","X","X"],["X","X","X","X","X","X","X","X"," "," ","X"],["X","X","X","X","X","X","X","X","X"," "," "]

for e in labr:
    print(e)

def recorrido(laberinto):
    posx = 0
    posy = 0
    resuelto = False

    while not resuelto:
        if laberinto[posx][posy+1] == ' ':
            posy += 1
            print('Movimiento hacia la derecha.')
            print(posx,posy)
        
        elif laberinto[posx+1][posy] == ' ':
            posx += 1
            print('Movimiento hacia abajo.')
            print(posx,posy)

        elif laberinto[posx][posy-1] == ' ':
            posy -= 1
            print('Movimiento hacia la izquierda.')
            print(posx,posy)
        
        elif laberinto[posx-1][posy] == ' ':
            posx -= 1
            print('Movimiento hacia arriba.')
            print(posx,posy)

        if posx == len(laberinto) and posy == len(laberinto[0]):
            break

recorrido(labr)
