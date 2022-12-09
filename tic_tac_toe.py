def welcome():
    print("*******************")
    print("  Добро пожаловать  ")
    print("      в игру       ")
    print("  'Крестики-нолики'  ")
    print("*******************")
    print(" Чтобы сделать ход, введите: x y")
    print("  x - номер строки  ")
    print("  y - номер столбца ")


board = [[" "] * 3 for i in range(3) ]

def show_board():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(board):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def request():
    while True:
        cells = input("         Ваш ход: ").split()

        if len(cells) != 2:
            print(" Введите 2 числа! ")
            continue

        x, y = cells

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Такой клетки нет! ")
            continue

        if board[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cells = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cells in win_cells:
        symbols = []
        for c in cells:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Победа игрока 'X'!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победа игрока '0'!!!")
            return True
    return False


welcome()
count = 0
while True:
    count += 1
    show_board()
    if count % 2 == 1:
        print(" Ходит Игрок 'X'!")
    else:
        print(" Ходит Игрок '0'!")

    x, y = request()

    if count % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print("Победила Дружба!")
        break