# Best Time to Buy and Sell Stock (at most one transaction allowed)
# https://www.geeksforgeeks.org/best-time-to-buy-and-sell-stock/

def max_profit(input):
    result = 0
    buy = input[0]
    for i in range(1, len(input)):
        if buy < input[i]:
            sum = input[i] - buy
            if sum > result:
                result = sum
        else:
            buy = input[i]
    print(result)


max_profit([7, 1, 5, 3, 6, 4])
max_profit([7, 6, 5])
