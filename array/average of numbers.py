n = int(input("Enter number of elements (max 100): "))
numbers = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
average = sum(numbers) / n
print("Average:", average)