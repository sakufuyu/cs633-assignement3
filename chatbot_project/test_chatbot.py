"""
Required:

pip install chatterbot
pip install chatterbot-corpus
python -m spacy download en_core_web_sm
"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a new chatbot
chatbot = ChatBot("TestBot")

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot
trainer.train("chatterbot.corpus.english")

# Implement simple chat
print("Simple chat begins. To quit, enter 'quit'")
user_input = ""

while (user_input != "quit"):
    user_input = input("You: ")

    response = chatbot.get_response(user_input)
    print(f"Bot: {response}")
