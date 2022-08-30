"""
Problem:
    It is a sweltering summer day, and a boy wants to buy some ice cream bars.

    At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

    Return the maximum number of ice cream bars the boy can buy with coins coins.

    Note: The boy can buy the ice cream bars in any order.

    Example 1:
    Input: costs = [1,3,2,4,1], coins = 7
    Output: 4
    Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
    
    Example 2:
    Input: costs = [10,6,8,7,7,8], coins = 5
    Output: 0
    Explanation: The boy cannot afford any of the ice cream bars.
    
    Example 3:
    Input: costs = [1,6,3,1,2,5], coins = 20
    Output: 6
    Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.

Solution:
    Sort all costs in an ascending order. Count how many ice-creams we can buy given a certain amount of coints. 

Complexity:
    Time: O(nlogn)
    Space: O(1)
"""


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:

        # Sort costs
        costs.sort()

        # Initialize the result
        res = 0

        # Iterate through all cost
        for cost in costs:

            # Update the coin
            coins -= cost

            # If coins reach negative, we know that we are overspend
            if coins < 0:
                break

            # Else, increment the result
            res += 1

        return res
