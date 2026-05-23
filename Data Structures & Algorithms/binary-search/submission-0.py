class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lt, rt = 0, len(nums)
        while lt < rt:
            middle = (lt + rt) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                lt = middle + 1
            else:
                rt = middle
        return -1

        