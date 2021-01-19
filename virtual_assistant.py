import wolframalpha
import webbrowser
import pyttsx3
import speech_recognition as sr
import subprocess
import selenium
from selenium import webdriver
import screen_brightness_control as sbc
engine = pyttsx3.init()
client = wolframalpha.Client("UQWGUR-WHP3TKXQQJ")
engine.setProperty('rate', 150)


while True:
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        try:
            print("Ask me anything !")
            audio = rObject.listen(source, phrase_time_limit=4)
            print("Render")  # limit 5 secs
            text = rObject.recognize_google(audio, language='en-US')
            print("You : ", text)
        except sr.UnknownValueError:
            print("Ask me anything !")
            audio = rObject.listen(source, phrase_time_limit=4)
            print("Render")  # limit 5 secs
            text = rObject.recognize_google(audio, language='en-US')
            print("You : ", text)

    if text == ("hello"):
        name = "Hello, Human ; How can I Help You"
        engine = pyttsx3.init()
        engine.say(name)
        engine.runAndWait()
    elif text == ("who are you"):
        name = "My Name is Rookie, I am a virtual assistant developed by Eshwar"
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
        engine.say(name)
        engine.runAndWait()
    elif text == ("wake up"):
        name = "yeah tell me"
        engine = pyttsx3.init()
        engine.say(name)
        engine.runAndWait()
    elif text == ("what is your name"):
        developer = "My name is Rookie"
        engine = pyttsx3.init()
        engine.say(developer)
        engine.runAndWait()
    elif text == ("open Chrome"):
        say = ("Opening Chrome")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        subprocess.call('google-chrome')
    elif text == ("open code blocks"):
        say = ("Opening Codeblocks")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        subprocess.call('codeblocks')
    elif text == ("open discord"):
        say = ("Opening Discord")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        subprocess.call('discord')
    elif text == ("open vs code"):
        say = ("Opening vs code")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        subprocess.call('code')
    elif text == ("play games"):
        say = ("Select Games Blocks Pacman Snake TicTacTae")
        print('blocks \npacman \nsnake \ntictactoe')
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
    elif text == ("pacman"):
        say = ("opening pacman")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        subprocess.call('pacman4console')
    elif text == ("cheese"):
        say = ("opening camera")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        subprocess.call('cheese')
    elif text == ("blocks"):
        say = ("opening blocks")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        subprocess.call('bastet')
    elif text == ("snake"):
        say = ("opening snake")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        subprocess.call('nsnake')
    elif text == ("maths class"):
        say = ("opening maths class")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        driver = webdriver.Chrome("google-chrome")
        url = "https: // meet.google.com / fzz - ymvv - hjf?pli = 1 & authuser = 2"
        driver.get(url)
        webdriver.chrome.find_element_by_xpath(
            "/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span/span/div/div[1]/div/svg")
        webdriver.chrome.find_element_by_xpath(
            "/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span/span/div/div/svg")
        webdriver.chrome.find_element_by_xpath(
            "/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span")
    elif text == ("Google search"):
        say = ("tell me what i need to search")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        rObject = sr.Recognizer()
        audio = ''

        with sr.Microphone() as source:
            print("Ask me anything !")
            audio = rObject.listen(source, phrase_time_limit=5)
            print("Render")  # limit 5 secs
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        query = text
        results = ("Showing google results for " + query)
        engine = pyttsx3.init()
        engine.say(results)
        engine.runAndWait()
        webbrowser.open("https://www.google.com/search?q=" + query)
    elif text == ("increase brightness"):
        say = ("how much should i increase")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        rObject = sr.Recognizer()
        audio = ''

        with sr.Microphone() as source:
            print("Ask me anything !")
            audio = rObject.listen(source, phrase_time_limit=2)
            print("Render")  # limit 5 secs
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        query = text
        results = ("increasing screen brightness to " + text)
        engine = pyttsx3.init()
        engine.say(results)
        engine.runAndWait()
        sbc.set_brightness(text)
    elif text == ("decrease brightness"):
        say = ("how much should i decrease")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        rObject = sr.Recognizer()
        audio = ''

        with sr.Microphone() as source:
            print("Ask me anything !")
            audio = rObject.listen(source, phrase_time_limit=2)
            print("Render")  # limit 5 secs
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        query = text
        results = ("decreasing screen brightness to " + text)
        engine = pyttsx3.init()
        engine.say(results)
        engine.runAndWait()
        sbc.fade_brightness(text)
    elif text == ("Wiki search"):
        say = ("tell me what i need to search")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        rObject = sr.Recognizer()
        audio = ''

        with sr.Microphone() as source:
            print("Ask me anything !")
            audio = rObject.listen(source, phrase_time_limit=2)
            print("Render")  # limit 5 secs
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        query = text
        results = ("Showing Wiki results for " + query)
        engine = pyttsx3.init()
        engine.say(results)
        engine.runAndWait()
        webbrowser.open("https://en.wikipedia.org/wiki/" + query)
    elif text == ("YouTube search"):
        say = ("tell me what i need to search")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        rObject = sr.Recognizer()
        audio = ''

        with sr.Microphone() as source:
            print("Ask me anything !")
            audio = rObject.listen(source, phrase_time_limit=2)
            print("Render")  # limit 5 secs
        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        query = text
        results = ("Showing youtube results for " + query)
        engine = pyttsx3.init()
        engine.say(results)
        engine.runAndWait()
        webbrowser.open("http://www.youtube.com/results?search_query=" + query)
    elif text == ("tictactoe"):
        say = ("opening tictactoe")
        engine = pyttsx3.init()
        engine.say(say)
        engine.runAndWait()
        from tkinter import *
        from tkinter import messagebox
        import random as r


        def button(frame):  # Function to define a button
            b = Button(frame, padx=1, bg="papaya whip", width=3, text="   ", font=('arial', 60, 'bold'),
                       relief="sunken", bd=10)
            return b


        def change_a():  # Function to change the operand for the next player
            global a
            for i in ['O', 'X']:
                if not (i == a):
                    a = i
                    break


        def reset():  # Resets the game
            global a
            for i in range(3):
                for j in range(3):
                    b[i][j]["text"] = " "
                    b[i][j]["state"] = NORMAL
            a = r.choice(['O', 'X'])


        def check():  # Checks for victory or Draw
            for i in range(3):
                if (b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == a or b[0][i]["text"] == b[1][i]["text"] ==
                        b[2][i]["text"] == a):
                    messagebox.showinfo("Congrats!!", "'" + a + "' has won")
                    reset()
            if (b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == a or b[0][2]["text"] == b[1][1]["text"] ==
                    b[2][0]["text"] == a):
                messagebox.showinfo("Congrats!!", "'" + a + "' has won")
                reset()
            elif (b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] == b[1][0]["state"] == b[1][1]["state"] ==
                  b[1][2]["state"] == b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"] == DISABLED):
                messagebox.showinfo("Tied!!", "The match ended in a draw")
                reset()


        def click(row, col):
            b[row][col].config(text=a, state=DISABLED, disabledforeground=colour[a])
            check()
            change_a()
            label.config(text=a + "'s Chance")


        ###############   Main Program #################
        root = Tk()  # Window defined
        root.title("Tic-Tac-Toe")  # Title given
        a = r.choice(['O', 'X'])  # Two operators defined
        colour = {'O': "deep sky blue", 'X': "lawn green"}
        b = [[], [], []]
        for i in range(3):
            for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command=lambda row=i, col=j: click(row, col))
                b[i][j].grid(row=i, column=j)
        label = Label(text=a + "'s Chance", font=('arial', 20, 'bold'))
        label.grid(row=3, column=0, columnspan=3)
        root.mainloop();
        from tkinter import *
        from tkinter import messagebox
        import random as r


        def button(frame):  # Function to define a button
            b = Button(frame, padx=1, bg="papaya whip", width=3, text="   ", font=('arial', 60, 'bold'),
                       relief="sunken", bd=10)
            return b


        def change_a():  # Function to change the operand for the next player
            global a
            for i in ['O', 'X']:
                if not (i == a):
                    a = i
                    break


        def reset():  # Resets the game
            global a
            for i in range(3):
                for j in range(3):
                    b[i][j]["text"] = " "
                    b[i][j]["state"] = NORMAL
            a = r.choice(['O', 'X'])


        def check():  # Checks for victory or Draw
            for i in range(3):
                if (b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == a or b[0][i]["text"] == b[1][i]["text"] ==
                        b[2][i]["text"] == a):
                    messagebox.showinfo("Congrats!!", "'" + a + "' has won")
                    reset()
            if (b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == a or b[0][2]["text"] == b[1][1]["text"] ==
                    b[2][0]["text"] == a):
                messagebox.showinfo("Congrats!!", "'" + a + "' has won")
                reset()
            elif (b[0][0]["state"] == b[0][1]["state"] == b[0][2]["state"] == b[1][0]["state"] == b[1][1]["state"] ==
                  b[1][2]["state"] == b[2][0]["state"] == b[2][1]["state"] == b[2][2]["state"] == DISABLED):
                messagebox.showinfo("Tied!!", "The match ended in a draw")
                reset()


        def click(row, col):
            b[row][col].config(text=a, state=DISABLED, disabledforeground=colour[a])
            check()
            change_a()
            label.config(text=a + "'s Chance")


        ###############   Main Program #################
        root = Tk()  # Window defined
        root.title("Tic-Tac-Toe")  # Title given
        a = r.choice(['O', 'X'])  # Two operators defined
        colour = {'O': "deep sky blue", 'X': "lawn green"}
        b = [[], [], []]
        for i in range(3):
            for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command=lambda row=i, col=j: click(row, col))
                b[i][j].grid(row=i, column=j)
        label = Label(text=a + "'s Chance", font=('arial', 20, 'bold'))
        label.grid(row=3, column=0, columnspan=3)
        root.mainloop()
    else:
        res = client.query(text)
        wolfram_res = next(res.results).text
        engine = pyttsx3.init()
        engine.setProperty('rate', 125)
        engine.say(wolfram_res)
        engine.runAndWait()



















