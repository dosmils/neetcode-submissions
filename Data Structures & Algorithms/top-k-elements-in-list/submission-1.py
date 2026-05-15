class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        keys = set(nums)
        for key in nums:
            if key in d:
                d[key] += 1
            else:
                d[key] = 1
        sorted_dict = dict(sorted(d.items(), key=lambda x: x[1])[::-1])
        result = [key for key, value in list(sorted_dict.items())[:k]]
        return result