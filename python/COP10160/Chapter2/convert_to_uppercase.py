string = input("String to be converted: ")
n = int(input("What are the number of last letters to convert: "))

#get first part of string
first = string[:len(string) - n]
#get last part of string, the part we are converting
last = string[len(string) - n:]
#add first and last part of string together again
print(first + last.upper())
