class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, (target - p) / s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        prevTime = 0
        count = 0
        for i in pair:
            if i[1] > prevTime:
                count += 1
                prevTime = i[1]

        return count