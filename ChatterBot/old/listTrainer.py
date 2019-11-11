from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json



chatbot = ChatBot(
    'ListTrainer',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        }
    ],
    database_uri='sqlite:///list-trainer.sqlite3'
)

trainer = ListTrainer(chatbot)

allJokesAbove3 = []
count = 0
with open('stupidstuff.json') as json_file:
    data = json.load(json_file)
    for joke in data:
        if (joke['rating'] > 3):
            allJokesAbove3.append(joke['body'])
        
        count+=1
    
print("{} out of {}".format(len(allJokesAbove3), count))

# trainer.train([
#     "Hi there!",
#     "Hello",
# ])

trainer.train(allJokesAbove3)

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input(">> ")

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

# Now we can export the data to a file
trainer.export_for_training('./list_trainer.json')