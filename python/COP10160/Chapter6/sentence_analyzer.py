def sentence_analyzer(sentence):
    '''
    A function that takes in a line of text and ouputs a dictionary with each
each letter as a key, the value being the frequency of appearance of the letter.

    sentence_analyzer("Pythonn")
>>> {
  "P": 1,
  "y": 1,
  "t": 1,
  "h": 1,
  "o": 1
  "n": 2
}
    '''
    solution={}
    for char in sentence:
        if char != '':
            if char in solution:
                solution[char] += 1
            else:
                solution[char] = 1
    
    return solution
