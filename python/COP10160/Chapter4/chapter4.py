#def tells the compiler what follows next is a function
def addNum(a,b): #whatever is in () are arguments passed to the function
    return a + b

#pass in arguments to the function and print
result = addNum(2,3)
print(result)
#or
print(addNum(1,2))

def multiply(a,b,c):
    return a * b * c
print(multiply(1,2,3))

#lambda functions: declare an anonymous function    
add = lambda x,y: x+y
print('sum: ', add(2,3))

mult = lambda x,y,z: x*y*z
print('product: ', mult(2,3,4))

#list of numbers
numbers = [1,2,3,4,5]

#use a filter to get only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print('even values: ', evens)

odds = list(filter(lambda x: x % 2 != 0, numbers)) # or x % 2 == 1
print('odd values: ', odds)