def disp(board):
    for i in range(0,9):
        if board[i] == i:
            board[i] = "_"
            print("_",end=" ")
        else:
            print(board[i],end=" ")
        
        if (i+1)%3 == 0:
            print("\n")

board = [0,1,2,3,4,5,6,7,8]
print("Enter number between 1 to 9:")
disp(board)

isWin = False

i = 0
while i < 9:
    if(i % 2 == 0):
        turn = "X"
    else:
        turn = "O"

    
    print("I:",i)
    inputNumber = int(input("Turn of player " + turn + " : "))

    if (inputNumber > 0 and inputNumber < 10) and board[inputNumber-1] == "_" :
        board[inputNumber-1] = turn
    else:
        print("This place is occupied or you have entered invalid input.")
        i -= 1
    
    disp(board)

    if i > 3:
        # Vertical
        for x in range(0,3):
            if board[x] != "_" and board[x] == board[x+3] == board[x+6]:
                isWin = True
                
        # Horizontal
        for x in range(0,9,3):
            if board[x] != "_" and board[x] == board[x+1] == board[x+2]:
                isWin = True

        # Diagonal \
        if board[0] != "_" and board[0] == board[4] == board[8]:
                isWin = True
        
        # Diagonal /
        if board[2] != "_" and board[2] == board[4] == board[6]:
                isWin = True

    if isWin:
        print(f"Player {turn} has Won the game.")
        break

    if i == 8:
        print("Its a Draw.")

    i +=1