#Vending Machine

"""We're going to build a function that will calculate the coins that should be
returned by a vending machine to make the correct change.

specification: given an amount of change that needs to be paid, we want to
generate the list of coins that should be given to the customer.

Our function should pay the minimum number of coins possible, and the available
coin denominations are 100, 50, 20, 10, 5, 2, and 1."""

from byotest import *
# from byotest we import everything

# Refactoring, we save the list [100, 50, 20, 10, 5, 2, 1] inside a variable called coins
usd_coins = [100, 50, 25, 10, 5, 2, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]

#putting the equals there in the get_change(), it means that if we don't supply the argument,
#it will default to using eur_coins.
def get_change(amount, coins=eur_coins):
    """
    Takes the payment amount and returns the change
    `amount` the amount of money that we need to provide change for
    Returns a list of coin values
    """
    #Now we can take all the is out because they are included inside the while
    """if amount == 0:
        return []
    
    if amount in coins:
        return [amount]"""
    
    change = []
    for coin in coins:
        #As long as the coin is less than or equal to the amount, it will carry on adding it.
        #Before was an "if"
        while coin <= amount:
            amount -= coin
            change.append(coin)

    return change


#  Write our tests for our code

test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(9), [5, 2, 2])
test_are_equal(get_change(35, usd_coins), [25, 10])

print("All tests pass!")