# time complexity O(n)
# space complexity O(1)
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([2, 1, 2, 1, 10]))
print(max_profit([1, 5, 2, 3]))
print(max_profit([3, 3, 3, 3]))
print(max_profit([5]))
print(max_profit([]))s
print(max_profit(list(range(100000))))