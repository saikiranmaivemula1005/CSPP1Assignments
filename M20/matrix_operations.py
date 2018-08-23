def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    pass

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    res = []
    if len(m1) == len(m2):
        res = [m1[i] + m2[i] for i in range(len(m1))]
        print(res)
    return(res)

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
        matrix.append(l1)
    return matrix


def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    m1 = read_matrix()
    # print(m1)
    m2 = read_matrix()
    add_matrix(m1, m2)
    mult_matrix(m1, m2)
    # print(m2)
if __name__ == '__main__':
    main()
