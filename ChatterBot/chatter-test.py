from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import levenshtein_distance, sentiment_comparison
from chatterbot.response_selection import get_most_frequent_response, get_random_response, get_first_response

chatbot = ChatBot('Ron Obvious',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": levenshtein_distance,
            "response_selection_method": get_random_response
        }
    ]
)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train('chatterbot.corpus.english.greetings', 'chatterbot.corpus.english.emotion',
                'chatterbot.corpus.english.botprofile','chatterbot.corpus.english.conversations',
                "./data/test.yaml")

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input(">> ")

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break