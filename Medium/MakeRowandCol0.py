def make_zeroes(matrix):
  m = len(matrix)
  n = len(matrix[0])

  row = set()
  col = set()

  for i in range(m):
    for j in range(n):
      if matrix[i][j] == 0:
        if i not in row:
          row.add(i)
        if j not in col:
          col.add(j)
  print(row,col)
  for i in row:
    for j in range(n):
      matrix[i][j]=0

  for j in col:
    for i in range(m):
      matrix[i][j]=0

  return matrix


mat  =[[1, 5, 45, 0, 81], [6, 7, 2, 82, 8], [20, 22, 49, 5, 5], [0, 23, 50, 4, 92]]
print(make_zeroes(mat))