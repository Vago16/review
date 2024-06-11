def steps(number):
    """
    Function that no matter which positive number you start with, you will always reach 1 eventually.
    param number: int - positive integer
    """
    if number < 1:
        raise ValueError('Only positive integers are allowed')
    step_counter = 0
    while number > 1:
        number = 3 * number + 1 if number % 2 else number / 2
        step_counter += 1
    return step_counter