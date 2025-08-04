from django.shortcuts import render
from django.http import JsonResponse
from .bot import ChatBotManager


chatbot_manager = ChatBotManager()

def home(request):
    return render(request, "chatbot/home.html")


def get_bot_response(request):
    if (request.method == "POST"):
        user_input = request.POST.get("user_input", "")
        response = chatbot_manager.get_response(user_input)
        return JsonResponse({"response": str(response)})
    return JsonResponse({"error": "Invalid request"}, status=400)
