import os
import speech_recognition as sr
import time
import webbrowser
import random
import pyttsx3
import socket
from requests import get
import wikipedia
os.system("figlet \"SIRI The hacker\"")
def speak(content):
    speak = pyttsx3.init()
    speak.setProperty("rate",150)
    speak.setProperty("voice","com.apple.speech.synthesis.voice.moira")
    speak.say(content)
    speak.runAndWait()
speak("SIRI ,the hacker")
def loctime():
    if time.localtime().tm_hour < 12:
        speak("good morning")
    elif time.localtime().tm_hour > 12 and time.localtime().tm_hour < 16:
        speak("good afternoon")
    elif time.localtime().tm_hour > 16:
        speak("good evening")
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 2500
        r.adjust_for_ambient_noise(source,duration=1)
        voice = r.listen(source)
        print("Listening..... ")
        try:
            listen_text = r.recognize_google_cloud(voice,language="en-in")
            print(listen_text)
        except sr.UnknownValueError:
            listen_text = listen()
        except sr.RequestError as e:
            content = "sorry,Request Error,Please connect to internet and try again"
            speak(content)
            exit()
        except ConnectionError:
            content = "sorry sir, no internet connection"
            speak(content)
    return listen_text
def startUp():
    loctime()
    speak("welcome,how can i help you")
def files_create(path, name):
    try:    
        txt = open(path + name, "x")
        speak("file created..")
        txt.close()
    except FileExistsError:
        speak("file already exist")
def file_read(path, name):
    txt = open(path + name, "r")
    content = txt.read()
    speak(content)
    txt.close()
def file_write(path, name):
    txt = open(path + name, "w+")
    speak("aye sir,preparing to write")
    os.system("open -t " + path + name)
    txt.close()
def file_rename(path, name, new_name):
    os.rename(path + "/" + name, path + "/" + new_name)
def list_files():
    content = os.listdir()
    list_dir = ",".join(content)
    speak(list_dir)
def localAddress():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = "google.com"
    port = 80
    s.connect((host,port))
    speak(s.getsockname()[0])
def PublicAddress():
    ip = get("https://ipify.org").text
    speak(ip)
def NetworkScan():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect_ex(("google.com",80))
    ip = s.getsockname()[0]
    b = str(ip)
    a = b.split(".")
    dot = "."
    addr = a[0]+dot+a[1]+dot+a[2]+dot+"1/24"
    os.system("nmap -oG -"+" "+addr+" "+"| grep Up | awk \'{print $2}\' > ip.txt")
    v = open("ip.txt","r")
    c = v.read()
    print(c)
    v.close()
    speak("scan completed,you can see the devices in your console")
    os.remove("ip.txt")
def about(query):
    try:
        speak(wikipedia.summary(query,sentences=2))
    except Exception:
        speak("sorry,i can't find ")
def exploit():
    speak("aye sir,exploit mode activated")
    speak("starting exploit database")
    speak("checking......done!")
    while 1:
        listen_text = listen()
        if "exit" in listen_text:
            speak("aye sir....exiting")
        else:
            speak("getting all the exploits for"+" "+listen_text)
            os.system("searchsploit"+" "+listen_text)
            speak("all exploits are printed in the console please check......!")
def sys_cmd():
    speak("System Command Mode activated")
    while 1:
        listen_text = listen()
        if "create"  and "file" in listen_text:
            speak("aye sir,preparing to create a file")
            speak("please enter the path where you want to create a file")
            path = input()
            speak("please enter the name of the file with extension")
            name = input()
            files_create(path, name)
            listen_text = listen()
            if "open " in listen_text:
                file_write(path, name)
            if "read" in listen_text:
                file_read(path, name)
        if "open " and "file" in listen_text:
            speak("aye, preparing system to open  a file")
            speak("please enter the path")
            path = input()
            speak("please enter the name os the file to open")
            name = input()
            file_write(path, name)
        if "read" and "file" in listen_text:
            speak("aye sir,preparing to read a file")
            speak("please enter the path")
            path = input()
            speak("please enter the name")
            name = input()
            file_read(path, name)
        if "rename" and "file" in listen_text:
            speak("aye sir,preparing to change ")
            speak("please enter the path to a file")
            path = input()
            speak("please enter the name of the file")
            name = input()
            speak("please enter the new name u want to change")
            new_name = input()
            file_rename(path, name, new_name)
        if "directory" and "current" in listen_text:
            temp = os.getcwd()
            content = temp.split("/")
            path = ",".join(content)
            speak("sir your current working directory is" + path)
        if "directory" and "change" in listen_text:
            speak("aye sir")
            speak("enter the new directory")
            path = input()
            os.chdir(path)
            speak("done")
        if (("show" and "file") or "directories") in listen_text:
            speak("aye sir")
            list_files()
        if "delete" and "file" in listen_text:
            speak("sir,please enter the name of the file")
            file = input()
            os.remove(file)
        if "site" and "report" in listen_text:
            speak("aye sir,please enter the url")
            url = input()
            webbrowser.open("https://sitereport.netcraft.com/?url=" + url)
        if ("reverse dns" or ("websites" and "web server")) in listen_text:
            speak("aye sir,opening")
            webbrowser.open("https://www.yougetsignal.com/tools/web-sites-on-web-server/")
        if "local" and "address" in listen_text:
            speak("aye sir ,getting your IP")
            localAddress()
        if "public" and "address" in listen_text:
            speak("aye sir,getting your public IP")
            PublicAddress()
        if "network" and "scan" in listen_text:
            speak("aye sir,performing a network scan")
            speak("please wait while scaning your network")
            NetworkScan()
        if ("archive" or "wayback" or "server activity") in listen_text:
            speak("aye sir,please enter the website address")
            url = input()
            webbrowser.open("https://web.archive.org/web/*/" + url)
        if "open" in listen_text:
            list = listen_text.split()
            list.remove("open")
            url = "".join(list)
            webbrowser.open("https://"+url+".com")
        if "exploit" or "query" in listen_text:
            speak("aye,getting ready")
            exploit()
        if "exit" in listen_text:
            speak("aye sir,switching into normal mode")
            break
