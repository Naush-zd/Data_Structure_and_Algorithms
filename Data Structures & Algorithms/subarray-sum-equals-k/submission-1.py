class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {}
        currSum = 0
        count = 0

        for i, num in enumerate(nums):

            currSum += num

            if currSum == k:
                count += 1

            diff = currSum - k

            if diff in prefix:
                count += len(prefix[diff])

            if currSum not in prefix:
                prefix[currSum] = []

            prefix[currSum].append(i)

        return count

        