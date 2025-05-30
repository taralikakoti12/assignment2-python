string = input("Enter a string: ")
result = " "
for c in string:
    if c.isalpha():
        result += c
print("Output String:",result)