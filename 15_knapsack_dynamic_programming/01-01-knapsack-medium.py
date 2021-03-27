"""
Introduction
Given the weights and profits of ‘N’ items, we are asked to put these items in a
 knapsack which has a capacity ‘C’.
The goal is to get the maximum profit out of the items in the knapsack.
Each item can only be selected once, as we don’t have multiple quantities of any
 item.

Let’s take the example of Merry, who wants to carry some fruits in the knapsack
to get maximum profit.
    Here are the weights and profits of the fruits:
Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

Let’s try to put various combinations of fruits in the knapsack, such that their
 total weight is not more than 5:
Apple + Orange (total weight 5) => 9 profit
Apple + Banana (total weight 3) => 7 profit
Orange + Banana (total weight 4) => 8 profit
Banana + Melon (total weight 5) => 10 profit
This shows that Banana + Melon is the best combination as it gives us the
maximum profit and the total weight does not exceed the capacity.
"""


def solve_knapsack(profits, weights, capacity):
    # basic check
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp_out = [0] * (capacity + 1)
    # if we have only one weight, take it if it is not more than the capacity.
    for i in range(1, capacity + 1):
        if weights[0] <= i:
            dp_out[i] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit1 = profits[i] + dp_out[c - weights[i]]
            # exclude the item
            profit2 = dp_out[c]
            # take maximum
            dp_out[c] = max(profit1, profit2)
    return dp_out[capacity]


def main():
    print("Total knapsack profit: " +
          str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
    print("Total knapsack profit: " +
          str(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


if __name__ == "__main__":
    main()

"""
Time and Space complexity 
The above solution the has time and space complexity of O(N*S), 
where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.
"""