def hacker(listen_text):
    if "hacker" in listen_text:
        respond =["at your service sir","aye sir","i'm ready sir"]
        speak(random.choice(respond))
    if "how are you" in listen_text:
        concern = ["i'm fine,Thank You", "i'm good,what about you?", "i'm Excellent", "i'm fine,How r u?"]
        subject = random.choice(concern)
        speak(subject)
        if subject == concern[1] or subject == concern[3]:
            listen_text = listen()
            if listen_text in ["i am good ", "i am fine", "i am excellent", "i am alright", "good", "fine", "alright"]:
                speak("i'm glad to hear that")
            elif listen_text in ["i am bored", "bored", "i am not good", "i am not fine", "not well", "not good",
                                 "not fine"]:
                speak("may be i can make you happy..")
            elif listen_text in ["i am alone", "alone", "i am lonely", "feeling lonely", "lonely feeling",
                                 "feels alone",
                                 "single", "i am single"]:
                speak("Don't worry,i'm with you")
    if "your name" in listen_text:
        speak("siri,The hacker")
    if "call you " in listen_text:
        speak("u can call me Hacker")
    if "who are you" in listen_text:
        self = ["i'm a hacker", "i'm a memory", "i'm your digital assistant"]
        speak(random.choice(self))
    if "what can you do" in listen_text:
        speak("In normal mode,i can perform all the tasks like google and siri,In system Command mode i can perform terminal based operations,In hacker mode,i can perform a small attacks like wifi hacking,network scanning,port forwarding..etc...")
    if listen_text in ["who made you", "who is your creator", "who designed you", "creator of you", "who created you"]:
        speak("Sampath Pendurthi is my creator")
    if "i love you" in listen_text:
        txt = ["i love you too","thank you","yes i love myself"]
        speak(random.choice(txt))
    if "what is my name" in listen_text:
        speak("sampath pendurthi")
    if "do you love me" in listen_text:
        txt = ["yes,i love you","no i love myself","no,i'm not interested"]
        speak(random.choice(txt))
    if "fuck" in listen_text:
        txt = ["asshole","fuck you","bitch","go and fuck yourself"]
        speak(random.choice(txt))
    if "will you marry me" in listen_text:
        speak("yes,but only when you promise me that you'll not make babies with me..hahahahahaha")
    if listen_text in ["shutdown", "exit", "sleep", "poweroff"]:
        speak("aye sir,shuttingdown")
        exit()
    if "time " in listen_text:
        text_time = "sir it's" + str(time.localtime().tm_hour) + "hours" + str(time.localtime().tm_min) + "minutes" + str(time.localtime().tm_sec) + "seconds"
        speak(text_time)
    if "youtube" in listen_text:
        webbrowser.open(url="https://youtube.com")
    if "facebook" in listen_text:
        webbrowser.open(url="https://facebook.com")
    if "twitter" in listen_text:
        webbrowser.open(url="https://twitter.com")
    if "mail" in listen_text:
        webbrowser.open(url="https://gmail.com")
    if "Browser" in listen_text:
        speak("aye sir,opening web browser")
        webbrowser.open(url="https://google.com")
    if "search" in listen_text:
        new_text = listen_text.replace("search","")
        webbrowser.open("https://duckduckgo.com/?q=" + new_text + "&ia=web")
    if "who is " in listen_text or "tell me about " in listen_text or "what is" in listen_text:
        new_text= ''
        if "who is" in listen_text:
            new_text = listen_text.replace("who is","")
        elif "tell me about" in listen_text:
            new_text = listen_text.replace("tell me about","")
        elif "what is " in listen_text:
            new_text = listen_text.replace("what is ","")
        about(new_text)
        listen_text = listen()
        if "open"  or "show" in listen_text:
            page = wikipedia.page(new_text).url
            speak("aye,Opening wikipedia page....")
            webbrowser.open(page)
startUp()
while 1:
   try:
       listen_text = listen().lower()
       if "system command mode" in listen_text:
           speak("aye sir,switching into system command mode")
           sys_cmd()
       else:
           hacker(listen_text)
   except KeyboardInterrupt:
       speak("GoodBye")