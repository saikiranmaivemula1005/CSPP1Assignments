def checkGame(matrix):
    """kk"""
    count_o=0
    count_x=0
    for row in matrix:
        for i in row:
            if i == "o":
                count_o += 1
            elif i == "x":
                count_x += 1
    if abs(count_x-count_o) == 1 or abs(count_x-count_o) == 0:
        return True
    return False    
def checkInput(matrix):
    """kk"""
    for i in matrix:
        for j in i:
            if j not in "o x .":
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
    transPose =[]
    for i in range(len(matrix)):
        row =[]
        for j in range(len(matrix[0])):
            row.append(matrix[j][i])
        transPose.append(row)
    return rows(transPose)
def diagonals(matrix):
    """kk"""
    d1 =[]
    for i in range(len(matrix)):
        d1.append(matrix[i][i])
    if d1.count("o") == 3:
        return (True, "o")
    if  d1.count("x") == 3:
        return (True, "x")
    d2 = []
    j = len(matrix[0]) - 1
    for i in range(len(matrix)):
        d2.append(matrix[i][j])
        j = j - 1
    if d2.count("o") == 3:
        return (True, "o")
    if  d2.count("x") == 3:
        return (True, "x")
    return (False, 0)
def checkWinner(matrix):
    if rows(matrix)[0]:
        print(rows(matrix)[1])
    elif column(matrix)[0]:
        print(column(matrix)[1])
    elif diagonals(matrix)[0]:
        print(diagonals(matrix)[1])
    else:
        print("draw")
def main():
    matrix =[]
    i=0
    while i<3:
        lst = input().split(" ")
        matrix.append(lst)
        i=i+1
    # print(matrix)
    if checkInput(matrix):
        if checkGame(matrix):
            checkWinner(matrix)
        else :
            print("invalid game")
    else:
        print("invalid input")
main()
