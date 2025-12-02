nums = [1,0,0,3,12]

# By Filling

def moveZeros(nums):
    index = 0
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0
    return nums

print(moveZeros(nums=nums))    

# By Swapping(More Simpler and Optimal)

def move_zeros_swap(nums):
    last_pos = 0
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[current], nums[last_pos] = nums[last_pos], nums[current]
            last_pos += 1
    return nums

print(move_zeros_swap(nums=nums))