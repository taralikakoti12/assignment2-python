num1=int(input("Enter the value of num1:"))
num2=int(input("Enter the value of num2:"))
if num1>num2:
    max_num=num1
else:
    max_num=num2
for i in range(max_num,(num1*num2)+1):
    if(i%num1==0) and (i%nuum2==0):
        lcm=i
print("The LCM of",num1, "and", num2, "is", lcm)