def create_board():# Create a 3x3 board
    return [["_"] * 3 for _ in range(3)]
def make_move(board, player, row, col):# Make a move on the board
    board[row][col] = player
def check_winner(board):# Check if there is a winner
    for row in range(3):# Check rows
        if board[row][0] == board[row][1] == board[row][2] != "_":
            return board[row][0]
    for col in range(3):# Check columns
        if board[0][col] == board[1][col] == board[2][col] != "_":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != "_":
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] != "_":
        return board[2][0]
    return None# Return None if there is no winner
def check_draw(board):# Check if there is a draw
    for row in range(3):
        for col in range(3):
            if board[row][col] == "_":# If there are no empty spaces, return True
                return False
    return True# Return True if there is a draw
def play_game():# Play a game of tic-tac-toe
    board = create_board()# Create a board
    current_player = "X"# Set the current player to X
    winner = None# Set the winner to None
    is_draw = False# Set the draw to False
    while not winner and not is_draw:# While there is no winner and the game is not a draw
        for row in board:# Print the board
            print(" ".join(row))
        while True:# Get the player's move
            try:# If the move is invalid, ask for a new move
                row = int(input("Enter row (0-2): "))# Get the row
                col = int(input("Enter column (0-2): "))# Get the column
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == "_":# If the move is valid, break
                    break
                print("Invalid input. Try again.")# If the move is invalid, ask for a new move
            except ValueError:
                print("Invalid input. Try again.")
        make_move(board, current_player, row, col)# Make the move
        winner = check_winner(board)# Check if there is a winner
        is_draw = check_draw(board)# Check if there is a draw
        current_player = "O" if current_player == "X" else "X"# Switch the current player
    for row in board:# Print the board
        print(" ".join(row))
    if winner:# Print the winner
        print(f"Player {winner} wins!")
    else:# Print the draw
        print("The game is a draw.")
play_game()# Play the game
game.py
