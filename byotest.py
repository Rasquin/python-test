def number_of_evens(numbers):
    return 0

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)


#test_are_equal(number_of_evens([1,2,3,4,5]), 2)

#challenge I 

""" tests that fail the test_not_equal, and test_is_in test methods. 
Verify that the message is correct for the values given.
"""
#test_not_equal(2,2)
#test_is_in([1,3],2)

#challenge II

"""Write test methods for test_not_in which tests than an item is not in a 
collection, and test_between which tests that a value is between a lower and 
upper limit, inclusive."""

def test_not_in(collection,item):
    assert item not in collection, "{0} does contain {1}".format(collection,item)
    
def test_between(l,u,n):
    #l=lower limit/ u=upper limit / n=number in evaluation
    assert l<=n<=u, "{0} is not between {1} and {2}".format(n,l,u)
    
#test_not_in([1,2,3],2)
test_between(1,3,2)
