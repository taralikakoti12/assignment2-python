n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest element is:",largest)