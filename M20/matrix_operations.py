def mult_matrix(m1_, m2_):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = []
    if len(m1_[0]) == len(m2_):
        for i in range(len(m1_)):
            restemp = []
            for j in range(len(m2_[0])):
                res = 0
                for k in range(len(m2_)):
                    res += m1_[i][k] * m2_[k][j]
                restemp.append(res)
            result.append(restemp)
        return result
    print("Error: Matrix shapes invalid for mult")
    return None

def add_matrix(m1_, m2_):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1_) != len(m2_):
        print("Error: Matrix shapes invalid for addition")
        return
    for i, j in zip(m1_, m2_):
        if len(i) != len(j):
            print("Error: Matrix shapes invalid for addition")
            return
    result = []
    for i, j in zip(m1_, m2_):
        row = []
        for p, q in zip(i, j):
            row.append(p + q)
        result.append(row)
    return result
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows,columns = input().split(',')
    rows = int(rows)
    columns = int(columns)
    matrix = []
    for i in range(rows):
        l1 = [int(i) for i in input().split(' ')]
        if len(l1) != columns:
            print("Error: Invalid input for the matrix")
            return None
        matrix.append(l1)
    return matrix
def main():
    # read matrix 1
    # read matrix 2
    # add matrix 1 and matrix 2
    # multiply matrix 1 and matrix 2
    m1_ = read_matrix()
    # print(m1_)
    m2_ = read_matrix()
    if (m1_ != None and m2_ != None):
        print(add_matrix(m1_, m2_))
        print(mult_matrix(m1_, m2_))
    # print(m2_)
if __name__ == '__main__':
    main()
