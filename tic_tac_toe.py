import turtle
import random
t = turtle.Turtle()
s = turtle.Screen()

CELL_SIZE = 150 #this number may be adjusted

board = ['-','-','-','-','-','-','-','-','-']

VERT_LEFT = ((-CELL_SIZE/2, CELL_SIZE*3/2),(-CELL_SIZE/2, -CELL_SIZE*3/2))
VERT_RIGHT = ((CELL_SIZE/2, CELL_SIZE*3/2),(CELL_SIZE/2, -CELL_SIZE*3/2))
HORZ_TOP = ((-CELL_SIZE*3/2, CELL_SIZE/2),(CELL_SIZE*3/2, CELL_SIZE/2))
HORZ_BOTTOM = ((-CELL_SIZE*3/2, -CELL_SIZE/2),(CELL_SIZE*3/2, -CELL_SIZE/2))

def drawLine(t, fromPoint, toPoint):
    t.up()
    t.goto(fromPoint)
    t.down()
    t.goto(toPoint)

def drawGrid(t):
    initTurtle(t, 'drawGrid')
    drawLine(t, VERT_LEFT[0], VERT_LEFT[1])
    drawLine(t, VERT_RIGHT[0], VERT_RIGHT[1])
    drawLine(t, HORZ_TOP[0], HORZ_TOP[1])
    drawLine(t, HORZ_BOTTOM[0], HORZ_BOTTOM[1])



#part A
CELL_CENTERS = ((-CELL_SIZE, CELL_SIZE),(0, CELL_SIZE),(CELL_SIZE, CELL_SIZE),
                (-CELL_SIZE, 0),(0, 0),(CELL_SIZE, 0),(-CELL_SIZE, -CELL_SIZE),
                (0, -CELL_SIZE),(CELL_SIZE, -CELL_SIZE))

TRIPLETS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # 3 horizontal
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # 3 vertical
    (0, 4, 8), (2, 4, 6)              # 2 diagonal
    )

NUM_TRIPLETS = len(TRIPLETS)


#part B
def drawLineMidpoint (t, length):
    '''t is a turtle. length is an int. Use t to draw a line
    of the specified length extending equally in opposite direction'''
    t.up()
    t.bk(length/2)
    t.down()
    t.fd(length)
    t.up()
    t.bk(length/2)



#part C
def drawX(t, cell):
    '''use turtle t to draw two lines of X'''
    initTurtle(t, 'drawX')
    t.up()
    midpoint = CELL_CENTERS[cell]
    t.goto(midpoint[0], midpoint[1])
    t.setheading(135)
    t.down()
    drawLineMidpoint(t, CELL_SIZE*.8)

    t.setheading(45)
    drawLineMidpoint(t, CELL_SIZE*.8)



#part D
def testX(t):
    for i in range(9):
        drawX(t, CELL_CENTERS[i], CELL_SIZE)


#part A
def concentricCircle(t, r):
    t.up()
    t.forward(r)
    t.left(90)
    t.down()
    t.circle(r)
    t.right(90)
    t.up()
    t.back(r)
    
#part B
def drawO(t, cell):
    '''create a trutle to draw a circle representing O
    in specified cell of TTT grid'''
    initTurtle(t, 'drawO')
    r = CELL_SIZE/3.5
    t.up()
    t.goto(CELL_CENTERS[cell])
    t.left(90)
    concentricCircle(t, r)
    
#part C
def testO():
    for i in range(9):
        drawO(CELL_CENTERS[i],45)


#part A
def labelCell(t, cellNumber):
    '''use turtle t to write number of a cell at mdpt'''
    initTurtle(t, 'labelCell')
    t.up()
    t.goto(CELL_CENTERS[cellNumber])
    t.write(cellNumber, font=('Arial',15,'normal'))

#part B
def labelCells(t):
    '''function calls labelCell repeatedly to write
    the cell number in each cell'''
    for i in range(9):
        labelCell(t, i)

#part C
#labelCells()

def initTurtle(t, use):
    if use == 'drawGrid':
        t.color('green')
        t.width(10)
        t.speed(50)
    elif use == 'drawX':
        t.color('cyan')
        t.width(10)
        t.speed(50)
    elif use == 'drawO':
        t.color('violet')
        t.width(10)
        t.speed(50)
    elif use == 'labelCells':
        t.color('black')
        t.width(5)
        t.speed(50)
    elif use == 'drawWinLine':
        t.color('pink')
        t.width(7)
        t.speed(50)
    elif use == 'showExitMessage':
        t.color('lime')
        t.width(7)
        t.speed(50)



