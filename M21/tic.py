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
print(lst)

if lst.count('x') == 3 and lst.count('o') == 3 and lst.count('.') != 3:
    print('draw')
if lst.count('x') == lst.count('o'):
    print('invalid game')
elif lst.count('x') == 3 and lst.count('o') < 3:
    print('x')
elif lst.count('o') == 3 and lst.count('x') < 3:
    print('o')
else:
    print('invalid game')