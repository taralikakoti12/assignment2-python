r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
matrix = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input(f"matrix[{i}][{j}]: ")))
    matrix.append(row)
transpose = []
for i in range(c):
    row = []
    for j in range(r):
        row.append(matrix[j][i])
    transpose.append(row)
print("Transpose of matrix:")
for row in transpose:
    print(row)