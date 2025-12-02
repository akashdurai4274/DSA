def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if abs(curr_sum - target) < abs(closest - target):
                closest = curr_sum

            if curr_sum < target:
                left += 1

            if curr_sum > target:
                right -= 1

            else:
                return curr_sum
            
    return closest


nums =  [-4, -1, 2, 5, 6]
target = 1

print(threeSumClosest(nums=nums, target=1))


