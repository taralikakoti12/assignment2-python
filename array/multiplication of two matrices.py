r1 = int(input("Enter rows for matrix 1: "))
c1 = int(input("Enter columns for matrix 1: "))
r2 = int(input("Enter rows for matrix 2: "))
c2 = int(input("Enter columns for matrix 2: "))
if c1 != r2:
    print("Matrix multiplication not possible.")
else:
    mat1 = []
    print("Enter matrix 1:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input(f"mat1[{i}][{j}]: ")))
        mat1.append(row)
    mat2 = []
    print("Enter matrix 2:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input(f"mat2[{i}][{j}]: ")))
        mat2.append(row)
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += mat1[i][k] * mat2[k][j]
            row.append(total)
        result.append(row)
    print("Product of matrices:")
    for row in result:
        print(row)
