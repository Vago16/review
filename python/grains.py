def square(number):
    """
    param number: int - integer representing grain in between 1 and 64
    
    Function calculates the value of grain on a given square.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)
def total():
    """
    Function that calculates total value of grain on chessboard on 64 squares.
    """
    return 2 ** 64 - 1