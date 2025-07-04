# Simple Rule-Based Chatbot using if-else

print("Hello! I'm SURBHI'S_BOT. Type 'bye' to end the chat.")

while True:
    user_input = input("You: ").lower()  # Convert input to lowercase for easier matching

    if user_input == 'bye':
        print("SURBHI'S_BOT: Goodbye! Have a great day!")
        break
    elif 'hello' in user_input or 'hi' in user_input:
        print("SURBHI'S_BOT: Hello there! How can I help you?")
    elif 'how are you' in user_input:
        print("SURBHI'S_BOT: I'm just a bunch of code, but I'm doing great! How about you?")
    elif 'your name' in user_input:
        print("SURBHI'S_BOT: I'm SURBHI'S_BOT, your friendly chatbot.")
    elif 'help' in user_input:
        print("SURBHI'S_BOT: Sure! You can ask me about the weather, my name, or how I’m doing.")
    elif 'weather' in user_input:
        print("SURBHI'S_BOT: I can't check the weather yet, but it's always sunny in the world of code!")
    elif 'thanks' in user_input or 'thank you' in user_input:
        print("SURBHI'S_BOT: You're welcome!")
    else:
        print("SURBHI'S_BOT: I'm not sure. Try asking something else!")

