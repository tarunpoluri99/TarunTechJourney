'''
Best Time to Buy & Sell Stock

Simple Explanation
Imagine you can see all future prices.
You want to buy at the lowest price and sell at the highest price after that.
[7, 1, 5, 3, 6, 4]

Day 1 → price 7
Day 2 → price 1  ← buy here (lowest so far)
Day 3 → price 5  ← profit = 5-1 = 4
Day 4 → price 3  ← profit = 3-1 = 2
Day 5 → price 6  ← profit = 6-1 = 5 ✅ best!
Day 6 → price 4  ← profit = 4-1 = 3

Answer → 5th Day is best to sell and buy


Approach
Step 1 → Start with minimum price = first price and maximum profit = 0

Step 2 → Loop through each price
         If current price < min price
         → update min price (found cheaper buy day!)

         If current price - min price > max profit
         → update max profit (found better sell day!)

Step 3 → Return max profit
'''


class A:
    def max_profit(self,prices):
        min_price=prices[0]
        max_profit=0
        for i in prices:
            if i<min_price:
                min_price=i
            if i-min_price>max_profit:
                max_profit=i-min_price
        return max_profit
prices=list(map(int,input().split()))
s1=A()
k=s1.max_profit(prices)
print(k)
