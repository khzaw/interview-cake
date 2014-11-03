# Write a function that, given:
#     an amount of money
#     a list of coin denominations
# computes the number of ways to make amount of money
# with coins of the available denominations.


def num_of_ways(amount, denominations):
    # print "Amount :", amount, " Denominations:", denominations
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denominations) == 0:
        return 0
    return num_of_ways(amount-denominations[0], denominations) + \
        num_of_ways(amount, denominations[1:])


if __name__ == '__main__':
    print num_of_ways(20, [19, 2])       # 1
    print num_of_ways(4, [1, 2, 3])      # 4
