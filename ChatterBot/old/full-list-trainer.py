from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
import re

chatbot = ChatBot(
    'ListTrainer',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        }
    ],
    database_uri='sqlite:///full-list-trainer.sqlite3'
)

trainer = ListTrainer(chatbot)

chosenJokes = []
count = 0
with open('stupidstuff.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
    for joke in data:
        if (joke['rating'] > 3 and len(joke['body']) < 70 and joke['category'] != 'Blonde Jokes'):
            chosenJokes.append("Tell me a joke")
            chosenJokes.append(joke['body'])
        
        count+=1
    

# with open('wocka.json', encoding="utf-8") as json_file:
#     data = json.load(json_file)
#     for joke in data:
#         if (len(joke['body']) < 70 and not ('Blond' in joke['category']) ):
#             chosenJokes.append( re.sub(r'[^\x00-\x7F]+',' ', joke['body'].replace('\r', "").replace('\n', "")))
        
#         count+=1
    
trainer.train(chosenJokes)
trainer.export_for_training('./full_list_trainer.json')

# # The following loop will execute each time the user enters input
# while True:
#     try:
#         user_input = input(">> ")

#         bot_response = chatbot.get_response(user_input)

#         print(bot_response)

#     # Press ctrl-c or ctrl-d on the keyboard to exit
#     except (KeyboardInterrupt, EOFError, SystemExit):
#         break

