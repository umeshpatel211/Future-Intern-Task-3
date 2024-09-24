'''Create a program that allows users to play the classic game of rock, paper,
scissors against the computer. The user will input their choice, and the computer
will randomly select one of the three options. The program will then determine the
winner based on the rules of the game and display the result. The game will continue 
until the user decides to stop playing.'''

# Tic-Tac-Toe Game

def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                      (0, 4, 8), (2, 4, 6)]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    return all(space != ' ' for space in board)

def play_game():
    board = [' '] * 9
    current_player = "X"
    game_over = False

    print("Welcome to Tic-Tac-Toe!")
    
    while not game_over:
        print_board(board)
        
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        
        board[move] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing!")
            break

# Start the game
main()
