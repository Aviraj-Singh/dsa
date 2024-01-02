# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#Example:
#Input: prices = [7,1,5,3,6,4],
#Output: 5
#Explanation: [4,-1,2,1] has the largest sum = 6.
# Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

#The first solution that comes to mind, as always, is the brute force solution.

def max_profit_bruteforce(prices):
    max_profit = 0
    n = len(prices)
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
                
    return max_profit

# Example 1
prices1 = [7, 1, 5, 3, 6, 4]
print(max_profit_bruteforce(prices1))  # Output: 5

# Example 2
prices2 = [7, 6, 4, 3, 1]
print(max_profit_bruteforce(prices2))  # Output: 0

#Since we are looping through two nested for loops the time complexity is O(n^2)
#There's a much faster way to solve this which involves iterating through the array once and keeping track of the minimum price encountered so far.

def max_profit_efficient(prices):
    if not prices:
        return 0
    
    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
        
    return max_profit

# Example 1
prices1 = [7, 1, 5, 3, 6, 4]
print(max_profit_efficient(prices1))  # Output: 5

# Example 2
prices2 = [7, 6, 4, 3, 1]
print(max_profit_efficient(prices2))  # Output: 0

# Since this requires only one for loop, the time complexity is an efficiently O(n)!
