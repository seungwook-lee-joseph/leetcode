class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        max_profit = 0

        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                if sell <= buy:
                    pass
                profit = sell - buy

                sub_prices = prices[j+2:]
                sub_profit = self.maxProfit(sub_prices)

                tot_profit = profit + max(sub_profit, 0)  # Ensure sub_profit is non-negative

                if max_profit < tot_profit:
                    max_profit = tot_profit

        return max_profit
