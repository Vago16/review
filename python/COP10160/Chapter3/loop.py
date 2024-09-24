#class notes
age = 18

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")

count = 1

while count <=5:
    print(f"Count is {count}")
    count += 1

x = 1

if x < 5:
    print("x is less than 5")

while x <5:
    print(f"x is {x}")
    x += 1

for i in range(3):
    print(f"Loop iteration {i}")
    
#when specifying range, goes up to second number but does not include it
for i in range(1,6):
    print(i)

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f"Current number is {num}")

#nested loop, inner loop runs 2x for every loop the outer loop does, which is 3x
for i in range(1,4):
    for j in range(1,3):
        print(f"i={i}, j={j}")

#breaks the loop before i is printed being compared to 5
for i in range(1,10):
    if i == 5:
        print("Breaking the loop")
        break
    print(i)
