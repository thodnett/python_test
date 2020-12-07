import random

def drawBoard(board):
    """Function that prints the board it is passed.
    """
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def playerLetter():
    """Lets the player pick a letter, returns a list with players letter first.
    """
    letter=""
    while not(letter=='X' or letter =='O'):
        print("Do you want to play with an X or an O?")
        letter = input().upper()
        if letter == 'X':
            return['X','O']
        else:
            return['X', 'O']

def firstPlayer():
    """Randomly choose who goes first.
    """
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'




    
