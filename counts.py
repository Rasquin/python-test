#test After

# function count_upper_case--> count the number of uppercase characters in a message.
""" # Case saw in the class
def count_upper_case(message):
    #we seth the counter (count) to 0
    count = 0
    for c in message: 
        #if c is upper case, the count add 1
        if c.isupper():
            count += 1
    return count
"""
#Challenge
def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case("Aa1&") == 1, "1 of each character"

#case that is not goint to pass the test
#assert count_upper_case("a") == 1, "shouldn't past the test. 1 lower case"

print("All the tests passed")