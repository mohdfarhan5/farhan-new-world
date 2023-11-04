# Input matrices
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# Initialize a result matrix with zeros of the same shape as X and Y
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Perform matrix addition
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

# Print the result matrix
for row in result:
    print(row)
