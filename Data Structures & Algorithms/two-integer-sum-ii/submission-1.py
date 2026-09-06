class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j= 0, len(nums)-1
        while(i<j):
            total = nums[i] + nums[j]
            if total>target:
                j-=1
            elif total<target:
                i+=1
            else:
                return [i+1,j+1]   