import random
import keyboard
import time
import os

BOARD_LENGTH: int = 4
nb_tiles: int = 2

#Création du board
def GetBoard() -> list[list[str]]:
    board: list[list[str]] = []
    length: int = BOARD_LENGTH
    for r in range(length):
        row: list[str] = []
        for c in range(length):
            row.append(".")
        board.append(row)
    return board

#Apparition du board
def show_board(board: list[list[str]]) -> None:
    for row in board:
        print("    ".join(str(sign) for sign in row))

#Apparition des tuiles aléatoires
def spawn_tile(board: list[list[str]]) -> None:
    for _ in range(nb_tiles):
        empty_spots: list[tuple[int, int]] = [
            (i, j) for i in range(len(board)) for j in range(len(board)) if board[i][j] == "."
        ]
        if len(empty_spots) > 0:
            position: tuple[int, int] = random.choice(empty_spots)
            tile: int = random.randint(1, 10)
            if tile == 10:
                board[position[0]][position[1]] = str("4")
            else:
                board[position[0]][position[1]] = str("2")

#Vérifie si le tableau est plein
def full_board(board: list[list[str]]) -> bool:
    for row in board:
        for sign in row:
            if sign == ".":
                return False
    return True

#Fonction pour aller vers le haut
def move_up(board: list[list[str]]) -> None:
    for j in range(BOARD_LENGTH):
        for i in range(1, BOARD_LENGTH):
            if board[i][j] != ".":
                while i > 0 and (board[i - 1][j] == "." or board[i - 1][j] == board[i][j]):
                    if board[i - 1][j] == ".":
                        board[i - 1][j] = board[i][j]
                        board[i][j] = "."
                    elif board[i - 1][j] == board[i][j]:
                        board[i - 1][j] = str(int(board[i - 1][j]) * 2)
                        board[i][j] = "."
                        break
                    i -= 1

#Fonction pour aller vers la droite
def move_right(board: list[list[str]]) -> None:
    for i in range(BOARD_LENGTH):
        for j in range(BOARD_LENGTH - 2, -1, -1):
            if board[i][j] != ".":
                while j < BOARD_LENGTH - 1:
                    if board[i][j + 1] == ".":
                        board[i][j + 1] = board[i][j]
                        board[i][j] = "."
                        j += 1
                        break
                    
                    if board[i][j + 1] == board[i][j]:
                        board[i][j + 1] = str(int(board[i][j + 1]) * 2)
                        board[i][j] = "."
                        break

                    j += 1

#Fonction pour aller vers le bas
def move_down(board: list[list[str]]) -> None:
    for j in range(BOARD_LENGTH):
        for i in range(BOARD_LENGTH - 2, -1, -1):
            if board[i][j] != ".":
                while i < BOARD_LENGTH - 1 and (board[i + 1][j] == "." or board[i + 1][j] == board[i][j]):
                    if board[i + 1][j] == ".":
                        board[i + 1][j] = board[i][j]
                        board[i][j] = "."
                    elif board[i + 1][j] == board[i][j]:
                        board[i + 1][j] = str(int(board[i + 1][j]) * 2)
                        board[i][j] = "."
                        break
                    i += 1

#Fonction pour aller vers la gauche
def move_left(board: list[list[str]]) -> None:
    for i in range(BOARD_LENGTH):
        for j in range(1, BOARD_LENGTH):
            if board[i][j] != ".":
                while j > 0 and (board[i][j - 1] == "." or board[i][j - 1] == board[i][j]):
                    if board[i][j - 1] == ".":
                        board[i][j - 1] = board[i][j]
                        board[i][j] = "."
                    elif board[i][j - 1] == board[i][j]:
                        board[i][j - 1] = str(int(board[i][j - 1]) * 2)
                        board[i][j] = "."
                        break
                    j -= 1

#Verifie si un mouvement est disponible
def test_movement(board: list[list[str]]) -> bool:
    for i in range(BOARD_LENGTH):
        for j in range(BOARD_LENGTH):
            if i + 1 != 4:
                if board[i][j] == board[i + 1][j]:
                    return False
            if j + 1 != 4:
                if board[i][j] == board[i][j + 1]:
                    return False
    return True

#Main loop
def game() -> None:
    board: list[list[str]] = GetBoard()
    while True:
        os.system("cls")
        
        if full_board(board) and test_movement(board):
            print("Vous avez perdu")
            show_board(board)
            break
        
        spawn_tile(board)
        show_board(board)
        time.sleep(0.5)
        
        while True :
            event = keyboard.read_event()

            if event.event_type == keyboard.KEY_DOWN and event.name == "z":
                move_up(board)
                break
                
            if event.event_type == keyboard.KEY_DOWN and event.name == "q":
                move_left(board)
                break
                
            if event.event_type == keyboard.KEY_DOWN and event.name == "s":
                move_down(board)
                break
                
            if event.event_type == keyboard.KEY_DOWN and event.name == "d":
                move_right(board)
                break


if __name__ == "__main__":
    game()