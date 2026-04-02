from nltk.chat.util import Chat, reflections

# Assignment Requirement: Modify at least 5 rules or response patterns [cite: 22]
pairs = [
    (r"I need (.*)", ["Why do you need %1?", "Would getting %1 really help you?", "How soon do you need %1?"]),
    
    # Custom Rule 1: Specific response for Exam Stress [cite: 30]
    (r"I (.*) exams", ["Exams can be stressful. Have you prepared well for %1?", "What is the most difficult part about these exams?"]),
    
    # Custom Rule 2: Personalized Name Greeting [cite: 27]
    (r"My name is (.*)", ["Hello %1! How can I help you today?", "Nice to meet you, %1. What's on your mind?"]),
    
    # Custom Rule 3: Handling feelings of being tired [cite: 29]
    (r"I am tired", ["I'm sorry to hear that. Are you getting enough sleep?", "Does your exhaustion come from physical or mental stress?"]),
    
    # Custom Rule 4: Academic pressure / Strict parents [cite: 31]
    (r"My (.*) is strict", ["How does your %1's strictness affect you?", "What do you wish your %1 would do differently?"]),
    
    # Custom Rule 5: Career and Future worry
    (r"I am worried about (.*)", ["What about %1 causes you the most concern?", "Do you have a plan to address your worries regarding %1?"]),
    
    (r"quit", ["Goodbye! It was nice talking to you.", "See you later!"]),
    (r"(.*)", ["Please tell me more.", "How does that make you feel?", "I see. Go on."])
]

def get_eliza_response(user_input: str) -> str:
    chat = Chat(pairs, reflections)
    response = chat.respond(user_input)
    return response if response else "I am not sure I understand."

if __name__ == "__main__":
    print("ELIZA Chatbot (Custom Rule-Based)")
    print("Type 'quit' to stop.\n")
    chat = Chat(pairs, reflections)
    chat.converse()