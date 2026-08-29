# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy=min(prices)
#         i=prices.index(buy)
#         sell=buy
#         for j in range(i+1,len(prices)):
#             if prices[j]>sell:
#                 sell=prices[j]
#         return sell-buy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the lowest price seen so far
            if price < min_price:
                min_price = price
            # Check if selling today yields a better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
        