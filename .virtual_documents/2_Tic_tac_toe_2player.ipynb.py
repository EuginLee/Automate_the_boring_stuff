# Tic-tac-toe for 2 player - turn based
# Skills: using dictionary data structure, and practice capturing errors

turn = 'X'

# list of possible inputs
listed = ['top-L', 'top-M', 'top-R', 'mid-L', 'mid-M','mid-R','low-L','low-M','low-R']
 

# original gameboard, using dictionary 
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

#print out the updated game board
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


#criteria for winning, the x, o must form a line, and it cannot be empty    
def testForAWin(board):
    won = False
 
    if((board['top-L'] == board['top-M'] == board['top-R']) and board['top-L'] get_ipython().getoutput("= ' '):")
        won = True
    elif(board['mid-L'] == board['mid-M'] == board['mid-R'] and board['mid-L'] get_ipython().getoutput("= ' '):")
        won = True
    elif(board['low-L'] == board['low-M'] == board['low-R'] and board['low-L'] get_ipython().getoutput("= ' '):")
        won = True 
        
    elif(board['top-L'] == board['mid-L'] == board['low-L'] and board['top-L'] get_ipython().getoutput("= ' '):")
        won = True
    elif(board['top-M'] == board['mid-M'] == board['low-M'] and board['top-M'] get_ipython().getoutput("= ' '):")
        won = True
    elif(board['top-R'] == board['mid-R'] == board['low-R'] and board['top-R'] get_ipython().getoutput("= ' '):")
        won = True        
        
    elif(board['top-L'] == board['mid-M'] == board['low-R'] and board['top-L'] get_ipython().getoutput("= ' '):")
        won = True
    elif(board['top-R'] == board['mid-M'] == board['low-L'] and board['top-R'] get_ipython().getoutput("= ' '):")
        won = True        
               
    return won

 
for i in range(9):
    printBoard(theBoard)
    print('Turn for :' + turn + ' Choose a space : ')
    
    move = input()

    # error messsage if user entered 
    while not move in listed:
        print('Oops! that was not a valid cell. Try again.')
        print()
        print('top-L | top-M | top-R') 
        print('mid-L | mid-M | mid-R')
        print('low-L | low-M | low-R')
        move = input()
    
    # error message if the cell is not empty
    while not theBoard[move]== ' ':
        print('Do not try to steal a place! ')
        move = input()
 
    theBoard[move] = turn
    won = testForAWin(theBoard)
    
    if won:
        print(turn + ' wins the gameget_ipython().getoutput("')")
        break
    elif turn == 'X':
        turn = '0'
    else:
        turn = 'X'
printBoard(theBoard)



