import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print("You:", command)
            return command.lower()

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Speech service is unavailable.")
            return ""

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak("Current time is " + current_time)

def tell_date():
    current_date = datetime.datetime.now().strftime("%d %B %Y")
    speak("Today's date is " + current_date)

def search_google():
    speak("What do you want to search?")
    query = listen()

    if query != "":
        url = "https://www.google.com/search?q=" + query
        webbrowser.open(url)
        speak("Opening Google search for " + query)

def main():
    speak("Hello! I am your voice assistant.")

    while True:

        command = listen()

        if command == "":
            continue

        elif "hello" in command:
            speak("Hello! Nice to meet you.")

        elif "time" in command:
            tell_time()

        elif "date" in command:
            tell_date()

        elif "search" in command:
            search_google()

        elif "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I don't know that command.")

if __name__ == "__main__":
    main()