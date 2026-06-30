import random
import string
# import json

#moving the responses dictionary to json
# json.dumps(responses)


#saving the conversation history in a .txt file using open() and .write()
file = open('get_response', 'w')

file.write('get_response')

file.close()
responses = {
    "hello": ["Hey there", "Hello! How can I help?", "Hi! Great to see you."],
    "hi": ["Hey!", "Hello!", "Hi there!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "how are you": ["I'm doing well, thanks!", "Running smoothly!", "All good on my end."],
    "help": ["Sure, I can help. What do you need?", "I'm here to assist. What's up?"],
    "name": ["I'm ChatBot, your rule-based assistant.", "You can call me ChatBot!"],
    "weather": ["I can't check the weather yet, but that's a great upgrade idea!"],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
    ],
    "sports": ["Forms of exercise done to keep fit!", "Badminton, football, tennis, squash, basketball etc."],
    "food": ["Food is any substance consumed by an organism for nutritional support.", "This includes meat, eggs, shellfish and dairy products like milk and cheese."],
    "python": ["Python is a programming language that lets you work quickly!", "Friendly & Easy to Learn!", "Calculations are simple with Python!"],
    "technology": ["An emerging field with different niches.", " technology is broud", "A field that interest almost everyone."]
}



fallback = [
    "Hmm, I'm not sure about that one.",
    "I don't have a response for that yet.",
    "Could you rephrase that? I'm still learning!",
]

asked_before = set()

def clean_input(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.strip()

def get_response(user_input):
    cleaned = clean_input(user_input)
    for keyword, replies in responses.items():
        if keyword in cleaned:
            if keyword in asked_before:
                return f"You already asked about '{keyword}'! But here's another take: " + random.choice(replies)
            else:
                asked_before.add(keyword)
                return random.choice(replies)
    return random.choice(fallback)

def run_chatbot():
    print("Otuwose: Hello! Type 'quit' to exit.\n")

    history = []            # stores conversation as a text

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Otuwose: Goodbye! Closing now.")
            history.append("You: quit")
            history.append("Otuwose: Goodbye! Closing now.")
            break
        reply = get_response(user_input)
        print(f"Otuwose: {reply}\n")

        history.append(f"You: {user_input}")
        history.append(f"Otuwose: {reply}")

        file = open("conversation_history.txt", "w")
        file.write("\n".join(history))
        file.close()
        print("Conversation saved to conversation_history.txt")

run_chatbot()
