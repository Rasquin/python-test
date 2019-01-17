#test Before

""" The even_number_of_evens function,  accepts a list of numbers and returns 
True if the list contains an even number of even numbers"""

def even_number_of_evens(numbers):
    
    """
    Returns the number of even numbers contained in a list of numbers.
    `numbers` should be a list containing numbers
    
    Returns either True or False based on a number of criteria.
        - if `numbers` is empty, return `False`
        - if the number of even numbers is odd, return `False`
        - if the number of even numbers is 0, return `False`
        - if the number of even numbers is even, return `True`
    """
    
    # Check to see if the list is empty
    if numbers==0:
        return False
    else:
        # Set a `number_of_evens` variable that will be incremented each time
        # an even number is found
        evens = 0

    # Iterate of over each item and if it's an even number, increment the
    # `evens` variable
    for number in numbers:
        if number % 2 == 0:
            evens += 1
    
    if evens == 0:
        return False
    else:
        return evens % 2 == 0
        
        
assert even_number_of_evens([]) == False, "No numbers"   
assert even_number_of_evens([2]) == False, "One even number"
# assert even_number_of_evens([2, 4]) == True, "Two even numbers"
# assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
# assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")