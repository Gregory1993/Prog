from tkinter import *
from tkinter.messagebox import showinfo

points = 25

def toonLoginFrame():
    'Dit is het beginscherm'
    hoofdframe.pack_forget()
    loginframe.pack()

def toonHoofdFrame():
    'Dit is het spelscherm'
    loginframe.pack_forget()
    hoofdframe.pack()

def login():
    'Vraagt om de spelernaam'
    playerName = loginfield.get()
    toonHoofdFrame()

def highscore():
    'Pop-up met de highscore'
    bericht = 'Highscore hier!'
    showinfo(title='popup', message=bericht)


def showpoints():
    'Laat de puntentelling zien op het spelscherm'
    T.pack_forget()
    pointCount = Text(root, height=2, width=30)
    pointCount.pack()
    pointCount.insert(END, "Punten: {}".format(points))
    pointCount.config(state=DISABLED)
    pointCount.tag_configure("center", justify='center')
    pointCount.tag_add("center", 1.0, "end")

def puntenaftrek():
     global points
     points -= 3

def textweg():
    'Haalt de introtekst weg wanneer je naar het spelscherm gaat'
    T.pack_forget()

root = Tk()

T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "Vul je naam in")
T.config(state=DISABLED)
T.tag_configure("center", justify='center')
T.tag_add("center", 1.0, "end")

#Code voor het beginscherm
loginframe = Frame(master=root)
loginframe.pack(fill="both", expand=True)
loginfield = Entry(master=loginframe)
loginfield.pack(padx=20, pady=20)
loginbutton = Button(master=loginframe, text='Start', command=lambda:[login(),textweg(),showpoints()])
loginbutton.pack(side=LEFT, padx=20, pady=20)
loginbutton = Button(master=loginframe, text='View Highscore', command=highscore)
loginbutton.pack(side=RIGHT, padx=20, pady=20)

#Code voor het spelscherm
hoofdframe = Frame(master=root)
hoofdframe.pack(fill="both", expand=True)
hintbutton = Button(master=hoofdframe, text='Nieuwe hint (-3 punten!)', command=lambda:[puntenaftrek(),showpoints()])
hintbutton.pack(side=LEFT, padx=20, pady=20)



toonLoginFrame()
root.mainloop()
