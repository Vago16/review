import json

sample = {
  "name": "Bert Bertie",
  "age": 24
}

sample_json = json.dumps(sample)
#dict is encoded to JSON and should return a string
print(sample_json)
print(type(sample_json))

original_sample = json.loads(sample_json)
#JSON is encoded back to a Python object and returns as a dict
print(original_sample)
print(type(original_sample))
