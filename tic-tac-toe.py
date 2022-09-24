#This is the Tic-Tac-Toe Assignment by Emory Hubbard

def printBoard(squares):
    print(
        f"{squares['1']}|{squares['2']}|{squares['3']}\n" +
        "-+-+-\n" +
        f"{squares['4']}|{squares['5']}|{squares['6']}\n" +
        "-+-+-\n" +
        f"{squares['7']}|{squares['8']}|{squares['9']}")

def playerHasWon(player, squares):
    if playerHasWonARow(player, squares):
        return True
    if playerHasWonAColumn(player, squares):
        return True
    if playerHasWonADiagonal(player, squares):
        return True
    return False

def playerHasWonARow(player, squares):
    if squares['1']==player and squares['2']==player and squares['3']==player:
        return True
    if squares['4']==player and squares['5']==player and squares['6']==player:
        return True
    if squares['7']==player and squares['8']==player and squares['9']==player:
        return True
    return False

def playerHasWonAColumn(player, squares):
    if squares['1']==player and squares['4']==player and squares['7']==player:
        return True
    if squares['2']==player and squares['5']==player and squares['8']==player:
        return True
    if squares['3']==player and squares['6']==player and squares['9']==player:
        return True
    return False

def playerHasWonADiagonal(player, squares):
    if squares['1']==player and squares['5']==player and squares['9']==player:
        return True
    if squares['7']==player and squares['5']==player and squares['3']==player:
        return True
    return False

squares = {"1": "1", "2":"2", "3":"3", "4":"4", "5":"5",
"6":"6", "7":"7", "8":"8", "9":"9"}

player = "x"
gameOver = False
winner = None
selection = None

while not gameOver:
    printBoard(squares)

    selection = input(f"{player}'s turn to choose a square (1-9): ")

    if int(selection)<1 or int(selection)>9:
        while int(selection)<1 or int(selection)>9:
            print("Number invalid. Please choose a valid number (1-9)")
            selection = input(f"{player}'s turn to choose a square (1-9): ")
            break

    squares[selection] = player

    if playerHasWon("x", squares):
        gameOver = True
        winner = "x"
    if playerHasWon("o", squares):
        gameOver = True
        winner = "o"
    
    if player=="o":
        player = "x"
    elif player=="x":
        player = "o"

print(f"{winner} wins! Thanks for playing!")
