class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        
        cnt_lst = [(val, key) for key, val in cnt.items()]
        cnt_lst.sort()

        res = [y for x, y in cnt_lst[::-1]]
        return res[:k]