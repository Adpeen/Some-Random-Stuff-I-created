from tkinter import *
import random

joke = ""

def Joke():
    global joke
    jokes = list(my_jokes.keys())
    joke = random.choice(jokes)
    entry.delete(0.0, END)
    output.delete(0.0, END)
    entry.insert(END, joke)

def Answer():
    output.delete(0.0, END)
    try:
        answer = my_jokes[joke]
    except:
        answer = "There is no entry for this question."
    output.insert(END, answer)

window = Tk()
window.title("Hello World!")

Button(window, text="Get Joke", width=15, command=Joke).grid(row=3, column=0, sticky=W)

Button(window, text="Get Answer", width=15, command=Joke).grid(row=3, column=0, sticky=E)

entry = Text(window, width=50, height=2, wrap=WORD, background="green")
entry.grid(row=1, column=0, sticky=W)

output = Text(width=50, height=6, wrap=WORD, background="green")
output.grid(row=1, column=0, columnspan=2, sticky=W)

my_jokes = {
    "I told my wife she was drawing her eyebrows too high." : "She looked surprised.",
    "I tried to catch fog yesterday." : "Mist.",
    "And the Lord said unto John: ‘Come forth and you will receive eternal life’." : "But John came fifth, and won a toaster.",
    "I went to a really emotional wedding the other day." : "Even the cake was in tiers.",
    "Someone stole my mood ring." : "I don’t know how I feel about that."
    }

window.mainloop()
