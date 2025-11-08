import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("🎤 Speak your command...")
    audio = r.listen(source)

try:
    command = r.recognize_google(audio).lower()
    print("🗣️ You said:", command)
    if "stock" in command:
        print("📦 Checking stock data...")
    elif "forecast" in command:
        print("📈 Fetching forecast...")
    else:
        print("🤖 Command not recognized.")
except:
    print("❌ Could not recognize speech.")
