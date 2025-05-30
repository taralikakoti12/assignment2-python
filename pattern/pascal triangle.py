rows=int(input("Enter number of rows:"))
coef=1
for i in range(1,rows+1):
    for j in range(1,rows-i+1):
        print(" ",end=" ")
    for k in range(0,i):
        if k==0 or i==o:
            coef=1
        else:
            coef=coef*(i-k)//k
        print(coef, end=" ")
    print()