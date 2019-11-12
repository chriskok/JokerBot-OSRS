from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import levenshtein_distance, sentiment_comparison
from chatterbot.response_selection import get_most_frequent_response, get_random_response, get_first_response
import socket 

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

def changeString(myString):
    newString = myString + " - CHANGED\r\n"

    return newString

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 9876              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
conn, addr = s.accept()
print ('Connected by', addr)

while 1:

    try:
        data = conn.recv(1024)
        decodedRequest = data.decode("utf-8")

        if not data: break
        print( "request: {}".format(decodedRequest) )

        bot_response = chatbot.get_response(decodedRequest)
        print("response: {}".format(bot_response) )

        conn.sendall(str.encode(bot_response)) # turn it back into bytes 

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
    
conn.close()
