class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr=0
        for i in range(len(nums)):
            xorr ^= nums[i] ^ (i + 1)
        return xorr
