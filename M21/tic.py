rows = 3
matrix = []
for i1_ in range(rows):
    l1_ = [i1_ for i1_ in input().split(' ')]
    matrix.append(l1_)
# print(matrix)
for i in matrix:
	print(matrix.count(i))
	if matrix.count(i) == 3:
		print(matrix[i])
print('invalid game')