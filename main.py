import subprocess
import wolframalpha
import pyttsx3
# import tkinter
import json
# import random
# import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
# import winshell

# import feedparser
import smtplib
import ctypes
import time
import requests
# import shutil

# from client.textui import progress
# from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice[0].id)
engine.setProperty('voice',voice[1].id)

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

def takeCommand():
   r=sr.Recognizer()
   with sr.Microphone() as source:
         print("Listening...")
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
if _name=="main_":
  wishMe()
  while(True):
          
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

     #    elif 'news' in query:
             
     #        try:
     #            jsonObj = urlopen('''https://www.indiatoday.in/''')
     #            data = json.load(jsonObj)
     #            i = 1
                 
     #            speak('here are some top news')
                                 
     #            for item in data['articles']:
                     
     #                print(str(i) + '. ' + item['title'] + '\n')
     #                print(item['description'] + '\n')
     #                speak(str(i) + '. ' + item['title'] + '\n')
     #                i += 1
     #        except Exception as e:
                 
     #            print(str(e))   

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

     #    elif "weather" in query:
                 
     #        # Google Open weather website
     #        # to get API of Open weather
     #        api_key = "Api key"
     #        base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
     #        speak(" City name ")
     #        print("City name : ")
     #        city_name = takeCommand()
     #        complete_url = base_url + "appid =" + api_key + "&q =" + city_name
     #        response = requests.get(complete_url)
     #        x = response.json()
             
     #        if x["cod"] != "404":
     #            y = x["main"]
     #            current_temperature = y["temp"]
     #            current_pressure = y["pressure"]
     #            current_humidiy = y["humidity"]
     #            z = x["weather"]
     #            weather_description = z[0]["description"]
     #            print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
     #        else:
     #            speak(" City Not Found ")    

        elif "wikipedia" in query:
                webbrowser.open("wikipedia.com") 

        elif "i love you" in query:
            speak("It's hard to understand, love is complicated these days")

        elif "what is" in query or "who is" in query:
             
            
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")  
        elif 'lock window' in query:
                speak("doing it right way")
                ctypes.windll.user32.LockWorkStation()
 
     #    elif 'shutdown system' in query:
     #            speak("Give me few seconds")
     #            subprocess.call('shutdown / p /f')