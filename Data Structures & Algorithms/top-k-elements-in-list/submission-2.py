class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        
        minHeap = [(val, key) for key, val in cnt.items()]
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)

        res = [y for x, y in minHeap]
        return res
