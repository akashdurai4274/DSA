# Sum of subarray less than or equal to K

def subarray_sum(nums, k):
    left = 0
    window_sum = 0
    max_len = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > k:
            window_sum -= nums[left]
            left += 1

        max_len = max(max_len, right - left +1)

    return max_len

print(subarray_sum([1,2,1,0,1,1,0], 4))