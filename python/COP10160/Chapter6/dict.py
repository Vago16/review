d1=dict(
    state="NY",
    city="New York"
    )
#another way of initializing a dictionary
d2={
    "state": "Maryland",
    "city": "Baltimore"
    }

print(type(d1))
print(d1)
print(d2)

d2['bird']='Baltimore Oriole'
print(d2)

print(d1.get('state'))
print(d1.get('age'))
#second argument specifies what should be returned when no value exists
print(d1.get('age', 'Key age is not defined'))

#iterating through a dictionary's keys
for item in d1:
    print(item)
#iterating through a dictionary's keys explicity
for item in d1.keys():
    print(item)
#iterating through a dictionary's values
for item in d1.values():
  print(item)
#iterating through a dictionary's keys and values
for key, value in d1.items():
  print(key, value)

a = {
  "size": "10 feet",
  "weight": "16 pounds"
}
#if key exists in dict, prints True, else prints false
print("size" in a)
print("length" in a)
