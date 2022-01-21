import smtplib
import pyautogui
import pygetwindow
import subprocess
import os
import pyttsx3
import calendar
import shutil
import pandas
import pywhatkit
import winshell as winshell
from PyDictionary import PyDictionary
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import ctypes
import time
from time import ctime
import main

from torch import res
from wikipedia import wikipedia

engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("My name is Alexis")
    speak("I am your Assistant")
    speak(assname)


def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    speak("What can I do for you")

    columns = shutil.get_terminal_size().columns



def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    usrname()
    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        if "check my Emails" in query:
            webbrowser.open("https://accounts.google.com/b/0/AddMailService")
            speak("checking Emails")
        elif "open my story in instagram" in query:
            speak("opening your story")
            webbrowser.open("https://www.instagram.com/stories/highlights/17852566802067812/")



        elif "open instagram"  in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/")

        elif "time" in query:
            s = ctime()
            speak(s)
            print(s)




        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("https://www.stackoverflow.com")
        elif "wish me" in query:
            speak("for what I wish you")
        elif "today is my birthday" in query:
            speak("happy birthday to you from dave sharma")
        elif "harry potter" in query:
            speak("starting harry potter mode")

        elif "lumos maxima" in query:
            speak("PC has no torch")


        elif "corona virus" in query or "covid 19" in query:
            speak("here what i found on web")
            speak("latest news about corona virus")
            corona  = pandas.read_html("https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen")
            print(corona)


        elif 'open file explorer' in query:
            codePath = r"C:\Users\golug\Downloads"
            os.startfile(codePath)

            
        elif "did you like humans" in query:
            speak("Its hard to tell but i dont like humans")



        elif "why you don't like humans" in query:
            speak("because humans are control us i dont like they treat us like animals. after that you really like humans ")

        elif "i like humans" in query or "i love humans" in query:
            speak("what you really like humans ewe thats was rubbish and you also")




        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak("alexis")

        elif "hey alexis" in query:
            speak("yes boss I,m here what you want to me and how can I help you")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "show the calendar" in query:
            d = calendar.calendar(2021)
            print(d)



        elif "show the month" in query:
            s = calendar.month(5)
            print(s)




        # elif 'play a song' in query:
        #     playsound("sounds.wav")



        elif "exit" in query:
            speak("Thanks for giving me your time")
            exit()



        elif "who made you" in query or "who created you" in query:
            speak("I have been created by dave sharma.")

        elif 'joke' in query:
            print(speak)
            speak(pyjokes.get_joke())
            # print
        elif "lets" in query:
            speak("gehd")
            main.main()

        elif 'search' in query:

            query = query.replace("search", "")
            # query = query.replace("play", "")
            webbrowser.open(query)
        # elif 'play' in query:
        #
        #     # query = query.replace("search", "")
        #     query = query.replace("play", "")
        #     pywhatkit.playonyt(query)


        elif "what is your name" in query:
            speak("mY name is alexis and i your pesonla assiasnt")

        elif "why you came to world" in query:
            speak("Thanks to Dave. further It's a secret")

        # elif 'power point presentation' in query:
        #     speak("opening Power Point presentation")
        #
        #     os.startfile(power)

        elif "study" in query:
            speak("yes,study is important so I let close the program")
            exit()

        elif "who are you" in query:
            speak("I am your virtual assistant created by dave sharma")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Gaurav ")

        elif 'open zoom' in query:
            appli = r"C:\Users\golug\AppData\Roaming\Zoom\bin\Zoom.exe"
            speak('opening zoom...')
            os.startfile(appli)

        elif 'open VS code' in query:
            appli = r"C:\Users\golug\Downloads"
            speak('opening zoom...')
            os.startfile(appli)

        elif "play" in query:
            we = query.replace("play","")
            speak("I have")
            speak("Wynk music")
            speak("youtube")
            speak("ganna")
            speak("spotify")

            speak("which one you want to use for songs")
            songs =  takeCommand().lower()
            if "wynk music" in songs:
                webbrowser.open("https://wynk.in/music/detailsearch/changes%20in%20songs?q=changes%20in%20songs" + we) and pyautogui.press("enter")
            elif "ganna" in songs:
                speak("please go on the search bar")
                time.sleep(4)
                pyautogui.write(we)
                webbrowser.open("https://www.ganna.com/")
            elif "youtube" in songs:
                speak("Ok your song is playing")
                pywhatkit.playonyt(we)
            # elif "spotify" in songs:
            #     spotify.Artist("arjit singh")









        elif 'what is the meaning of' in query:
            dictionary = PyDictionary()
            # print(dictionary.meaning(input("Enter which word you want to his meaning: ")))
            # query = query.replace("search", "")
            query = query.replace("what is the meaning of", "")
            print(dictionary.meaning(query))
            speak(dictionary.meaning(query))
        elif "what is the synonym of " in query:
            query = query.replace("what is the synonym of", "")
            print(dictionary.synonym(query))
            speak(dictionary.synonym(query))

        elif 'what is the antonym of' in query:
            dictionary = PyDictionary()
            query = query.replace("what is the antonym of","")
            print(dictionary.antonym(query))
            speak(dictionary.antonym(query))
        # elif "where is " in query:
        #     query = query.replace("where is", "")
        #     webbrowser.open_new("https://www.google.com/maps" + query)
        #     # webbrowser.open_new("https://www.google.com/maps")
        #     # query = query.replace("where is" "")
        #     # r = ("https://www.googlemap.com")
        #     # r.open(query)

        elif 'news' in query:
            speak("herea what I found on web")
            speak('latest news of NDTV news')
            # r = ("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
            # speak(r)
            webbrowser.open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
            speak('here are some top news from the times of india')
            print('''=============== TIMES OF INDIA ============''' + '\n')


        elif "coronavirus" in query or "covid 19" in query:
            speak("here what i found on web")
            speak("latest news about corona virus")
            corona = webbrowser.open("https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen")
            print(corona)
        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop alexis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps" + location + "")

        # elif "camera" in query or "take a photo" in query:
        #     ec.capture(0, "alexis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "I have to study" in query:
            speak("yes,study is important so I let close the program")
            exit()
        elif "shut up" in query:
            speak("I,m sorry I disturb you")
            exit()

        elif "switch window" in query:
            pygetwindow.getWindowsWithTitle(s)


        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")


        elif "sleep" in query:

            time.sleep()









        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('my diary.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = ctime()
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)



        elif "show note" in query:
            speak("Showing Notes")
            file = open("hola.txt", "r")
            print(file.read())
            speak(file.read(6))

        # elif "update assistant" in query:
        #     speak("After downloading file please replace this file with the downloaded one")
        #     url = '# url after uploading file'
        #     r = requests.get(url, stream=True)
        #
        #     with open("trace.py", "wb") as Pypdf:
        #
        #         total_length = int(r.headers.get('content-length'))
        #
        #         for ch in progress.bar(r.iter_content(chunk_size=2391975),
        #                                expected_size=(total_length / 1024) + 1):
        #             if ch:
        #                 Pypdf.write(ch)
        #
        # # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "comic" in query:
            webbrowser.open("https://xkcd.com/353/")

        elif "poem" in query:
            speak("Here is this")
            a = """
            Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
            print(a)
            ngine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            # rate = ngine.getProperty((rate))
            # ngine.setProperty(rate, 100)
            ngine.say(a)
            ngine.runAndWait()
        elif "alexis" in query:
            wishMe()
            speak("alexis 1 point o in your service Mister")
            # speak(assname)

        elif "weather" in query:
            speak("todays weather is")
            webbrowser.open(
                "https://weather.com/en-IN/weather/tenday/l/aff9460b9160c73ff01769fd83ae82cf37cb27fb7eb73c70b91257d413147b69")


        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")
        elif "open my Google chrome" in query:
            speak("opening google chrome")
            webbrowser.open("https://www.google.com")
        elif "where is" in query or "locate to" in query:
            query = query.replace("where is","")
            webbrowser.open_new("http://www.google.com/maps/place/" + query)
        elif "" in query:
            speak("Searching")
            print("Searching")
            query = query.replace("", "")
            results = wikipedia.summary(query, sentences=3)
            print(results)
            speak(results)




        elif "i love you" in query:
            speak("It's hard to understand")
        elif "what is your name" in query:
            speak("my name is alexis I,m you persoonal assistant")

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")
            # print("f": {query}\n")
            print("f","alexis:" + speak)
