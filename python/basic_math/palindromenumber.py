from numberreversing import reverse_number

def check_palindrome_number(n):
    if n == 0:
        return True
    if n == reverse_number(n):
        return True
    else:
        return False
    
print(check_palindrome_number(1321))