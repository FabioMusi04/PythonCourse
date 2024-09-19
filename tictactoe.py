import numpy as np

# Define the Tic Tac Toe board
def initialize_board(size=3):
    return np.full((size, size), ' ')

def print_board(board):
    size = board.shape[0]
    print('-' * (size * 4 - 2))
    print('\n'.join([' | '.join(row) for row in board]))
    print('-' * (size * 4 - 2))

# Check for win or draw
def check_winner(board, mark):
    size = board.shape[0]
    # Check rows and columns
    for i in range(size):
        if np.all(board[i, :] == mark) or np.all(board[:, i] == mark):
            return True
    # Check diagonals
    if np.all(np.diag(board) == mark) or np.all(np.diag(np.fliplr(board)) == mark):
        return True
    return False

def is_draw(board):
    return np.all(board != ' ') and not (check_winner(board, 'X') or check_winner(board, 'O'))

# Minimax algorithm for optimal move
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return 10 - depth
    if check_winner(board, 'O'):
        return depth - 10
    if is_draw(board):
        return 0

    size = board.shape[0]
    if is_maximizing:
        best_score = -np.inf
        for i in range(size):
            for j in range(size):
                if board[i, j] == ' ':
                    board[i, j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i, j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for i in range(size):
            for j in range(size):
                if board[i, j] == ' ':
                    board[i, j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i, j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = np.inf
    move = None
    size = board.shape[0]
    for i in range(size):
        for j in range(size):
            if board[i, j] == ' ':
                board[i, j] = 'O'
                score = minimax(board, 0, True)
                board[i, j] = ' '
                if score < best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop with scoring and new game functionality
def play_game():
    board = initialize_board()
    scores = {'X': 0, 'O': 0}
    while True:
        current_player = 'X'
        while True:
            print_board(board)
            if current_player == 'X':
                print(f'Player {current_player}, enter your move (row, column): ')
                row, col = map(int, input().split(','))
                if board[row, col] != ' ':
                    print('Invalid move. Try again.')
                    continue
            else:
                print('Computer is making a move...')
                row, col = best_move(board)
            
            board[row, col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f'Player {current_player} wins!')
                scores[current_player] += 1
                break
            if is_draw(board):
                print_board(board)
                print('The game is a draw!')
                break
            current_player = 'O' if current_player == 'X' else 'X'
        print(f'Score: X - {scores["X"]}, O - {scores["O"]}')
        if input('Play another game? (yes/no): ').strip().lower() != 'yes':
            break
        else:
            board = initialize_board()

play_game()
