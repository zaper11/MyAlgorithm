def maxProfit(cost):
    if len(cost) == 1 or len(cost) == 0:
        return 0
    profit = 0
    for i in range(len(cost)-1):
        if cost[i] - cost[i+1] < 0:
            profit += cost[i+1] - cost[i]
    return (profit)