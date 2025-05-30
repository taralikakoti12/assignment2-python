word=input("Enter a word:")
word=word.lower()
length_word=int(len(word))
for i in range (len(word)):
    if word[-length_word]==word[-1]:
        print(word,"is a palindrome")
    else:
        print(word,"is not a palindrome")