# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.

# # key: current maxprofit is the current price minus curent min price

import time
class Solution(object):
    def maxProfit(self,prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

# other good solution:maxProfit
# key: can use map to build link of left and right node with maxDepth



def main():
    n=[1,2,3,5]
    time_t=time.time()
    sln=Solution().maxProfit(n)
    print(time.time()-time_t)

    print(sln)

if __name__=="__main__":
    main()