sentence = input("Sentence: ")
query = input("Word to look for in sentence: ")

#remove whitespace and convert to lowercase
sentence = sentence.lower().strip()
query =query.lower().strip()

#count amount of times query showed up in sentence
count_occurrences = sentence.count(query)

#print with formatting
print(f"There are {count_occurrences} of '{query}' in the sentence.")
