string = input("Enter a string: ")
words = string.split()
max_len = 0
largest = " "
for word in words:
    if len(word) > max_len:
        max_len = len(word)
        largest = word
print("Largest word:", largest)