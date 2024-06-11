def is_armstrong_number(number):
    """
    An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
    param number: int - positive integer
 
    Function to calculate if given number is an Armstrong number.
    """
    num = str(number)
    #turns integer into a string
    sum = 0
    #introduces sum variable for the for loop
    for digit in num:
        #seperates each digit into an integer and raises it to how many digits is in the given number ie. len(num)
        #so 100 would be would have a len of 3, while 10 would have a len of 2, and so on
        sum += int(digit) ** len(num)
    return sum == number