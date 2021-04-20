import json

# Loading json data file
data = json.load(open('data.json'))
#print(data)

# getting meaning for a particular word.
#print(data['rain'])


def translate(word_mean):

    if word_mean in data:
        return data[word_mean]
    else:
        return "Word Not Found"


word = input("Enter Word: ")
print(translate(word.lower()))
