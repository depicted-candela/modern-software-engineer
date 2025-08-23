from itertools import product
from typing import List, Optional

class TicTacToe:

    dim = 3
    iterator = range(3)
    players = {'X', 'O'}
    players_role = {True: 'X', False: 'O'}
    role_players = {'X': True, 'O': False}
    
    def __init__(self, board: List[List[Optional[str]]] = None):
        if board is None:
            self.board = [[None for _ in range(3)] for _ in range(3)]
        else:
            self.board = [row[:] for row in board]
        self.compute_free_items()
    
    def compute_free_items(self):
        self.free_items = {
            (i, j) for i, j in product(self.iterator, self.iterator) if not self.board[i][j]
        }

    def make_move(self, role, position):
        x, y = position
        self.board[x][y] = self.players_role[role]
    
    def next_movement(self, player):
        next_player = self.players_role[not player]
        next_role = self.role_players[next_player]
        return next_player, next_role


board = [
    ['O', None, 'X'],
    ['X', 'O', 'O'],
    [None, None, 'X']
]
board1 = [
    ['O', 'O', 'O'],
    ['X', 'O', 'O'],
    [None, None, 'X']
]
board2 = [
    ['O', None, 'X'],
    ['O', 'O', 'O'],
    [None, None, 'X']
]
board3 = [
    ['O', None, 'X'],
    ['X', 'O', 'O'],
    ['X', 'X', 'X']
]
board4 = [
    ['O', None, 'X'],
    ['O', 'O', 'O'],
    ['O', None, 'X']
]
board5 = [
    ['O', 'O', 'X'],
    ['X', 'O', 'O'],
    [None, 'O', 'X']
]
board6 = [
    ['O', None, 'X'],
    ['X', 'O', 'X'],
    [None, None, 'X']
]
board7 = [
    ['O', None, 'X'],
    ['X', 'O', 'X'],
    [None, None, 'O']
]
board8 = [
    ['O', None, 'X'],
    ['X', 'X', 'O'],
    ['X', None, 'X']
]
board9 = [
['X', 'O', 'X'],
['O', 'X', 'O'],
['X', 'O', 'X']
]
board10 = [
['X', 'O', 'X'],
['O', 'X', 'X'],
['O', 'X', 'O']
]
board11 = [
['X', 'O', 'X'],
['X', 'O', 'X'],
['O', 'X', 'O']
]
board12 = [
['X', 'X', 'O'],
['O', 'X', 'X'],
['X', 'O', 'O']
]
board13 = [
['O', 'X', 'O'],
['X', 'O', 'X'],
['X', 'O', 'X']
]
board14 = [
['O', 'X', 'O'],
['X', 'X', 'O'],
['X', 'O', 'X']
]
board15 = [
['O', 'X', 'X'],
['X', 'O', 'O'],
['X', 'O', 'X']
]
board16 = [
['X', 'O', 'X'],
['O', 'O', 'X'],
['X', 'X', 'O']
]

def winning_check(board: list[list[str]]):
    return squared_check(board) or diagonal_check(board)

def squared_check(board: list[list[str]]):
    for i in range(3):
        if board[0][i] is not None and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        if board[i][0] is not None and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
    return False

def diagonal_check(board: list[list[str]]):
    diagonals = [((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for (r1, c1), (r2, c2), (r3, c3) in diagonals:
        if board[r1][c1] == board[r2][c2] == board[r3][c3]: return board[r1][c1]
    return False

def is_draw(board: list[list[str]]):
    if winning_check(board): return False
    dims = range(3)
    for i, j in product(dims, dims):
        if not board[i][j]: return False
    return True

def player(which: str):
    if which == 'X': return True
    return False

def minimax(
        board: list[list[str]],
        is_maximizing_player = True
        ):
    base = base_case(board, is_maximizing_player)
    if base: return base
    
    tictactoe = TicTacToe(board)

    if is_maximizing_player:
        max_score = float("-infinity")
        for position in tictactoe.free_items:
            tictactoe.make_move(is_maximizing_player, position)
            score = minimax(tictactoe.board, is_maximizing_player)
            max_score = max(score, max_score)
        return max_score
    
    if not is_maximizing_player:
        is_not_maximizing = not is_maximizing_player
        min_score = float("infinity")
        for position in tictactoe.free_items:
            tictactoe.make_move(is_not_maximizing, position)
            score = minimax(tictactoe.board, is_not_maximizing)
            min_score = min(min_score, score)
        return min_score

def base_case(board, is_maximizing_player):
    winner = winning_check(board)
    if winner == 'X':
        return 10 if is_maximizing_player else -10
    if winner == 'O':
        return -10 if is_maximizing_player else 10
    if is_draw(board): return 0
    return False

def find_best_move(board):
    tictactoe = TicTacToe(board)
    best_score = float("-inf")
    for position in tictactoe.free_items:
        tictactoe.make_move(True, position)
        score = minimax(board)
        best_score = max(score, best_score)
        if best_score > 0: position
    print(position, best_score)

if __name__ == "__main__":
    tictactoe = TicTacToe()
    find_best_move(tictactoe.board)

# print(is_draw(board9))
# print(is_draw(board10))
# print(is_draw(board11))
# print(is_draw(board12))
# print(is_draw(board13))
# print(is_draw(board14))
# print(is_draw(board15))
# print(is_draw(board16))