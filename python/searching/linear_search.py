list = [4,5,8,32,44,87,98,43]

def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return  -1

print(linear_search(list, 44))
