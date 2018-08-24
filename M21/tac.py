rows = 3
matrix = []
lst = []
c = 0
for i1_ in range(rows):
    l1_ = [i1_ for i1_ in input().split(' ')]
    matrix.append(l1_)
# print(matrix)
for i in range(len(matrix)):
    if i not in ('x','o','.'):
        # print(j)
        c += 1
    # if c >= 1:
    #     print('invalid input')
    #     exit()
for i in range(len(matrix)):
    # print(i)
    for j in range(len(matrix)):
        # print(matrix[i][j])
        print(matrix.count(matrix[i][j]))
            # print(matrix[i][j])
