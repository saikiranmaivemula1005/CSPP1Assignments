"""kk"""
def check_game(matrix):
    """kk"""
    count_o = 0
    count_x = 0
    for row in matrix:
        for i1_ in row:
            if i1_ == "o":
                count_o += 1
            elif i1_ == "x":
                count_x += 1
    if abs(count_x-count_o) == 1 or abs(count_x-count_o) == 0:
        return True
    return False
def check_input(matrix):
    """kk"""
    for i1_ in matrix:
        for j1_ in i1_:
            if j1_ not in "o x .":
                return False
    return True
def rows(matrix):
    """kk"""
    winner_x = False
    winner_o = False
    for row in matrix:
        if row.count("x") == 3:
            winner_x = True
        if row.count("o") == 3:
            winner_o = True
    if winner_o and winner_x:
        print("invalid game")
        exit()
    if winner_x:
        return (True, "x")
    if winner_o:
        return (True, "o")
    return (False, 0)
def column(matrix):
    """kk"""
    transpose = []
    for i1_ in range(len(matrix)):
        row = []
        for j1_ in range(len(matrix[0])):
            row.append(matrix[j1_][i1_])
        transpose.append(row)
    return rows(transpose)
def diagonals(matrix):
    """kk"""
    d1_ = []
    length = len(matrix)
    for i1_ in range(length):
        d1_.append(matrix[i1_][i1_])
    if d1_.count("o") == 3:
        return (True, "o")
    if  d1_.count("x") == 3:
        return (True, "x")
    d2_ = []
    j1_ = len(matrix[0]) - 1
    for i1_ in range(length):
        d2_.append(matrix[i1_][j1_])
        j1_ = j1_ - 1
    if d2_.count("o") == 3:
        return (True, "o")
    if  d2_.count("x") == 3:
        return (True, "x")
    return (False, 0)
def check_winner(matrix):
    """kk"""
    if rows(matrix)[0]:
        print(rows(matrix)[1])
    elif column(matrix)[0]:
        print(column(matrix)[1])
    elif diagonals(matrix)[0]:
        print(diagonals(matrix)[1])
    else:
        print("draw")
def main():
    """kk"""
    matrix = []
    i1_ = 0
    while i1_ < 3:
        lst_ = input().split(" ")
        matrix.append(lst_)
        i1_ = i1_ + 1
    # print(matrix)
    if check_input(matrix):
        if check_game(matrix):
            check_winner(matrix)
        else:
            print("invalid game")
    else:
        print("invalid input")
main()
