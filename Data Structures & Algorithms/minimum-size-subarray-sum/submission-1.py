class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=float("inf")
        l=0
        t_sum=0
        for r in range(len(nums)):
            t_sum+=nums[r]
            while(t_sum>=target):
                length= min(length, r-l+1)
                t_sum-=nums[l]
                l+=1
           
                
        
        return 0 if length == float("inf") else length

