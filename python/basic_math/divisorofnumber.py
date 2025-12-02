import math
def find_divisor(n):
    divisors = []
    half = int(math.sqrt(n)) + 1
    for i in range(1, half):
        if n % i == 0:
            divisors.append(i)

            # condition mainly for after sqrt value like 2 * 18 -> (i) only 
            # till 6 i stored now the counter part also stored
            if i != n // i:
                divisors.append(n // i)
            
    divisors.sort()
    return divisors

print(find_divisor(36))