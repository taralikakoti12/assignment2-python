def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_prime_pairs(num):
    print(f"Prime pairs that sum to {num}:")
    found = False
    for i in range(2, num//2 + 1):
        if is_prime(i) and is_prime(num - i):
            print(f"{num} = {i} + {num - i}")
            found = True
    if not found:
        print("No prime pairs found.")