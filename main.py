import random
import os

BOARD_LENGTH: int = 4

# Création des lignes et des colonnes
def GetBoard() -> list[list[str]]:
    board: list[list[str]] = []
    length = BOARD_LENGTH
    for r in range(length) :
        row = []
        for c in range(length) :
            row.append(".")
        board.append(row)
    return board

#Verify if Inputs is in authorized_inputs
def ask_input(message: str, authorized_inputs: list) -> str:
    while True :
        answer: str = input(message + str(authorized_inputs) + " : ")
        
        if answer in authorized_inputs :
            return answer

def show_board(board: list[list[str]]) -> None:
    for row in board:
        print(" ".join(str(sign) for sign in row))

def spawn_tile(board: list[list[str]]) -> tuple[int,int]:
    empty_spots: list[tuple[int, int]] = [(i, j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == "."]
    position : tuple[int,int]= random.choice(empty_spots)
    tile : int = random.randint(1,10)
    if tile == 10 :
        board[position[0]][position[1]] = str("4")
    else :
        board[position[0]][position[1]] = str("2")

def full_board(board: list[list[str]]) -> bool:
    for row in board:
        for sign in row:
            if sign is ".":
                return False
    return True

def movement (board) -> str:
    dico_movement : dict = {"up" : "u", "right" : "r", "down" : "d", "left" : "l" }
    direction: str = ask_input("Entrez une direction" ,(list(dico_movement.values()) + list(dico_movement.keys())))
    if direction == "up" or "u" :
        for i in range(1, BOARD_LENGTH):
            for j in range(BOARD_LENGTH) :
                if board[i][j] != ".":
                    if board[i][j] == board[i-1][j] :
                        board[i-1][j] = str(int(board[i-1][j])*2)
                    else :
                        board[i-1][j] = board[i][j]
                    board[i][j] = "."
    
    if direction == "right" or "r" :
        for i in range(BOARD_LENGTH):
            for j in range(BOARD_LENGTH-1) :
                j = BOARD_LENGTH - j - 2
                if board[i][j] != ".":
                    if board[i][j] == board[i][j+1] :
                        board[i][j+1] = str(int(board[i][j+1])*2)
                    else :
                        board[i][j+1] = board[i][j]
                    board[i][j] = "."

    if direction == "down" or "d" :
        for i in range(BOARD_LENGTH-1):
            i = BOARD_LENGTH - i - 2
            for j in range(BOARD_LENGTH) :
                if board[i][j] != ".":
                    if board[i][j] == board[i+1][j] :
                        board[i+1][j] = str(int(board[i+1][j])*2)
                    else :
                        board[i+1][j] = board[i][j]
                    board[i][j] = "."

    if direction == "left" or "l" :
        for i in range(BOARD_LENGTH):
            for j in range(1,BOARD_LENGTH) :
                if board[i][j] != ".":
                    if board[i][j] == board[i][j-1] :
                        board[i][j-1] = str(int(board[i][j-1])*2)
                    else :
                        board[i][j-1] = board[i][j]
                    board[i][j] = "."

def game():
    board = GetBoard()
    while True:
        os.system('cls')

        if full_board(board):
            print("Vous avez perdu")
            break
        
        spawn_tile(board)
        show_board(board)
        movement(board)
game()