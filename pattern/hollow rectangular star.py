rows=int(input("Enter the number of rows:"))
coloumns=int(input("Enter the number of columns:"))
for i in range(0,rows):
    for j in range(0,coloumns):
        if i==0 or j==0 or i==rows-1 or j==cols-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        print()