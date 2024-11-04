import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init()
engine.setProperty('rate', 120) 

def speak(text):
    engine.say(text + "...")
    engine.runAndWait()

def Listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry, I did not catch that. Could you please repeat?...")
        speak("Sorry, I did not catch that. Could you please repeat?...")
        return None
    return query.lower()

def respond_to_greetings():
    speak("Hello! How can I assist you today?...")

def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {current_time}...")

def tell_date():
    today = datetime.date.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}...")

def search_wikipedia(query):
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia...")
    speak(results)

def web_search(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    speak(f"Here are the search results for {query}...")

def main():
    speak("Welcome to Voice assist...")
    while True:
        query = Listen()
        
        if query is None:
            continue
        
        if "hello" in query:
            respond_to_greetings()

        elif "time" in query:
            tell_time()

        if "date" in query:
            tell_date()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            search_wikipedia(query)

        elif "stop" in query or "exit" in query or "quit" in query or "close" in query:
            speak("Goodbye! Have a great day ahead.")
            break
        
        elif ("wikipedia" not in query and "time" not in query and "date" not in query and "hello" not in query) or ("search" in query or "web" in query):
            search_query = query.replace("search", "").strip()
            speak(f"Searching the web for {search_query}")
            web_search(search_query)

if __name__ == "__main__":
    main()
