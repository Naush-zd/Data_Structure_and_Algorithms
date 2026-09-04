class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<=0:
                nums[i] = len(nums)+1
        for i in range(len(nums)):
            val =abs(nums[i])
            if 1 <= val <= len(nums):
                nums[val-1] = -abs(nums[val-1])

        for n in range(len(nums)):
            if nums[n]>0:
                return n+1
        return len(nums)+1

        