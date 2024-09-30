password = 'random'
valid = False

while not valid:
    answer = input('please enter your password:')

    if answer == password:
        print('Welcome back user!')
        valid = True
    else:
        print('invalid password, try again')
