from main import move_up,move_right,move_left,move_down,BOARD_LENGTH, show_board




#Schema de déplacement au 2048
grid_custom: list[list[str]] = [
        ["16", ".", ".", "."],
        [".", "4096", "4", "."],
        [".", ".", "1024", "."],
        [".", "2048", "32", "."]
    ]

grid_custom_up: list[list[str]] = [
        ["16", "4096", "4", "."],
        [".",  "2048", "1024", "."],
        [".", ".",     "32", "."],
        [".", ".", ".", "."]
    ]

grid_custom_right: list[list[str]] = [
        ["32", "2048", ".", "."],
        ["1024", ".", ".", "."],
        ["4", "4096", ".", "."],
        ["16", ".", ".", "."]
    ]

grid_custom_left: list[list[str]] = [
        ["2048", "1024", "4096", "16"],
        ["32", ".", "4", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]

grid_custom_down: list[list[str]] = [
        [".", "32", "2048", "16"],
        [".", "1024", "4096", "."],
        [".", "4", ".", "."],
        [".", ".", ".", "."]
    ]

def rotation_matrice(matrice: list[list[str]]) -> list[list[str]]:

    lignes: int = len(matrice)
    colonnes: int = len(matrice[0])
    matrice_rotatee: list[list[str]] = []

    for _ in range(colonnes):
        matrice_rotatee.append([0] * lignes)

    for i in range(lignes):
        for j in range(colonnes):
            matrice_rotatee[j][lignes - i - 1] = matrice[i][j]

    return matrice_rotatee


def compare(move: list[list[str]]) -> None:
    resultat = rotation_matrice(grid_custom)
    if move == grid_custom_right or move == grid_custom_down:
        right = rotation_matrice(resultat)
        if right == move:
            print("TEST SUCCESS")
        else:
            print("TEST FAILURE")
        show_board(right)

    elif resultat == move:
        print("TEST SUCCESS")
        show_board(resultat)
    else:
        print("TEST FAILURE")
        show_board(resultat)


def rotate(move: str) -> None:
    if move == "right":
        move_right(grid_custom)
        compare(grid_custom_right)
    if move == "left":
        move_left(grid_custom)
        compare(grid_custom_left)
    if move == "down":
        move_down(grid_custom)
        compare(grid_custom_down)
    if move == "up":
        move_up(grid_custom)
        if grid_custom == grid_custom_up:
            print("TEST SUCCESS")
        else:
            print("TEST FAILURE")
        show_board(grid_custom)


rotate("right")
