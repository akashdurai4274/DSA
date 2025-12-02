arr = [4,3,56,75,2,1]

def selection_sort(list):
    n = len(list)
    for i in range(n - 1 , 0, -1):
        max_index = find_maxIndex(list, i+1)
        swap(list, max_index,i)
    return list

def find_maxIndex(list, end):
    maxIndex = 0
    for i in range(end):
        if list[i] > list[maxIndex]:
            maxIndex = i
    return maxIndex

def swap(list, a, b):
    list[a],list[b] = list[b],list[a]

print(selection_sort(arr))