def getMove(s, player, board):
    s = turtle.Screen()
    prompt = player + ',pick a cell to move'
    while True:
        move = s.numinput("", prompt, default=None, minval = 0, maxval = 8)
        if move is None:
            prompt = 'You must choose a valid move'
            continue
        intMove = int(move) #change float to integer
        if board[intMove] == '-':
            return intMove
        prompt = 'Not a valid move. Try again.'

def playAgainPrompt():
    s = turtle.Screen()
    prompt = 'Do you want to play again [0:Yes 1:No]?'
    answer = s.numinput("", prompt, default=None, minval = 0, maxval = 1)
    return answer

#playTicTacToe()


def testGetMove(iterations):
    import random
    s = turtle.Screen()

    for i in range(iterations):
        t = turtle.Turtle()
        board = ['-','-','-','-','-','-','-','-','-'] #9 empty cells

        drawGrid(t)
        labelCells(t)

        # pick random moves
        numMoves = random.randint(0,8)
        for i in range(numMoves):
            if i%2 == 0:
                randmove = 'X'
            else:
                randmove = 'O'
            board[i] = randmove
        random.shuffle(board)

        #display game
        drawGrid(t)
        for cell in range(len(board)):
            if board[cell] == 'X':
                drawX(t, cell)
            elif board[cell] == 'O':
                drawO(t, cell)

        #call getMove
        if numMoves%2 == 0:
            player = 'X'
        else:
            player = 'O'
        move = getMove(s, player, board)

        #validate move with 2 tests
        if move not in range(9):
            print('FAIL', 'must be an int in 0-8')
            break
        if board[move] != '-':
            print('FAIL', 'must move in an empty cell')
            break
        print('PASS')
        s.clear()
        t = turtle.Turtle()

#iterations = 10
#testGetMove(iterations)



def isWin(t, board, player):
    '''return true if player has three in a row, otherwise false'''
    t = turtle.Turtle()
    for triplet in TRIPLETS:  #detects winning triplets
        a, b, c = board[triplet[0]], board[triplet[1]], board[triplet[2]]
        if a == b == c == player:
            drawWinLine(t, triplet)
            return True
    return False   



def testIsWin(iterations):
    import random
    import turtle
    s = turtle.Screen()

    for i in range(iterations):
        t = turtle.Turtle()
        t.hideturtle()
        board = ['-', '-', '-', '-', '-', '-', '-', '-', '-'] # 9 empty cells
        empty = [0, 1, 2, 3, 4, 5, 6, 7, 8] # indices of empty cells
        drawGrid(t)

        # make random moves until board is full or a win
        player, nextPlayer = 'X', 'O'
        while '-' in board:
            # make a move
            move = random.choice(empty)
            empty.remove(move)
            board[move] = player
            if player == 'X':
                drawX(t, move)
            else:
                drawO(t, move)

            # see if the move resulted in a win
            win = False
            for triplet in TRIPLETS:
                a, b, c = board[triplet[0]], board[triplet[1]], board[triplet[2]]
                if a == b == c == player:
                    win = True
        
            # end test on FAIL
            if win != isWin(t, board, player):
                print('FAIL', board, 'win =', win)
                return   # end test on FAIL

            # end game on WIN
            if win == True:
                break # go to next game
            
            player, nextPlayer = nextPlayer, player # next move

        # next game
        if win == True:
            print('PASS', board, 'win')
        else:
            print('PASS', board, 'draw')
        s.clear()
        t = turtle.Turtle()
        
#------------------------------------------------------------------------

def isDraw(board):
    ''' A TRIPLET is blocked if it contains at least 1 cell of each player.
    If all TRIPLETS are blocked return True, else return False'''
    for triplet in TRIPLETS:
        a, b, c = board[triplet[0]], board[triplet[1]], board[triplet[2]]
        if not ('X' in (a,b,c) and 'O' in (a,b,c)):
            return False
    return True


