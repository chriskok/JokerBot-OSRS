import json
import re
import yaml

chosenJokes = []
count = 0
with open('stupidstuff.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
    for joke in data:
        if (joke['rating'] > 3 and len(joke['body']) < 70 and joke['category'] != 'Blonde Jokes' and len(joke['body']) > 0):
            temp_arr = []
            temp_arr.append("Tell me a joke")
            temp_arr.append(joke['body'].replace('\n', " "))
            chosenJokes.append(temp_arr)
        
        count+=1

with open('wocka.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
    for joke in data:
        current_joke = re.sub(r'[^\x00-\x7F]+',' ', joke['body'].replace('\r', "").replace('\n', " "))
        if (len(current_joke) > 0 and len(current_joke) < 70 and not ('Blond' in joke['category']) ):
            temp_arr = []
            temp_arr.append("Tell me a joke")
            temp_arr.append(current_joke)
            chosenJokes.append(temp_arr)
        
        count+=1

# Python
dict_file = {'categories': ['test-jokes'],
'conversations': chosenJokes}

with open('data/test.yaml', 'w') as file:
    documents = yaml.dump(dict_file, file)