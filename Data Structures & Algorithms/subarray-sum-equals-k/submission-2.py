class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum={}
        currSum, count=0, 0
        for n in nums:
            currSum+=n
            diff = currSum -k
            if diff==0:
                count+=1
            count += prefixsum.get(diff,0)
            prefixsum[currSum] = prefixsum.get(currSum,0) +1
        return count

        