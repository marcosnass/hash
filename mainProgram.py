from time import sleep
import os
import random

matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
playAgain = 'S'
player = 0# 0 CPU  1 PESSOA
plays = 0
maxPlays = 9
win = 'n'


def writeFeddBack():
    global plays
    os.system('cls')
    print('    0   1   2')
    print(f'0:   {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}')
    print('    -----------')
    print(f'1:   {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}')
    print('    -----------')
    print(f'2:   {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}')
    print(f'Jogada: {plays}')


def playGame():
    global plays
    global player
    global maxPlays
    if player == 0 and plays < maxPlays:
        try:
            lin = int(input('Linha: '))
            col = int(input('Coluna: '))
            while matrix[lin][col] != ' ':
                lin = int(input('Linha: '))
                col = int(input('Coluna: '))
            matrix[lin][col] = 'X'
            player = 1
            plays += 1
        except:
            print('Linha e/ou coluna inválida')


def playCpu():
    global plays
    global player
    global maxPlays
    print('Cpu está jogando...')
    sleep(1)
    if player == 1 and plays < maxPlays:
        lin = random.randrange(0, 3)
        col = random.randrange(0, 3)
        while matrix[lin][col] != ' ':
            lin = random.randrange(0, 3)
            col = random.randrange(0, 3)
        matrix[lin][col] = 'O'
        player = 0
        plays += 1


def checkWin():
    global matrix
    win = 'n'
    symbols = ['X', 'O']
    #verificar linhas
    for s in symbols:
        win = 'n'
        il = ic = 0
        while il < 3:
            sum = 0
            ic = 0
            while ic < 3:
                if matrix[il][ic] == s:
                    sum += 1
                ic += 1
            if sum == 3:
                win = s
                break
            il += 1
        if win != 'n':
            break
    # verificar colunas
        il = ic = 0
        while ic < 3:
            sum = 0
            il = 0
            while il < 3:
                if matrix[il][ic] == s:
                    sum += 1
                il += 1
            if sum == 3:
                win = s
                break
            ic += 1
        if win != 'n':
            break
    #verifica diagonal 1
        sum = 0
        idiag = 0
        while idiag < 3:
            if matrix[idiag][idiag] == s:
                sum += 1
            idiag += 1
        if sum == 3:
            win = s
            break
    #verifica diagonal 2
        sum = 0
        idiagl = 0
        idiagc = 2
        while idiagc >= 0:
            if matrix[idiagl][idiagc] == s:
                sum += 1
            idiagl += 1
            idiagc -= 1
        if sum == 3:
            win = s
            break
    return win


def reset():
    global matrix
    global player
    global plays
    global maxPlays
    global win
    matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player = 0  # 0 CPU  1 PESSOA
    plays = 0
    maxPlays = 9
    win = 'n'

while playAgain == 'S':
    while True:
        writeFeddBack()
        playGame()
        playCpu()
        #writeFeddBack()
        win = checkWin()
        if win != 'n' or plays >= maxPlays:
            break
    if win == 'X' or win == 'O':
        print(f'O jogador {win} venceu')
        writeFeddBack()
    else:
        print('Empate')
        writeFeddBack()
    playAgain = str(input('Jogar novamente? [s/n]: ')).upper()[0]
    reset()
print('FIM DO JOGO')