import math

#better approach
def find_gcd(m,n):
    if m == 0 or n == 0:
        return max(m,n)
    else:
        maximum, minimum = max(m,n), min(m,n)
        return find_gcd(maximum - minimum, minimum)
    
#optimal approach
def find_gcd_optimal(m,n):
    if m == 0 or n == 0:
        return max(m,n)
    else:
        return find_gcd(n, m%n)


print(find_gcd(20,15))
print(find_gcd_optimal(6,9))


