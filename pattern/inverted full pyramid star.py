rows=int(input("Enter number of rows:"))
for i in range(rows,1,-1):
    for j in range(0,rows-i):
        print(" ",end=" ")
    for k in range(i,2*i-1):
        print("*",end=" ")
    for k in range(1,i-1):
        print("*",end=" ")
    print()