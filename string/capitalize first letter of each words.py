string = input("Enter a string: ")
result = " "
capitalize = True
for c in string:
    if capitalize and c.isalpha():
        result += c.upper()
        capitalize = False
    else:
        result += c
    if c == " ":
        capitalize = True
print("Capitalized string:", result)