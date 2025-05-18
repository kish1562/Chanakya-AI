import datetime
import os
import json
from textblob import TextBlob

MEMORY_FILE = "memory.json"

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {
        "name": input("What should I call you, bro? "),
        "emotion_log": [],
        "last_seen": str(datetime.datetime.now())
    }

print(f"\nHey {memory['name']}, I’m here for you.")

def analyze_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    else:
        return "neutral"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "bye", "quit"]:
        print("AI: Catch you later, bro!")
        break

    mood = analyze_emotion(user_input)
    memory['emotion_log'].append({
        "timestamp": str(datetime.datetime.now()),
        "text": user_input,
        "mood": mood
    })

    print(f"AI: Got it. You seem {mood} today.")
    if mood == "sad":
        print("AI: Whatever it is, you’ll get through it. I got you.")
    elif mood == "happy":
        print("AI: Love that energy, bro!")
    else:
        print("AI: Let’s keep pushing forward together.")

with open(MEMORY_FILE, "w") as f:
    json.dump(memory, f, indent=2)
