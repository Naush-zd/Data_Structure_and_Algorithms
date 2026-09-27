class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stack = []

        for i in range(len(a)):
            explode = False    
            while stack and a[i] < 0 and stack[-1] > 0:
                if abs(a[i]) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(a[i]) == stack[-1]:
                    stack.pop()
                    explode= True
                    break
                else:
                    explode = True
                    break

            if not explode:
                
                stack.append(a[i])

        return stack