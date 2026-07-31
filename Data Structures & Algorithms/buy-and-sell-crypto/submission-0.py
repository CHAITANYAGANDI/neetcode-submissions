class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minimum_buying_price = prices[0]
        maximum_profit = 0

        for day_index in range(1, len(prices)):
            
            current_selling_price = prices[day_index]

            current_profit = (
                current_selling_price - minimum_buying_price
            )

            maximum_profit = max(
                maximum_profit,
                current_profit
            )

            minimum_buying_price = min(
                minimum_buying_price,
                current_selling_price
            )

        return maximum_profit