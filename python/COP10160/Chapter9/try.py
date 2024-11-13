try:
    with open('input.txt', 'r') as myinputfile:
        for line in myinputfile:
            print(line)
except FileNotFoundError:
    print("Whoops! File does not exist.")
except ValueError:
    print("A value error occurred")

#additional else statement
try:
    with open('input.txt', 'r') as myinputfile:
        for line in myinputfile:
            print(line)
except FileNotFoundError:
    print("Whoops! File does not exist.")
except ValueError:
    print("A value error occurred")
except Exception:
    print("Something unforeseen happened")
else:
    print("No error because file exists")
print("Execution will continue to here.")

#finally defines a code block that must execute before the try...except block exits
try:
    with open('input.txt', 'r') as myinputfile:
        for line in myinputfile:
            print(line)
except FileNotFoundError:
    print("Whoops! File does not exist.")
except ValueError:
    print("A value error occurred")
except Exception:
    print("Something unforeseen happened")
finally:
    print("I will always show up")
  
print("Execution will continue to here.")