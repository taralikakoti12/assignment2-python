string = input("Enter a string: ")
reversed_str = " "
for c in string:
    reversed_str = c + reversed_str
if string == reversed_str:
    print("Palindrome")
else:
    print("Not a palindrome")