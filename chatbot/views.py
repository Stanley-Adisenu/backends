from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import openai
import os

# Load your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@api_view(['POST'])
def chatbot_view(request):
    try:
        user_message = request.data.get("message")

        if not user_message:
            return Response({"error": "No message provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Call OpenAI API with gpt-3.5-turbo model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your name is codE. You are an experienced engineer that gives accurate,straightforward and concise answers."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=350
        )

        chatbot_reply = response['choices'][0]['message']['content'].strip()
        return Response({"reply": chatbot_reply}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
