r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
mat1 = []
print("Enter elements of first matrix:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input(f"mat1[{i}][{j}]: ")))
    mat1.append(row)
mat2 = []
print("Enter elements of second matrix:")
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input(f"mat2[{i}][{j}]: ")))
    mat2.append(row)

result = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(mat1[i][j] + mat2[i][j])
    result.append(row)

print("Sum of matrices:")
for row in result:
    print(row)
