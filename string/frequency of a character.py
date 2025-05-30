string = input("Enter a string: ")
char = input("Enter character to find frequency: ")
count = 0
for c in string:
    if c == char:
        count += 1
print("Frequency of", char,"is:",count)