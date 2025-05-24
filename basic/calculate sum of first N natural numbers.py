num=int(input("Enter the number:"))
if num<0:
    print("Enter a positive number:")
else:
    while(num>0):
        sum+=num
        num-=1
    print("The sum is",sum)