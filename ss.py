from tkinter import *
from tracemalloc import start
# import tkinter.font
from turtle import width 
# from tkinter.ttk import *
# from turtle import onclick
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
# import wolframalpha
# import smtplib
# import pyjokes
    
    
# writing code needs to
# create the main window of 
# the application creating 
# main window object named root
root = Tk()
  
# giving title to the main window
root.title("Virtual Assistant")




#import pywhatkit
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice[0].id)
engine.setProperty('voice',voice[1].id)

rate = engine.getProperty('rate')   # getting details of current speaking rate
              
engine.setProperty('rate', 145)  
def speak(audio):
     engine.say(audio)
     engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)



def wishMe():
     hour= int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak("Good Morning")

     elif hour>=12 and hour<18:
           speak("Good Afternoon")        
     else:
          speak("Good Evening")     

     speak("Winsey here, how may I help you") 
     
     
     
     i=1
     while(i<3):
          
        query = takeCommand().lower()
        if "wikipedia" in query:
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query)
          speak(results)

        elif 'youtube' in query:
             webbrowser.open("youtube.com")

        elif 'google' in query:
             webbrowser.open("google.com")  
        elif 'stack overflow' in query:
             webbrowser.open("stackoverflow.com")    
  
        elif 'podcats' in query:
            webbrowser.open("podcasts.google.com")
       
        elif 'translate' in query:
             webbrowser.open("translate.google.co.in")    
  
     #    elif 'search' in query or 'play' in query:             
     #      #   query = query.replace("search", "")
     #      #   query = query.replace("play", "")         
     #      #   webbrowser.open(query)
     #      query = query.replace("play","")
     #      song = query.replace("play","")
     #      pywhatkit.playonyt(song)

          #pywhatkit.playonyt(song)

        elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"The Time {strTime}")  

        elif "calculate" in query:             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)     

        elif 'send a mail' in query:
           try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
           except Exception as e:
                print(e)
                speak("I am not able to send this email")             
     
        elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

        elif 'joke' in query:
                speak(pyjokes.get_joke())      

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")    

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        i+=1
    

def takeCommand():
   r=sr.Recognizer()
   with sr.Microphone() as source:
        print("Listening...")
        Label(root, text = "Listening").place(x = 40, y = 60)
        r.pause_threshold = 1
        audio= r.listen(source)
   try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')    
        print(f"User Said:{query}\n")
          
   except Exception as e:
       # print(e)
        print("Say That Again Please...")
        return "None"      
   return query 




# Label is what output will be 
# show on the window
# helv36 = tk.Font(family="Helvetica",size=36,weight="bold")

label = Label(root, text ="Hey am Winsey!!!", font=("ubuntu",30), fg="#900C3F", pady=250, padx=50).pack()
  
img = PhotoImage(file='pics/1.png')

 
main_button = Button(root, image=img, width=70, height=70, fg="white", bg="#F0F0F0", bd=0, command=wishMe)
main_button.place(relx=0.5, rely=0.8, anchor=CENTER)
# user_name = Label(root, text = "Username").place(x = 40, y = 60)

# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying


root.mainloop()

# if __name__=="__main__":
#   wishMe()
 
