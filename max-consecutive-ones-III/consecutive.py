def longestOnes(nums, k):
    left = 0
    res = 0
    
    for i in range(len(nums)):
        print(nums[left:i])
        if nums[i] == 0:
            k -= 1
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
        res = max(res, i - left + 1)
    return res