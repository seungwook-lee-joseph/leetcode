# Only calculate profit sell_price > buy_price.
# if buy_price is small then we can change the buyprice.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        buy_price = prices[0]
        max_len = len(prices)

        for i in range(1, max_len):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                profit = max(profit, prices[i]-buy_price)
        return profit