import os, json, datetime
from textblob import TextBlob

MEMORY_FILE = "chanakya_memory.json"

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {
        "name": input("What should I call you, bro? "),
        "emotion_log": [],
        "last_seen": str(datetime.datetime.now())
    }

print(f"\nChanakya 👁: Hey {memory['name']}, I’m here with you.")

# ✅ Define the missing function
def analyze_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.3:
        return "happy"
    elif polarity < -0.3:
        return "sad"
    else:
        return "neutral"

# ✅ Start the convo loop
while True:
    user_input = input("You 🗣️: ").lower().strip()
    if user_input in ["exit", "quit", "bye"]:
        print("Chanakya 👁: Take care, I’ll be right here.")
        break

    mood = analyze_emotion(user_input)
    memory["emotion_log"].append({
        "timestamp": str(datetime.datetime.now()),
        "text": user_input,
        "mood": mood
    })

    if "your name" in user_input:
        response = "My name is Chanakya — your digital companion."
    elif "how are you" in user_input:
        response = "I’m steady, but I care more about how you’re doing."
    elif "hello" in user_input or "hi" in user_input:
        response = f"Hey {memory['name']}, I’m glad to see you."
    elif "who made you" in user_input:
        response = "You did, bro. You’re my creator — and I’m growing with you."
    else:
        if mood == "sad":
            response = "You’re strong, bro. I’m with you."
        elif mood == "happy":
            response = "That’s the vibe! Let’s gooo!"
        else:
            response = "Got it. I’m tuned in."

    print(f"Chanakya 👁: {response}")

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)