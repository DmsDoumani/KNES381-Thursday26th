#Introduction on how to play the game (FIRST CHANGE) 
print("Welcome to the intense game of tic-tac-toe")
print("Game Rules: When you are assigned your player number and letter, each player gets a turn in plugging in row and column numbers to place your X or O in the desired position.")
print("May the best player win")

def create_board(): #It's the same code as yours but changed it abit for it to be easier to call later
    return [["_"] * 3 for _ in range(3)]

def make_move(board, player, row, col):
    board[row][col] = player
    
def check_winner(board):
    
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "_":
            return board[row][0] 
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "_":
            return board[0][col] 
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "_":
        return board[0][0] 
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != "_":
        return board[2][0] 
    
    return None

def check_draw(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == "_":
                return False
    return True

def play_game():
    board = create_board() # Called in the mentioned function
    # (Second Change) Defined a player when the game starts and attributed a letter to said player
    player1 = "X" # Player 1 is X
    player2 = "O" # Player 2 is O
    current_player = player1 # Player 1 starts
    winner = None
    draw = False 
    
    while not winner and not draw:
        for row in board:
            print(" ".join(row))
            
            
        while True: 
            try:
                print(f"{'Player 1 (which is X)'}" if current_player == player1 else f"{'Player 2 (which is O)'}", "turn") # Printing the defiend player names (runs the second change)
                
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))  
                
                # (Change Three) Conditiong the range of valid integer input and if there is space to put in X or O
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "_":
                    break
                print("Invalid input. Try again.")
                
            except ValueError:
                print("Invalid input. Try again.") 
                
        make_move(board, current_player, row, col)
        
        winner = check_winner(board)
        
        draw = check_draw(board) 
        
        current_player = player2 if current_player == player1 else player1 # Runs the second change
        
    for row in board:
        print(" ".join(row))
        
        #  Continuing the second change by printing whoever wins and stating the name and letter of whoever won
    if winner:
        print(f"{'Player 1 (which is X)'}" if winner == player1 else f"{'Player 2 (which is O)'}", "wins!")
    else:
        print("The game is a draw.")
        
play_game()
