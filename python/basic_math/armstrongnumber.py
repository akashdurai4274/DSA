from countdigits import count_digits

def find_armstrong(n):
    number = n
    digits = count_digits(n)
    sum = 0

    while(n > 0):
        sum += (n % 10) ** digits
        n //= 10
    return sum == number


print(find_armstrong(153))
print(find_armstrong(371))