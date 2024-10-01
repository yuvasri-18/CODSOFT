def chatbot():
    print("Hello! I am your chatbot. Type 'quit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing well, thank you!")
        elif 'your name' in user_input:
            print("Chatbot: I am a simple chatbot.")
        elif 'bye' in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")
chatbot()