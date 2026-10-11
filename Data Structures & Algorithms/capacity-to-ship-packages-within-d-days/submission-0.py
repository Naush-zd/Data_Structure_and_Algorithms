class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r= max(weights), sum(weights)
        res=r
        def canship(cap):
            day, curr= 1, cap
            for w in weights:
                if curr-w<0:
                    day+=1
                    if day>days:
                        return False
                    curr = cap
                curr -=w
            return True


        while(l<=r):
            m= (l+r)//2
            if canship(m):
                res= min(res, m)
                r=m-1
            else:
                l=m+1
        return res
