class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for lt in range(len(nums) - 1):
            rt = lt + 1
            while rt < len(nums) and nums[lt] + nums[rt] != target:
                rt += 1
            if rt < len(nums) and nums[lt] + nums[rt] == target:
                return [lt, rt]
            else:
                continue

        