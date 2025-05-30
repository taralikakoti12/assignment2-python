string = input("Enter a string: ")
vowels = consonants = digits = spaces = 0
for c in string:
    if c.lower() in 'aeiou':
        vowels += 1
    elif c.isalpha():
        consonants += 1
    elif c.isdigit():
        digits += 1
    elif c.isspace():
        spaces += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("White spaces:",spaces)