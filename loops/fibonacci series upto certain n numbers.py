n=int(input("Enter the value of n:"))
a=0
b=1
print("Fibonacci series is:",end=" ")
while a<=n:
    print(a,end=" ")
    a=b
    b=a+b