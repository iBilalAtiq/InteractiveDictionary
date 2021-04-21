import json
from difflib import SequenceMatcher, get_close_matches

# Loading json data file
data = json.load(open('data.json'))
#print(data)

# getting meaning for a particular word.
#print(data['rain'])


def translate(word_mean):

    word_lower = word_mean.lower()
    similarity = get_close_matches(word_lower, data.keys())[0]
    if word_lower in data:
        if word_lower == similarity:
            print(f"{similarity}")
        return data[word_lower]
    else:
        return "Word Not Found"


word = input("Enter Word: ")
print(translate(word))
