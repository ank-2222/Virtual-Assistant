import ctypes
import smtplib
from tkinter import *
import pyttsx3
from googlesearch import search
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

root = Tk()

root.title("Virtual Assistant")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")

    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Gray here, how are you? ")
    print("List of Task you can ask for :-)")
    print(
        """
        • Wish the User (default): 
        • Ask him “How are You” and try to answer with I’m good
        •Search anything in google
        • Search anything in Wikipedia (e.g.: - MS Dhoni in Wikipedia):
        • Open YouTube (gray open YouTube, works in Hindi to)
        • Ask him what is the time, hope he is not busy to answer
        • Ask him to write note • Ask him to locate any place
        • Want to lock the window, he can do that to just ask “gray Lock Window”
        • To terminate the code say-“exit”
          """
    )
    i = 1
    while i < 6:

        query = takeCommand().lower()

        if "wikipedia" in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query)
            speak(results)
        elif "search" in query:
            x = query.replace("search", "")
            search(x)
            webbrowser.open(x)
        elif "youtube" in query:
            webbrowser.open("youtube.com")

        elif "google" in query:
            webbrowser.open("google.com")
        elif "stack overflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "podcats" in query:
            webbrowser.open("podcasts.google.com")

        elif "translate" in query:
            webbrowser.open("translate.google.co.in")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time {strTime}")

        elif "how are you" in query:
            speak("I am fine, Thank you")
            speak("How are you")

        elif "fine" in query or "good" in query:
            speak("It's good to know that your fine")

        elif "exit" in query:
            speak("Thanks for giving me your time")
            exit()

        elif "write a note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open("text.txt", "w")
            speak("Should i include date and time")
            snfm = takeCommand()
            if "yes" in snfm or "sure" in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "i love you" in query:
            speak("It's hard to understand, love is complicated these days")

        elif "lock window" in query:
            speak("doing it right way")
            ctypes.windll.user32.LockWorkStation()

        i += 1


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say That Again Please...")
        return "None"
    return query


Label(
    root, text="Hey am Gray!!!", font=("ubuntu", 30), fg="#900C3F", pady=250, padx=50
).pack()

img = PhotoImage(file="pics/1.png")

main_button = Button(
    root, image=img, width=70, height=70, fg="white", bg="#F0F0F0", bd=0, command=wishMe
)
main_button.place(relx=0.5, rely=0.8, anchor=CENTER)
# user_name = Label(root, text = "Username").place(x = 40, y = 60)
# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying
root.mainloop()
