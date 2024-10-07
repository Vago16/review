number = 5

"""
Define function "summation" that takes two parameters
"""
def sumnation(first, second):
    total = first + second + number
    return total

# Call the "summation" function with two parameters as expected and assign
outer_total = sumnation(10, 20)

print ("The first number we initilised was " + str(number))

print("The total after sumnation is " + str(outer_total))
