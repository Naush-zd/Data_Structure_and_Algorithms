class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum={0:1}
        currSum, count=0, 0
        for n in nums:
            currSum+=n
            diff = currSum -k

            count += prefixsum.get(diff,0)
            prefixsum[currSum] = prefixsum.get(currSum,0) +1
        return count

        