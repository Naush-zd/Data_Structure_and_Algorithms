class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res= [0]* len(temperatures)
        stack= []
        for i, n in enumerate(temperatures):
            
            while stack and n> temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev]=i-prev

            stack.append(i)
        return res