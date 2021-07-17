# jarvis

import pyttsx3

import datetime

import speech_recognition as sr

import wikipedia

import webbrowser

from pywikihow import search_wikihow

import pywhatkit as kit

import pyjokes
import sys

from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtCore import QTimer, QTime, QDate, Qt

from PyQt5.QtGui import QMovie

from PyQt5.QtCore import *

from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.uic import loadUiType

from jui import Ui_Jarvi10 




engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

#print(voices[0].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):

    engine.say(audio)

    engine.runAndWait()


def wishme():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:

        speak("Good Morning")


    elif hour>=12 and hour<18:

        speak("Good afternoon")


    else:

        speak("Good evening")


    speak("I am Jarvis, how can I help you Bosss?")


class MainThread(QThread):


    def __init__(self):

        super(MainThread,self).__init__()


    def run(self):

        self.TaskExecution()


    def takecommand(self):
        """


        :rtype: object
        """

        r = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening........")

            sr.pause_threshold = 1

            audio = r.listen(source)


        try:

            print("Recognizing...")

            query = r.recognize_google(audio, language='en-in')

            print("User said: ", query)


        except Exception as e :

            print("Say that again please...")

            return "None"

        return query








    def TaskExecution(self):

        wishme()

        while True:

            self.query = self.takecommand().lower()
            


            if 'wikipedia' in self.query:

                speak('searching wikipedia')

                self.query = self.query.replace("wikipedia", "")

                results = wikipedia.summary(self.query, sentences=4)

                speak("According to Wikipedia")

                speak(results)

                """print statement daalna hai"""


            elif 'open youtube' in self.query:

                webbrowser.open("youtube.com")


            elif 'open google' in self.query:

                webbrowser.open("google.com")


            elif "search in google" in self.query:

                speak("what would u like to search in google")

                cm =takecommand().lower()

                webbrowser.open(f"{cm}")

            

            elif 'stack overflow' in self.query:

                webbrowser.open("stackoverflow.com")


            elif "spotify" in self.query:

                webbrowser.open("spotify.com")

            

            elif ' open Hacker rank' in self.query:

                webbrowser.open("hackerrank.com")


            elif 'the time' in self.query:

                strTime = datetime.datetime.now().strftime("%H:%M:%S")

                speak(f"Boss, the time is {strTime}")
            
            

            elif "how to" in self.query:

                speak("Getting Data From the Internet!")

                op = self.query.replace("Jarvis","")

                max_result = 1

                how_to_func = search_wikihow(op, max_result)

                assert len(how_to_func) == 1

                how_to_func[0].print()

                speak(how_to_func[0].summary)


            elif 'send message' in self.query:

                kit.sendwhatmsg('+919403034727', 'pywhatkit_dbs.txt', 10, 3)


            elif "play song" in self.query:

                kit.playonyt("Best of Hollywood songs")


            elif "tell me a joke" in self.query:

                jokee = pyjokes.get_joke()

                speak(jokee)
          
                



            elif "terminate" in self.query:
                speak("thanks for using me,have a good day")
                sys.exit()


                


    



startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Jarvi10()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)


    def startTask(self):
        self.ui.movie = QtGui.QMovie((".ASSETS/MImN.gif"))
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie((".ASSETS/QjoV.gif"))
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
        


    def showTime(self):
        current_time = QTime.currentTime()
        current_date  = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)




app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())

        

        
        
        
        


            
        




        
        
        








