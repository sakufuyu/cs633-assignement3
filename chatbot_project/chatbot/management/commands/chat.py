from django.core.management.base import BaseCommand
from chatbot.bot import ChatBotManager


class Command(BaseCommand):
    help = "Starts a chat bot session"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("###### Chatbot activating... #####\n"))
        manager = ChatBotManager()

        self.stdout.write("Bot: Hi! How can I assist you today? To quite, enter 'quit'!")
        while (True):
            user_input = input("You: ")

            if (user_input.lower() == "quit"):
                self.stdout.write("Bot: Good bye...😢")
                break
            response = manager.get_response(user_input)
            self.stdout.write(f"Bot: {response}")
