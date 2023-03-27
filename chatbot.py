import random

class Chatbot:
    def __init__(self):
        self.keywords = {
            "dad": "family",
            "mom": "family",
            "brother": "family",
            "sister": "family",
            "dog": "pets",
            "cat": "pets",
            "no": "negative",
        }
        self.responses = {
            "family": ["Tell me more about your family.", "What does your family mean to you?", "How do you feel about your family?"],
            "pets": ["Tell me more about your pets.", "What kind of pets do you have?", "How long have you had your pets?"],
            "negative": ["Why so negative?", "Is there anything positive you can focus on?", "Let's try to stay positive!"],
            "teacher": ["He sounds like a good teacher.", "You're lucky to have a teacher like him.", "What's your favorite thing about his class?"],
            "noncommittal": ["I see.", "Interesting.", "Tell me more.", "That's good to know.", "Thanks for sharing."]
        }
        self.good_teacher_names = ["Finkelstein", "Johnson", "Lee"]
        
    def process_input(self, statement):
        statement = statement.strip().lower()
        
        if not statement:
            return "Say something, please."
        
        if statement == "bye":
            return "Goodbye!"
        
        found_keyword = False
        for word in statement.split():
            if word in self.keywords:
                found_keyword = True
                category = self.keywords[word]
                if category == "family":
                    return random.choice(self.responses["family"])
                elif category == "pets":
                    return random.choice(self.responses["pets"])
                elif category == "negative":
                    return random.choice(self.responses["negative"])
                
        if not found_keyword:
            for name in self.good_teacher_names:
                if name.lower() in statement:
                    response = random.choice(self.responses["teacher"])
                    response = response.replace("him", name)
                    response = response.replace("his", name + "'s")
                    return response
            
            return random.choice(self.responses["noncommittal"])
        
        return "Wait a moment!"

chatbot = Chatbot()

print("Hi, how are you? This is Chatbot Q.")
print("I can answer all your questions.")

while True:
    statement = input("You>> ")
    response = chatbot.process_input(statement)
    print("Q>>", response)
    if response == "Goodbye!":
        break