def testIsDrawGame():
    ''' Generate a TTT game by choosing each move at random from among
    the empty cells. Terminate when the game is won or drawn, where drawn
    is defined as a board in which all TRIPLES have at least one X and 
    one O. (A different definition might detect additional draws.)

    After each move compare the draw status with isDraw. Print
    PASS if they agree, FAIL otherwise. 
    '''
    board = ['-','-','-','-','-','-','-','-','-'] # 9 empty cells
    empty = [0, 1, 2, 3, 4, 5, 6, 7, 8] # indices of empty cells
    winner = None
    player, nextPlayer = 'X', 'O'

    # the game loop
    moveCount = 0
    while '-' in board:
        # make a move
        move = random.choice(empty)
        empty.remove(move)
        board[move] = player
        moveCount += 1

        # check for win
        for triplet in TRIPLETS:
            a, b, c = board[triplet[0]], board[triplet[1]], board[triplet[2]]
            if a == b == c == player:
                winner = player
                break

        # check for draw
        blocked = 0
        for triplet in TRIPLETS:
            a, b, c = board[triplet[0]], board[triplet[1]], board[triplet[2]]
            if 'X' in (a,b,c) and 'O' in (a,b,c):
                blocked += 1
            
            testDraw = (blocked == NUM_TRIPLETS)
            drawn = isDraw(board)
        
        # game is won
        if winner == 'X' or winner == 'O':
            print('PASS', board, 'moves', moveCount, ', testDraw', testDraw, ', isDraw', drawn, ', winner', winner)
            break

        if testDraw == drawn == True:
            print('PASS', board, 'moves', moveCount, ', testDraw', testDraw, ', isDraw', drawn, ', winner', winner)
            break
        elif testDraw != drawn:
            print('FAIL', board, 'moves', moveCount, ', testDraw', testDraw, ', isDraw', drawn, ', winner', winner)
            return
        player, nextPlayer = nextPlayer, player

def testIsDrawGames(iterations):
    print('\ntesting isDraw')
    for i in range(iterations):
        print(i, end=' ')
        testIsDrawGame()


#---------------------------------------------------------------------------

#-----------------------------------------------------------------------------

def drawWinLine(t, triplet):
    '''Draw a line connecting the centers of the first and third cells
    of a winning triplet.'''
    
    initTurtle(t, 'drawWinLine')
    startCell = CELL_CENTERS[triplet[0]]
    endCell = CELL_CENTERS[triplet[2]]
    drawLine(t, startCell, endCell)


def testDrawWinLine():
    '''Test the function drawWinLine by drawing a TTT grid then drawing
    all possible win lines on it'''
    t = turtle.Turtle()
    s = turtle.Screen()
    drawGrid(t)
    for triplet in TRIPLETS:
        drawWinLine(t, triplet)
    s.exitonclick()



def showExitMessage(t, winner):
    '''The game is over; write outcome message'''
    initTurtle(t, 'showExitMessage')
    t.up()
    t.goto(CELL_CENTERS[6])
    t.setheading(270)
    t.forward(30)
    if winner == None:
        outcome = 'DRAW!'
    else:
        outcome = winner+ ' WINS!'
    t.up()
    t.goto(0, -CELL_SIZE*2.3)
    t.write(outcome, align='center', font=('Arial', 30, 'bold'))

    t.up()
    t.goto(0, -CELL_SIZE*2.5)
    t.down()
        
    
    


def playTicTacToe():
    '''initialize board and game, alternate play between
    X and O until board is full, check for win after each move
    and end in case of a win.'''

    #create screen and turtle
    s = turtle.Screen()
    t = turtle.Turtle()
    
    # draw the board
    drawGrid(t)
    labelCells(t)

    # initialize the game
    board = ['-','-','-','-','-','-','-','-','-'] #9 empty cells
    winner = None 
    player, nextPlayer = 'X', 'O' #x always goes first
    
  
    while '-' in board:
        move = getMove(s, player, board) #get the next move
        board[move] = player    #update the board
        if player == 'X':       #determine who's playing and draw X or O
            drawX(t, move)
        else:
            drawO(t, move)
        if isWin(t, board, player):  #check for a win
            winner = player
            break
        if isDraw(board):
            break
        player, nextPlayer = nextPlayer, player #switch variables to make nextplayer the current variable

    showExitMessage(t, winner)
    answer = playAgainPrompt()
    if answer == 0:
        s.clear()
        playTicTacToe()
    else:
        s.exitonclick()

playTicTacToe()
