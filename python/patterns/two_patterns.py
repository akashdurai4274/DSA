arr = [2, 7, 11, 15]
target = 9

left, right = 0, len(arr) - 1
while left < right:
    s = arr[left] + arr[right]
    if s == target:
        print("Pair found:", arr[left], arr[right])
        break
    elif s < target:
        left += 1
    else:
        right -= 1
