class RuleBasedChatbot:
    def __init__(self):
        self.rules = {
            "hello": "Hello! How can I assist you today?",
            "how are you": "I'm just a chatbot, but I'm here to help!",
            "bye": "Goodbye! Have a great day!",
            "default": "I'm not sure how to respond to that."
        }

    def get_response(self, message):
        message = message.lower()
        response = self.rules.get(message, self.rules["default"])
        return response

chatbot = RuleBasedChatbot()

print("Rule-Based Chatbot: Hi there! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Rule-Based Chatbot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("Rule-Based Chatbot:", response)
