rows = 3
matrix = []
lst = []
for i1_ in range(rows):
    l1_ = [i1_ for i1_ in input().split(' ')]
    matrix.append(l1_)
# print(matrix)
for i in matrix:
	for j in i:
		lst.append(j)
	if lst.count(j) == 3:
		print(j)
