release_year = '1991'
answer = input('When was Python first released?')

if answer == release_year:
    print('Congratulations! That is correct.')
elif answer > release_year:
    print('No, that\'s too late.')
elif answer < release_year:
    print('No, that\'s too early.')

print('Bye!')


answer = input("Return TRUE or FALSE: Python was released in 1991:\n")

if answer.upper() == "TRUE":
  print('Correct')
elif answer.upper() == "FALSE":
  print('Wrong')
elif answer.upper() != ("TRUE" or "FALSE"):
  print('Please answer TRUE or FALSE')

print('Bye!')

