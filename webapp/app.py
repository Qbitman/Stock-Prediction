
from platform import python_branch
from flask import Flask, render_template, request, jsonify
import subprocess
import os
import spacy
import pyttsx3
import speech_recognition as sr
import webbrowser


english = spacy.load("en_core_web_sm")

app = Flask(__name__)


def lastWord(string):
    idx = string.find("search")
    print(idx)
    temp = (string[idx+7:])
    print(temp)
    x = temp.replace(" ", "+")
    return x


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/voice", methods=['GET'])
def voice():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("say something...")
            audio = r.listen(source)
        ch = r.recognize_google(audio)
        ch = ch.lower()
        print(ch)

        # wake word: hey Jarvis
        wake = ch.split()[0:2]

        try:
            if (wake[0] == "jarvis"):
                if ("date" in ch and "show" in ch):
                    output = subprocess.getoutput("date /t")
                    return output
                elif ("you" in ch and ("up" in ch or "there" in ch)):
                    pyttsx3.speak("Always there for you sir!")
                    return "Always there for you sir!"
                elif ("notepad" in ch and "open" in ch):
                    pyttsx3.speak("opening notepad... just a second")
                    subprocess.getoutput("notepad")
                    return "Success!"
                elif ("youtube" in ch and "open" in ch and "search" in ch):
                    last = lastWord(ch)
                    subprocess.getoutput(
                        "start chrome www.youtube.com/results?search_query=" + last)
                    return "Success!"
                elif(("stock" in ch or "price" in ch) and ("predict" in ch or "prediction" in ch)):
                    webbrowser.open("http://localhost:8501/")
                    return "success"
                else:
                    return "I didn't get it! can u please repeat"
            elif(wake[0] == "hello" and wake[1] == "jarvis"):
                pyttsx3.speak("what can I do for you sir?")
                return " "
            else:
                return "didn't find wake word"
        except:
            return "unknown error! let's solve it together :)"
    except TypeError:
        return "I didn't get it! can u please repeat"
    except:
        return "I didn't get it! can u please repeat"


@app.route("/launch", methods=['GET'])
def launch():
    myaction = ""
    req = request.args.get("req")
    doc1 = english(req)
    req = req.lower()
    for i in doc1:
        if i.pos_ == "VERB":
            # print(i.text, i.lemma_)
            myaction = i.lemma_
    print(myaction)
    if ("date" in req and "show" in myaction):
        output = subprocess.getoutput("date /t")
        return output
    elif ("notepad" in req and ("open" in req or "start" in req or "run" in req)):
        subprocess.getoutput("notepad")
        return "Success!"
    elif ("chrome" in req and ("open" in req or "start" in req or "run" in req)):
        subprocess.getoutput("start chrome")
        return "Success!"
    elif ("youtube" in req and ("open" in req or "start" in req or "run" in req) and ("search" in req)):
        last = lastWord(req)
        subprocess.getoutput(
            "start chrome www.youtube.com/results?search_query=" + last)
        return "Success!"
    elif ("youtube" in req and ("open" in req or "start" in req or "run" in req)):
        subprocess.getoutput("start chrome www.youtube.com")
        return "Success!"
    elif ("facebook" in req and ("open" in req or "start" in req or "run" in req)):
        subprocess.getoutput("start chrome www.facebook.com")
        return "Success!"
    elif(("stock" in req or "price" in req) and ("predict" in req or "prediction" in req)):
        webbrowser.open("http://localhost:8501/")
        return "success"

    return "hii"


if __name__ == '__main__':
    app.run(debug=True)
