class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        nums = [1,7,3,6,5,6]
        pref = [0,1,8,11,17,22,28]
        suff = [28,27,20,17,11,6,0]
        '''
        n = len(nums)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]
        
        for i in range(n):
            if prefix[i] == suffix[i + 1]:
                return i
        return -1

