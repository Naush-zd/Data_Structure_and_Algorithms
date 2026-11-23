class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)
        k = len(nums)-k
        for _ in range(k):
            heapq.heappop(minHeap)
        return minHeap[0]