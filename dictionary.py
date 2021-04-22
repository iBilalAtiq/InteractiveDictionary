import json
from difflib import get_close_matches

# Loading json data file
data = json.load(open('data.json'))


# print(data)

# getting meaning for a particular word.
# print(data['rain'])


def translate(word_mean):
    word_lower = word_mean.lower()
    similarity = get_close_matches(word_lower, data.keys())[0]
    if word_lower in data:
        return data[word_lower]
    elif len(similarity) > 0:
        print(f"Did you mean {similarity}? If yes type Yes else No")
        user_input = input("Yes or No: ")
        if user_input.lower() == 'yes':
            print(data[similarity])
        elif user_input.lower() == 'no':
            return "Word does not exist"
        else:
            return "Word not found"
    else:
        return "Word does not exist"


word = input("Enter Word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
    else:
        print(output)
