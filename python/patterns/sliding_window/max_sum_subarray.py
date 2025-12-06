def max_sub_arraysum(nums, k):
    left = 0
    window_sum = 0
    max_sum = 0
    
    for right in range(len(nums)):
        window_sum += nums[right]

        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[left]
            left += 1
    return max_sum

        

print(max_sub_arraysum([2,5,1,3,2], 3))