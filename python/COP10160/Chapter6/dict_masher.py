def dict_masher(dict_a,dict_b):
    '''
    A function that takes two dictionaries and returns a single dictionary
with non-duplicated keys.

>>> dict_masher({"name": "Amos"}, {"age": 100})
>>> 
{
   "name": "Amos",
   "age": 100
}
    '''
    for key, value in dict_b.items():
        if key not in dict_a:
            dict_a[key] = value
        return dict_a
