# Write a function that, given:
#     an amount of money
#     a list of coin denominations
# computes the number of ways to make amount of money
# with coins of the available denominations.


def num_of_ways(amount, denominations, m):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if amount >= 1 and m < 0:
        return 0
    return num_of_ways(amount, denominations, m-1) + \
        num_of_ways(amount - denominations[m], denominations, m)


if __name__ == '__main__':
    print num_of_ways(20, [1, 2, 3], 2)
