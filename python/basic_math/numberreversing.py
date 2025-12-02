def reverse_number(n):
    rev = 0
    while n > 0:
        temp = n % 10
        rev = (rev * 10) + temp
        n = n // 10

    return rev

print(reverse_number(12345))
