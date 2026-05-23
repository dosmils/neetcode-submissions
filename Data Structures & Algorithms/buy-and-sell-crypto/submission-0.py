class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = 10 ** 10
        mx = 0
        for price in prices:
            mn = min(mn, price)
            mx = max(mx, price - mn)
        return mx
        