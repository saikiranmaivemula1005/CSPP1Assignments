rows = 3
matrix = []
lst = []
c = 0
for i1_ in range(rows):
    l1_ = [i1_ for i1_ in input().split(' ')]
    matrix.append(l1_)
# print(matrix)
for i in matrix:
    for j in i:
        lst.append(j)
    if j not in ('x','o','.'):
        # print(j)
        c += 1
if c >= 1:
    print('invalid input')
    exit()
for i in matrix:
	print(i)