def binary_to_decimal(binary_str):
    decimal = 0
    power = len(binary_str) - 1
    for digit in binary_str:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal
