from main import move_up,move_right,move_left,move_down,BOARD_LENGTH, show_board




#Schema de déplacement au 2048
grid_custom: list[list[str]] = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        ["2", ".", ".", "."],
        ["4", "2", ".", "."]
    ]

grid_custom_up: list[list[str]] = [
        ["2", "2", ".", "."],
        ["4", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]

grid_custom_right: list[list[str]] = [
        ["2", "4", ".", "."],
        ["2", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]

grid_custom_left: list[list[str]] = [
        ["4", "2", ".", "."],
        ["2", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]

grid_custom_down: list[list[str]] = [
        ["4", "2", ".", "."],
        ["2", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]

def rotation_matrice(matrice):
    if not matrice:
        return []

    lignes, colonnes = len(matrice), len(matrice[0])
    matrice_rotatee = []

    for _ in range(colonnes):
        matrice_rotatee.append([0] * lignes)

    for i in range(lignes):
        for j in range(colonnes):
            matrice_rotatee[j][lignes - i - 1] = matrice[i][j]

    return matrice_rotatee


def compare(move) :
    resultat = rotation_matrice(grid_custom)
    if move == grid_custom_right :
        right = rotation_matrice(grid_custom)
        if resultat == move :
            print("TEST SUCCESS")
        else :
            print("TEST FAILURE")
        show_board(right)
        
    elif resultat == move :
        print("TEST SUCCESS")
        show_board(resultat)
    else :
        print("TEST FAILURE")
        show_board(resultat)
    

def rotate(move : str) :
    if move == "right" :
        move_right(grid_custom)
        compare(grid_custom_right)
    if move == "left" :
        move_left(grid_custom)
        compare(grid_custom_left)
    if move == "down" :
        move_down(grid_custom)
        compare(grid_custom_down)
    if move == "up" :
        move_up(grid_custom)
        if grid_custom == grid_custom_up :
            print("TEST SUCCESS")
        else :
            print("TEST FAILURE")
        show_board(grid_custom)
    

rotate("left")

