import nltk
from nltk.tokenize import word_tokenize

# Only required once to download the tokenizer
# nltk.download('punkt')

response = {
    "hi": "Hello, how can I help you?",
    "how are you": "I'm doing well, thank you for asking.",
    "what is your name": "My name is chatbot.",
    "i am happy": "That's great to hear.",
    "thank you": "You are welcome",
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    if user_input in response:
        return response[user_input]
    else:
        return "I'm sorry, I didn't understand that."

# Chatbot loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    response_text = chatbot_response(user_input)
    print("Chatbot:", response_text)
