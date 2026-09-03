class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        no1=no2=-1
        count1=count2 =0
        for i in nums:
            if i == no1:
                count1+=1
            elif i==no2:
                count2+=1
            elif count1==0:
                no1= i
                count1=1
            elif count2==0:
                no2=i
                count2=1
            else:
                count1-=1
                count2-=1
        count1 = 0
        count2 = 0

        for num in nums:
            if num == no1:
                count1 += 1
            elif num == no2:
                count2 += 1

        res = []

        if count1 > len(nums) // 3:
            res.append(no1)

        if count2 > len(nums) // 3:
            res.append(no2)

        return res

