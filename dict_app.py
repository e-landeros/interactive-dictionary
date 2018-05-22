import json
#data.json file is key, value pair of dictionary words and their meanings.
#some words have multiple definitions, separated by comma

#1. transform json file into python dictionary object with json library
data = json.load(open('data.json'))

def translate(w):
    #clean input string to lower case
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word does not exist. Please double check spelling. "

# Clean up input strings from user, Case,
word = input('Enter word: ')

print(translate(word))
