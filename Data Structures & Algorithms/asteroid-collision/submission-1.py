class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stack = []

        for i in range(len(a)):
            alive = True    
            while stack and a[i] < 0 and stack[-1] > 0:
                if abs(a[i]) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(a[i]) == stack[-1]:
                    stack.pop()
                    alive= False
                    break
                else:
                    alive= False
                    break

            if alive:
                
                stack.append(a[i])

        return stack