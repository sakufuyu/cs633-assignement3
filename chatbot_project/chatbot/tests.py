from django.test import TestCase, Client
from django.urls import reverse
from .bot import ChatBotManager


class ChatBotTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.chatbot = ChatBotManager()

    def test_bot_response(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "chatbot/home.html")

    def test_api_endpoint(self):
        response = self.client.post(
            reverse("get_bot_response"),
            {"user_input": "Hello!"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.json())
