class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i, j = 0, len(nums) - 1

        while i <= j:

            if nums[i] == val and nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

            elif nums[i] == val and nums[j] == val:
                j -= 1

            elif nums[i] != val:
                i += 1

        return j + 1