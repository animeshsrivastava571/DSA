'''
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
'''


def buy_sell_stock(lst_price):

    sort_list = sorted(lst_price,reverse=True)
    if sort_list == lst_price:
        buy_value_day = 0
        sell_value_day = 0
        return buy_value_day,sell_value_day 
    
    max_diff = 0
    for i in range(len(lst_price)):
        for j in range (i+1,len(lst_price)):
            if (lst_price[j] - lst_price[i]) > 0 and (lst_price[j] - lst_price[i]) > max_diff:
                max_diff = lst_price[j] - lst_price[i]
                buy_value_day = i+1
                sell_value_day = j+1
            # else:
            #     buy_value = 0
            #     sell_value = 0

    return buy_value_day,sell_value_day

#lst_price = [7,1,5,3,6,4]
lst_price = [7,6,4,3,1]
print(buy_sell_stock(lst_price))


