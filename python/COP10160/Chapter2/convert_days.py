days = int(input("Number of days:"))
years = days // 365
#weeks:use modulo operation to convert remainder of days not converted into
# years into weeks
weeks = (days % 365) // 7
days = days - ((years * 365) + (weeks * 7))

print("Years:", years)
print("Weeks:", weeks)
print("Days", days)
