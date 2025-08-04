from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class ChatBotManager:
    def __init__(self):
        self.chatbot = ChatBot("CS633Assignment3")
        self._train_bot()

    def _train_bot(self):
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train("chatterbot.corpus.english")

    def get_response(self, user_input):
        return self.chatbot.get_response(user_input)
