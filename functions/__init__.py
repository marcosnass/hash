from time import sleep
import os
import random

def writeFeddBack(matrix):
    os.system('cls')
    jogadas = 0
    print('    0   1   2')
    print(f'0:   {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}')
    print('    -----------')
    print(f'1:   {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}')
    print('    -----------')
    print(f'2:   {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}')
    print(f'Jogadas: {jogadas}')


def verification(matrix, lin, col):
    print(matrix[lin][col])

def playGame(matrix, player, plays, maxPlays):
    if player == 0 and plays < maxPlays:
        lin = int(input('Linha: '))
        col = int(input('Coluna: '))
        while matrix[lin][col] != ' ':
            lin = int(input('Linha: '))
            col = int(input('Coluna: '))
        try:
            while matrix[lin][col] != ' ':
                lin = int(input('Linha: '))
                col = int(input('Coluna: '))
            matrix[lin][col] = 'X'
            player = 1
            plays += 1
        except:
            print('Linha e/ou coluna inválida')


def playCpu(matrix, player, plays, maxPlays):
    if player == 0 and plays < maxPlays:
        lin = int(input('Linha: '))
        col = int(input('Coluna: '))
        while matrix[lin][col] != ' ':
            lin = random.randrange(0, 3)
            col = random.randrange(0, 3)
            while matrix[lin][col] != ' ':
                lin = random.randrange(0, 3)
                col = random.randrange(0, 3)
            matrix[lin][col] = 'O'
            player = 2
            plays += 1
