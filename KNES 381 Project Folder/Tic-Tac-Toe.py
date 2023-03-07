#Introduction on how to play the game (FIRST CHANGE) 
print("Welcome to the intense game of tic-tac-toe")
print("Game Rules: When you are assigned your player number and letter, each player gets a turn in plugging in row and column numbers to place your X or O in the desired position.")
print("May the best player win")

def create_board(): >>
    return [["_"] * 3 for _ in range(3)]

def make_move(board, player, row, col):
    board[row][col] = player
    
def check_winner(board):
    
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "_":
            return board[row][0] >>
        
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "_":
            return board[0][col] >>
        
    if board[0][0] == board[1][1] == board[2][2] != "_":
        return board[0][0] >>
    if board[2][0] == board[1][1] == board[0][2] != "_":
        return board[2][0] >>
    
    return None

def check_draw(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == "_":
                return False
    return True

def play_game():
    board = create_board() >>>
    player1 = "X" # Player 1 is X
    player2 = "O" # Player 2 is O
    current_player = player1 # Player 1 starts
    winner = None
    is_draw = False >> 
    
    while not winner and not is_draw:
        for row in board:
            print(" ".join(row))
            
        while True:# Get a valid move  >>>
            try:# Try to get a valid move
                print(f"{'Player 1 (which is X)'}" if current_player == player1 else f"{'Player 2 (which is O)'}", "turn")# Print whose turn it is
                
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "_":# Check if the move is valid
                    break# If it is, break out of the loop
                print("Invalid input. Try again.")
            except ValueError:# If the user enters something that is not an integer
                print("Invalid input. Try again.") >>>
                
        make_move(board, current_player, row, col)
        
        winner = check_winner(board)
        
        is_draw = check_draw(board) >>
        
        current_player = player2 if current_player == player1 else player1# Switch players >>>
        
    for row in board:
        print(" ".join(row))# Print the winner
        
    if winner:
        print(f"{'Player 1 (which is X)'}" if winner == player1 else f"{'Player 2 (which is O)'}", "wins!")# Print who won
    else:
        print("The game is a draw.")
        
play_game()
