import json


chosenJokes = []
count = 0
with open('stupidstuff.json') as json_file:
    data = json.load(json_file)
    for joke in data:
        if (joke['rating'] > 3 and len(joke['body']) < 70 and joke['category'] != 'Blonde Jokes'):
            chosenJokes.append(joke['body'])
        
        count+=1
    
print("{} out of {}".format(len(chosenJokes), count))

print("CHOSEN STUPID STUFF JOKES")
for i in range(40):
    print(chosenJokes[i])

print("\n\n")

chosenJokes = []
count = 0
with open('wocka.json') as json_file:
    data = json.load(json_file)
    for joke in data:
        if (len(joke['body']) < 70 and not ('Blond' in joke['category']) ):
            chosenJokes.append( joke['body'].replace('\r', "").replace('\n', "") )
        
        count+=1
    
print("{} out of {}".format(len(chosenJokes), count))

print("CHOSEN WOCKA JOKES")
for i in range(40):
    print(chosenJokes[i])