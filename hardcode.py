from main import move_up,move_right,move_left,move_down

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

grid_custom =  [
    [".",".",".","2"],
    [".",".",".","2"],
    [".",".",".","2"],
    [".",".",".","2"],
]


grid_expected =  [
    ["2",".",".","."],
    ["2",".",".","."],
    ["2",".",".","."],
    ["2",".",".","."],
]


func = [move_left, move_up, move_right, move_down]

for i in range(0, 4) :
    func[i](grid_custom)
    if grid_custom == grid_expected :
        print("TEST SUCCESS")
    else :
        print("TEST FAILED")
    #rotation 90 grid
    grid_custom = rotation_matrice(grid_custom)
    #rotation 90 expected_result
    grid_expected = rotation_matrice(grid_expected)

