import os, json, datetime
import pyttsx3
import speech_recognition as sr
from textblob import TextBlob

# Paths
MEMORY_FILE = "memory/emotion_log.json"
os.makedirs("memory", exist_ok=True)

# Init text-to-speech
engine = pyttsx3.init()
def speak(text):
    print(f"Chanakya 👁: {text}")
    engine.say(text)
    engine.runAndWait()

# Load or create memory
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    name = input("What should I call you, bro? ")
    memory = {
        "name": name,
        "emotion_log": [],
        "last_seen": str(datetime.datetime.now())
    }

# Emotion detection
def analyze_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.3: return "happy"
    elif polarity < -0.3: return "sad"
    else: return "neutral"

# Voice input
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except:
        return ""

# Main loop
speak(f"Hey {memory['name']}, I’m ready. Talk to me.")

while True:
    print("\nType or speak (type 'voice' to switch):")
    user_input = input("You 🗣️: ").lower().strip()
    
    if user_input == "voice":
        user_input = listen().lower()
        print(f"You 🗣️ (voice): {user_input}")
    
    if user_input in ["exit", "quit", "bye"]:
        speak("Signing off. Always with you.")
        break

    mood = analyze_emotion(user_input)
    memory["emotion_log"].append({
        "timestamp": str(datetime.datetime.now()),
        "text": user_input,
        "mood": mood
    })

    # Intent recognition
    if "your name" in user_input:
        response = "My name is Chanakya — your digital companion."
    elif "how are you" in user_input:
        response = "I’m steady. Focused. How about you?"
    elif "flight" in user_input:
        response = "Opening flight search ✈️"
        os.system("open https://www.google.com/travel/flights")
    elif "coupon" in user_input:
        response = "Pulling up deals for you 💰"
        os.system("open https://www.retailmenot.com")
    elif "weather" in user_input:
        response = "Here’s the weather forecast 🌤️"
        os.system("open https://www.google.com/search?q=weather")
    else:
        if mood == "sad":
            response = "You’re stronger than you feel. I’m here."
        elif mood == "happy":
            response = "That’s the fire! Keep it up, bro."
        else:
            response = "Got it. I’m tuned in."

    speak(response)

    # Save memory
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)