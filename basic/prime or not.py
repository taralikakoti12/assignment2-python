num=int(input("Enter a number:"))
if num<=1:
    print(False)
else:
    is_prime=True
    for i in range(2,num+1):
        is_prime=False
        break
    print("The number is prime:"is_prime)