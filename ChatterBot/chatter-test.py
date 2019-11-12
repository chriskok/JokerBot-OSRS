from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new instance of a ChatBot
# chatbot = ChatBot(
#     'Terminal',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     # logic_adapters=[
#     #     {
#     #         'import_path': 'chatterbot.logic.BestMatch'
#     #     }
#     # ],
#     database_uri='sqlite:///chatter-test.sqlite3'
# )

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train('chatterbot.corpus.english.greetings', "./data/test.yaml")

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input(">> ")

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break