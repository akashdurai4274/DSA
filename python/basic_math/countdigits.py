import math
#brute force - % 10 approach

def count_digits(n):
    if n == 0:
        return 1
    return math.floor(math.log10(abs(n))) + 1


print(count_digits(123456789086))
print(count_digits(0))