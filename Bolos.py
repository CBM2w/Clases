import random


class Partida():

    def __init__(self):
        self.partida = []

    def tirar(self):
        bolos = 10
        tirada = []
        n_1 = random.randint(0,10)
        n_2 = input('Introduce un número del 0 al 10: ')
        media = (n_1 + int(n_2)) // 2
        tirada.append(media)
        bolos = bolos - media

        if bolos == 0:
            print('PLENO')
        else:
            n_1_2 = random.randint(0,bolos)
            n_2_2 = input('Introduce un número del 0 al ' + str(bolos) + ': ')
            media_2 = (n_1_2 + int(n_2_2)) // 2
            tirada.append(media_2)
            
        return tirada

    def puntuacion(self,tirada):
        puntuacion = 0

        for i in tirada:
            puntuacion += i
        
        return puntuacion

    def menu(self):
        self.partida.append({})
        self.partida.append({})

        jugador_1 = input('Nombre jugador 1: ')
        jugador_2 = input('Nombre jugador 2: ')

        puntos_j1 = 0
        puntos_j2 = 0

        for t in range(0,10):
            turno_j1 = self.tirar()
            self.partida[0]['Turno ' + str(t)] = turno_j1
            #print('Turno ' + str(t) + ': ' + for i in turno_j1[i])

            turno_j2 = self.tirar()
            self.partida[1]['Turno ' + str(t)] = turno_j2
            #print('Turno ' + str(t) + ': ' + turno_j2)

            puntos_j1 += self.puntuacion(turno_j1)
            puntos_j2 += self.puntuacion(turno_j2)

        print(puntos_j1)
        print(puntos_j2)

        return self.partida

part = Partida()
print(part.menu())