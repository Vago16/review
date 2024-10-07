answer = lambda first, second: first + second
print(answer(6,9))

#use a lmbda function to generate a new list with the squares of every item in the list
numbers = [2,4,6,8,10]

#without lambda
'''
squared =[]

for num in numbers:
squared.append(num**2)
'''

#with lambda
squared = list(map(lambda num: num ** 2, numbers))

print(squared)
