def check_input(matrix):
    for i in matrix:
        for j in i:
            if j not in 'o,x,.':
                return False
            return True
def row(matrix):
    winner_x = False
    winner_o = False
    for row in matrix:
        if row.count('x') == 3:
            winner_x = True
            return (True,'x')
        if row.count('o') == 3:
            return(True, 'o')
            winner_o = True
    if winner_o and winner_x:
        print('invalid game')
        exit()
    if winner_x:
        return(True,'x')
    if winner_o:
        return(True,'o')
    return (False,0)
def column(matrix):
    trans = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)[0]):
            row.append(matrix[j][i])
        trans.append(row)
    return row(trans)
def diagonal(matrix):
    d1 = []
    for i in range(len(matrix)):
        d1.append(matrix)[i][i]
    if d1.count('o') == 3:
        return (True,'o')
    if d1.count('x') == 3:
        return (True, 'x')
    d2 = []
    j = len(matrix[0])-1
    for i in range(len(matrix)):
        d2.append(matrix[i][i])
        j -= 1
    if d2.count('o') == 3:
        return (True,'o')
    if d2.count('x') == 3:
        return (True, 'x')
    return (False,0)

def check_winner(matrix):
    if row(matrix)[0]:
        print(row(matrix)[1])
    elif column(matrix)[0]:
        print(column(matrix)[1])
    elif diagonal(matrix)[0]:
        print(diagonal(matrix))[1]
    else:
        print('draw')
def check_game(matrix):
    c_of_x = 0
    c_of_o = 0
    for i in matrix:
        for j in i:
            if i == 'o':
                c_of_o += 1
            elif i == 'x':
                c_of_x += 1
    if abs(c_of_x - c_of_o) == 1:
        return True
def main():
    matrix = []
    i = 0
    while i < 3:
        l1 = input().split(' ')
        matrix.append(l1)
        i += 1
    # print(matrix)
    if check_input(matrix):
        if check_game(matrix):
            if check_winner(matrix):
                print('')
        else:
            print('invalid game')
    else:
        print('invalid input')
main()
