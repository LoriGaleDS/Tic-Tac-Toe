"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        for elem in row:
            if elem != EMPTY:
                count += 1
    if count % 2 == 0:
        return X
    else: 
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] not in (O,X):
                possible_actions.add((i,j))
    return(possible_actions)

def action_is_valid(board,action):
    row = action[0]
    col = action[1]
    if board[row][col] not in (X,O):
        return True
    else: return False

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)
    row = action[0]
    col = action[1]
    if action_is_valid(board, action):
        new_board[row][col] = player(board)
        return new_board
    else: raise Exception("The move is not valid")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """     
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
        
    for i in range(len(board)):

        # check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]   
        
        # check cols
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in (X,O):
        return True
    else: 
        return all(elem is not None for row in board for elem in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else: return 0
    else: return None



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board), None
        v = -math.inf
        best_action = None
        for action in actions(board):
            min_val, _ = min_value(result(board, action))
            if min_val > v:
                v = min_val
                best_action = action
        return v, best_action

    def min_value(board):
        if terminal(board):
            return utility(board), None
        v = math.inf
        best_action = None
        for action in actions(board):
            max_val, _ = max_value(result(board, action))
            if max_val < v:
                v = max_val
                best_action = action
        return v, best_action

    current_player = player(board)
    if current_player == X:
        _, best_action = max_value(board)
    else:
        _, best_action = min_value(board)
    
    return best_action

board1 = [[None, "X", "O"], 
          ["O", "X", None], 
          ["X", None, "O"]]
print(minimax(board1)) 
