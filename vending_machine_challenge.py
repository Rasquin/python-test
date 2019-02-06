#Challenge I

""""Change the function so that instead of a list of coins, the function works 
with a dictionary that contains the coin denominations, and the quantity of each
coin available. By default, assume there are 20 of each coin, but this can be 
overridden by passing a dictionary to the function as with the previous example.

If a coin that would normally be used to make change isn't available the 
program should attempt to use smaller coins to make up the change.

If it is not possible to make the change with the coins available, 
the function should raise an error."""

from byotest import *
# from byotest we import everything

# Create a dictionary with denomination of coin and its quantity as key, value
usd_coins = [100:20, 50:20, 25:20, 10:20, 5:20, 2:20, 1:20]
eur_coins = [200:20, 100:20, 50:20, 20:20, 10:20, 5:20, 2:20, 1:20]


def get_change(amount, coins=eur_coins):
       """
    Takes the payment amount and returns the change
    `amount` the amount of money that we need to provide change for
    `coins` is the set of coins that we need to get change for (i.e. the set
        of available coins)
    Returns a list of coin values
    """
    change = []
    
      # Unlike a list, looping through a dictionary does not keep the order.
    # Therefore we use `sorted()` to sort the order. 'coins.key()' to move between the keys. This will start with the
    # lowest by default, so we use `reverse=True` to start with the highest
    # denomination. The `while` ends when the domination quantity reaches 0.
    # An exception is thrown if there are insufficient coins to give change.
    
    for denomination in sorted(coins.key(), reverser=True):
        #As long as the coin is less than or equal to the amount, it will carry on adding it.
        #Before was an "if"
        while denomination <= amount and coins[denomination] > 0:
            amount -= denomination
            coins[denomination] -=1
            change.append(denomination)
    
    if amount != 0:
        raise Exception("Insufficient coins to give change.")


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
#here we are choosing the list of coins and their Key:value pars.
test_are_equal(get_change(5, {2: 1, 1: 4}), [2, 1, 1, 1])
test_exception_was_raised(get_change, (5, {2: 1, 1: 2}),
    "Insufficient coins to give change.")

print("All tests pass!")