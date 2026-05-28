import nltk
from nltk.chat.util import Chat, reflections

reflections = {
    "i am"    : "you are",
    "i was"   : "you were",
    "i"       : "you",
    "i 'm"    : "you are",
    "i' d"    : "you would", 
    "i've"    : "you have", 
    "i'll"    : "you will",
    "my"      : "your",
    "you are" : "I am",
    "you were" : "I was",
    "you've"  : "I have",
    "you'll"  : "I will",
    "your"    : "my",
    "yours"   : "mine", 
    "you"     : "me", 
    "me"      : "you" 
}

pairs = [
    [
        r"Me name is Haaland", 
        ["Hello Haaland, How are you today ?"]
    ],
    [
        r"Hi|hey|Hello",
        ["Hello", "Hey there,"]
    ],
    [
        r"What is your name?",
        ["I am a bot created by you. You can call me Jarvis"]
    ],
    [
        r"How are you ?",
        ["I am doing good and How about you?"]
    ],
    [
        r"Sorry Haaland",
        ["It's okay, no need to apologize."]
    ],
    [
        r"I am fine, thank you",
        ["Great to hear that! How can I assist you today?"]
    ],
    [
        r"I'm Haaland doing good",
        ["Nice to hear that", "How can I help you today?"]
    ],
    [
        r"Haaland age?",
        ["I'm a computer to program duden and seriously you are asking me this?"]
    ],
    [
        r"What Haaland want?", 
        ["Make me an offer I can 't refuse"]
    ],
    [
        r"Haaland created?",
        ["Haaland created me using Python s' NLTK liberary","It 's a top secret"]
    ],
    [
        r"Haaland (locaation|live|city)?",
        ["Leeds, West Yorkshire, England"]
    ],
    [
        r"Who Haaland sportsperson?",
        ["Messy, Ronaldo, Neymar, Mbappe, Bruno and many more"]
    ],
    [
        r"Who Haaland (moviestar|actor)?",
        ["Micheal Jackson"]
    ],
    [
        r"I am looking for online guides and course to learn about football",
        ["Jarvis_Tech has many great articles with each step explanation and pratically explains with Mbappe"]
    ],
    [
        r"By the way what is going on with Mbappe?",
        ["Mbappe is doing great and he is ery dedicated, active and focuse towards his goals and aim", "Only TWO SHOTS are left for him to score in his entire career", "The LAST TWO SHOTS will decide his fate and whom will he end"]
    ],
    [
        r"Will Mbappe succed in his goals or need ASSIST for this?",
        ["Well I don t' think so because Mbappe is very dedicated towards his goals for like about an year and will succed one day", "Soon that day might come or will not", "It has a 30-70 probability"]
    ],
    [
        r"Thank you Jarvis",
        ["You are welcome! If you have any more questions, feel free to ask."]
    ],
    [
        r"Bye|Goodbye",
        ["Goodbye! Have a great day!"]
    ],
]

def chat():
    print("Hi! I'm Jarvis and I am here to assist you with your football related queries. Type 'Bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    chat()    