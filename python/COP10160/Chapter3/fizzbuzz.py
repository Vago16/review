#two possible answers for FizzBuzz
numList = list(range(1,51))
finalList =[]

for num in range(len(numList)):
    x = numList[num]
    output=''
    if x % 3 == 0:
        output += 'Fizz'
    if x % 5 == 0:
        output += 'Buzz'
    if output =='':
        output += str(x)
    numList[num] = output
print(numList)

#for i in range(1,51):
#  if i%3 == 0 and i%5 == 0:
#    print("FizzBuzz")  
#  elif i%3 == 0:
#    print("Fizz")
#  elif i%5 == 0:
#    print("Buzz")
#  else:
#    print(i)
