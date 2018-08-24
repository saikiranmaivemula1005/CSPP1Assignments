rows = 3
matrix = []
for i1_ in range(rows):
    l1_ = [i1_ for i1_ in input().split(' ')]
    matrix.append(l1_)
# print(matrix)
for i in matrix:
	for j in i:
		# print(j)
		print(matrix.count(j))
		if matrix.count(j) == 3:
			print(matrix[j],'kk')
# print('invalid game')