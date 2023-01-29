import pyttsx3
import tkinter as tk

app = tk.Tk()
app.title("Text to Speech")
app.geometry("500x500")
app.resizable(0, 0)

def speak():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text.get())
    engine.runAndWait()

text = tk.StringVar()
text.set("Enter your text here")

tk.Label(app, text="Text to Speech", font=("Arial", 20)).pack(pady=20)
tk.Entry(app, textvariable=text, font=("Arial", 15)).pack(pady=20, ipadx=100,ipady=50)
tk.Button(app, text="Speak", font=("Arial", 15), command=speak).pack(pady=20)

app.mainloop()