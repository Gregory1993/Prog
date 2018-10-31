from tkinter import *
from tkinter.messagebox import showinfo
from marvelapicall import *
from tkinter.scrolledtext import ScrolledText

public_key = "e236fca8413247cbbd3b6eab5a278226"
private_key = "52fd65bb2019b663e26f555526b943dcfc1d5b2d"
counter = 0
timestamp = str(time.time())
hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
md5digest = str(hash.hexdigest())
url = "http://gateway.marvel.com:80/v1/public/characters"

dataOpvragen()
points = 25
heroDescrip = ''
heroName = ''
disguise = 'x'


global pointCount
global playerName

def kiesHero():
    global heroName, heroDescrip
    with open('Hero.json') as read:
        data = json.load(read)
        heroName = data['hero']['name']

    if '(' in heroName:
         heroName = (heroName[:heroName.find('(') -1])
    print(heroName)



def eersteHint():
    global heroDescrip
    with open('Hero.json') as read:
        data = json.load(read)
        heroDescrip = data['hero']['description']
        if '.' in heroDescrip:

            print(heroDescrip)

kiesHero()
eersteHint()

# def nieuweHint():


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
    global playerName
    playerName = loginfield.get()
    toonHoofdFrame()

def descripText(destroy = False):
    'Laat de puntentelling zien op het spelscherm'
    T.pack_forget()
    #global pointCount
    if destroy:
        pointCount.pack_forget()
    pointCount = ScrolledText(root, height=8, width=50, padx=170, pady=50)
    pointCount.pack()
    pointCount.insert(END, heroDescrip)
    pointCount.config(state=DISABLED)
    pointCount.tag_configure("center", justify='center')
    pointCount.tag_add("center", 1.0, "end")
    pointCount.place(relx=1, x=-2, y=2, anchor=NE)

def highscore():
    'Pop-up met de highscore'
    bericht = 'Highscore hier!'
    showinfo(title='popup', message=bericht)

def showpoints(destroy = False):
    'Laat de puntentelling zien op het spelscherm'
    T.pack_forget()
    global pointCount
    if destroy:
        pointCount.pack_forget()
    pointCount = Text(root, height=2, width=30)
    pointCount.pack()
    pointCount.insert(END, "Punten: {}".format(points))
    pointCount.config(state=DISABLED)
    pointCount.tag_configure("center", justify='center')
    pointCount.tag_add("center", 1.0, "end")


def puntenaftrek():
    global points
    if points >= 3:
        points -= 3
    elif points == 2:
        points -= 2
    elif points == 1:
        points -= 1

def checkpoints(points):
    if points <= 0:
        points = 0
        showpoints(True)
        bericht = 'Je bent af!\n{} is geëindigd met {} punten!'.format(playerName, points)
        showinfo(title='popup', message=bericht)
        root.destroy()


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

loginbutton = Button(master=loginframe, text='Start', command=lambda:[login(),textweg(),showpoints(), descripText()])
loginbutton.pack(side=LEFT, padx=20, pady=20)
loginbutton = Button(master=loginframe, text='View Highscore', command=highscore)
loginbutton.pack(side=RIGHT, padx=20, pady=20)

#Code voor het spelscherm
hoofdframe = Frame(master=root)
loginfield = Entry(master=hoofdframe, text='API call hier')
loginfield.pack(padx=320, pady=150)
loginfield1 = Entry(master=loginframe)
loginfield1.pack(padx=20, pady=20)
loginfield1.place(relx=1, x=-29, y=200, anchor=NE)
hoofdframe.pack(fill="both", expand=True)
hintbutton = Button(master=hoofdframe, text='Nieuwe hint (-3 punten!)', command=lambda:[puntenaftrek(),showpoints(True),checkpoints(points)])
hintbutton.pack(side=LEFT, padx=20, pady=20)



toonLoginFrame()
root.mainloop()
