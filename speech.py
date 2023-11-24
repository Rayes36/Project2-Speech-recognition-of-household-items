from __future__ import print_function
import speech_recognition as sr
import os
import datetime
import warnings
import calendar
import pyttsx3
import random
import os.path
import webbrowser

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def listen_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting and Listening")
        audio = recognizer.listen(source)

        data = ""

        try:
            data = recognizer.recognize_google(audio)
            print("You said:", data)

        except sr.UnknownValueError:
            print("Error: Unable to understand the audio")

        except sr.RequestError as e:
            print("Error: Request to Google Speech Recognition failed:", e)

        return data


def is_wake_word(text):
    wake_word = "ok"
    text = text.lower()
    if wake_word in text:
        return True
    return False


def get_current_date():
    now = datetime.datetime.now()
    date_today = datetime.datetime.today()
    weekday_today = calendar.day_name[date_today.weekday()]
    month_today = now.month
    day_today = now.day
    months = [
        "January", "February", "March", "April", "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    ordinals = [
        "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th",
        "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th",
        "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th",
        "29th", "30th", "31st"
    ]
    return "Today is " + weekday_today + ", " + months[month_today - 1] + " the " + ordinals[day_today - 1] + "."


def get_greeting(text):
    greetings = ["hi", "hey", "hello", "greetings", "wassup", "hola"]
    responses = ["what's good", "hello", "hey there","hello hello"]

    for word in text.split():
        if word.lower() in greetings:
            return random.choice(responses) + "."

    return ""


while True:
    try:
        text = listen_audio()
        response = ""

        if is_wake_word(text):
            response += get_greeting(text)

            if "date" in text or "day" in text or "month" in text:
                current_date = get_current_date()
                response += " " + current_date

            elif "lights" in text:
                if "on" in text:
                    response = "Lights on"
                elif "off" in text:
                    response = "Lights off"

            elif "time" in text:
                now = datetime.datetime.now()
                regiontime= ""
                if now.hour >= 12:
                    regiontime = "p.m."
                    hour = now.hour - 12
                else:
                    regiontime = "a.m."
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                response += "The time is  " + str(hour) + ":" + minute + " " + regiontime + "."

            elif "how are you" in text:
                response += "I am awesome! Thank you. How are you?"

            elif "fine" in text or "good" in text:
                response += "I am glad to know that you're fine."

            elif "open" in text.lower():
                if "opera" in text.lower():
                    response += "Opening Opera GX"
                    os.startfile(r"C:\Users\ASUS\AppData\Local\Programs\Opera GX\launcher.exe")

                elif "word" in text.lower():
                    response += "Opening Microsoft Word"
                    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")

                elif "excel" in text.lower():
                    response += "Opening Microsoft Excel"
                    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")

                elif "youtube" in text.lower():
                    response += "Opening YouTube"
                    webbrowser.open("https://youtube.com/")

                elif "google" in text.lower():
                    response += "Opening Google"
                    webbrowser.open("https://google.com/")

                elif "stackoverflow" in text.lower():
                    response += "Opening Stack Overflow"
                    webbrowser.open("https://stackoverflow.com/")

                elif "binus" in text.lower():
                    response += "Opening BINUS website"
                    webbrowser.open("https://binus.ac.id")

                else:
                    response += "Error : App not found"

            elif "search" in text.lower():
                index = text.lower().split().index("search")
                search_query = text.split()[index + 1:]
                webbrowser.open("https://www.google.com/search?q=" + "+".join(search_query))
                response += "Searching " + str(search_query) + " on Google"

            elif "youtube" in text.lower():
                index = text.lower().split().index("youtube")
                search_query = text.split()[index + 1:]
                webbrowser.open("http://www.youtube.com/results?search_query=" + "+".join(search_query))
                response += "Opening " + str(search_query) + " on YouTube"

            elif "stop" in text or "exit" in text or "quit" in text:
                print("Goodbye!Thank You.")
                talk("Goodbye! Thank you.")
                break

            print(response)
            talk(response)

    except:
        talk("Sorry, I'm not sure about that.")
