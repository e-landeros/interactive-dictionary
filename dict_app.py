import json
from difflib import get_close_matches
#data.json file is key, value pair of dictionary words and their meanings.
#some words have multiple definitions, separated by comma

#1. transform json file into python dictionary object with json library
data = json.load(open("data.json"))

def translate(w):
    #clean input string to lower case
    w = w.lower()
    #user enters exact word returns v for k
    if w in data:
        return data[w]
    #check for close matches and recommend a word, default .7 corr cutoff
    elif len(get_close_matches(w, data.keys())) > 0:
        #input so user doesnt exit program. return 1st closest match only
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return "The word does not exist. Please double check spelling. "
        else:
            return "I did not understand your entry. goodbye."
    #reccomendations arebeyond threshold and no matches
    else:
        return "The word does not exist. Please double check spelling. "

# Clean up input strings from user - built into translate function
word = input('Enter word: ')

output = translate(word)

#list returned from program
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
