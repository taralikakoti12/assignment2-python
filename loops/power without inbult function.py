base=int(input("Enter the base:"))
exponent=int(input("Enter the exponent:"))
result=1
i=1
while i<=exponent:
    result*=base
    i+=1
print(base,"raised to the power",exponent,"is",result)