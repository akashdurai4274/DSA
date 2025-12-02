list = [4,5,8,32,44,87,98,43]

def binary_search(list, target):
    left = 0
    right = len(list)

    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid + 1
        elif list[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

print(binary_search(list, 44))