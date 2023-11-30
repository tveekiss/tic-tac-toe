def enter_move(field):
    move = list(map(int, input("Введите ряд и столбец (через пробел): ").split()))
    if not (len(move) == 2 and 0 < move[0] < 4 and 0 < move[1] < 4):
        print("Неправильно набрана ячейка")
    elif field[move[0]][move[1]] != '-':
        print("Ячейка уже занята")
    else:
        return move
    return enter_move(field)


def check_winner(row, cols):
    def wrapper(element):
        count = {}
        for i in element:
            if i in count:
                count[i] += 1
                if count[i] == 3:
                    return True
            else:
                count[i] = 1
        return False
    temp1 = 0
    temp2 = 0
    for a, b in zip(row, cols):
        if a - b == 0:
            temp1 += 1
            if temp1 == 3:
                return True
        if a - b == 2 or a - b == -2 or (a == 2 and b == 2):
            temp2 += 1
            if temp2 == 3:
                return True
    return wrapper(row) or wrapper(cols)


field = (
    [' ', '1', '2', '3'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-'],
    ['3', '-', '-', '-']
)
print(*[" ".join(row) for row in field], sep='\n')
row_x, cols_x, row_o, cols_o, winner = [], [], [], [], ''
while True:
    print("Ходят крестики")
    move = enter_move(field)
    field[move[0]][move[1]] = 'x'
    row_x.append(move[0])
    cols_x.append(move[1])
    print(*[" ".join(row) for row in field], sep='\n')
    if check_winner(row_x, cols_x):
        winner = 'крестики'
        break
    if len(row_x) == 5:
        break
    print("Ходят нолики")
    move = enter_move(field)
    field[move[0]][move[1]] = 'o'
    row_o.append(move[0])
    cols_o.append(move[1])
    print(*[" ".join(row) for row in field], sep='\n')
    if check_winner(row_o, cols_o):
        winner = 'нолики'
        break

if winner:
    print(f"Победил игрок, игравший за {winner}!!!")
else:
    print("Ничья!!!")
