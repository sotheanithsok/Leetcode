""" 
Problem:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    
    Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

Solution:
    The best single transcation for any given day is the difference between the today and the minimum price of among previous day prices. Then, we can return the largest difference. 

Complexity:
    Time: O(n)
    Space: O(1)
"""

from math import inf


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # Initialize best price and minimum price
        bestPrice, minPrice = -inf, inf

        # Iterate through all prices
        for price in prices:

            # Update the minimum price
            minPrice = min(minPrice, price)

            # Update the best price
            bestPrice = max(bestPrice, price - minPrice)

        return bestPrice
