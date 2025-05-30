string = input("Enter a string: ")
words = 1
for c in string:
    if c == " ":
        words += 1
print("Number of words:",words)