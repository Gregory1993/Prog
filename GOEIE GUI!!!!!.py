from tkinter import *
from tkinter.messagebox import showinfo
from marvelapicall import *
from tkinter.scrolledtext import ScrolledText
import random
import datetime
import csv

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
gebruikteHints = []
hint = ''

global pointCount
global playerName

def kiesHero():
    global heroName, hint
    with open('Hero.json') as read:
        data = json.load(read)
        heroName = data['hero']['name']

    if '(' in heroName:
         heroName = (heroName[:heroName.find('(') -1])
    print(heroName)



def eersteHint():
    global hint
    with open('Hero.json') as read:
        data = json.load(read)
        hint = data['hero']['description']
        if '.' in hint:

            print(hint)



def nieuweHint():
    global gebruikteHints, hint
    with open('Hero.json') as read:
        data = json.load(read)
        while True:
            randomGetal = random.randrange(0,3)
            randomStorieComicSerie = ['comics', 'series', 'stories']
            lst = randomStorieComicSerie[randomGetal]
            if int(data['hero'][lst]['appearances']) >= 20:
                randomIndex = random.randrange(0, 19)
            else:
                randomIndex = random.randrange(0, int(data['hero'][lst]['appearances'])-1)
            hint = 'Deze superheld komt voor in: (' + lst + ')\n' + data['hero'][lst]['items'][randomIndex]['name']
            if hint in gebruikteHints:
                continue
            else:
                gebruikteHints.append(hint)
                print('De hero komt voor in de ' + lst + ' :')
                print(hint)
                break

#kiesHero()
#eersteHint()
#nieuweHint()

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
    global hint, root, destxt
    destxt = ScrolledText(root, height=8, width=50, padx=170, pady=50)
    destxt.pack()
    destxt.insert(END, hint)
    destxt.config(state=DISABLED)
    destxt.tag_configure("center", justify='center')
    destxt.tag_add("center", 1.0, "end")
    destxt.place(relx=1, x=-2, y=2, anchor=NE)

def highscore():
    'Pop-up met de highscore'
    bericht = 'Highscore hier!'
    showinfo(title='popup', message=bericht)

def checkAnswer():
    global points
    answerUser = answerField.get()
    print(answerUser)
    print(heroName)
    if answerUser == heroName:
        bericht = 'JE WINT!\n{} is geëindigd met {} punten!'.format(playerName, points)
        showinfo(title='popup', message=bericht)
        root.destroy()
    else:
        points -= 1

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
        bericht = 'Je bent af!\n{} is geëindigd met {} punten!\n Het goede antwoord was {}'.format(playerName, points, heroName)
        showinfo(title='Loser', message=bericht)
        root.destroy()


def textweg():
    'Haalt de introtekst weg wanneer je naar het spelscherm gaat'
    T.pack_forget()

import json as serializer
from tkinter import *

def situatie(naam1, naam2, highscore):
    """
    Openen van het puntentotnutoe csv bestand en kijken tijdens welke situaties we de score opslaan.
    """
    with open('puntentotnutoe.csv', 'r+') as file:
        reader = csv.reader(file)
        for row in reader:
            naam2.append(row[0])
            if naam1 in naam2:
                if int(highscore) >= int(row[1]):
                    return 'situatie_2'
                else:
                    return 'situatie_3'
        return 'situatie_1'

def nieuwe_highscore(naam1, highscore):
    """
    In situatie 1 sla je de score op in het puntentotnutoe csv bestand. Hier sla je de datum waarop deze score behaald is ook bij op.
    """
    datum = datetime.datetime.now()
    datum2 = datum.strftime('%d %b %Y')
    naam2 = []
    inp = situatie(naam1,naam2, highscore)
    if inp == 'situatie_1':
        with open('puntentotnutoe.csv', 'situatie_1') as file:
            gegevens = '{},{},{}\n'.format(naam1, highscore, datum2)
            file.write(gegevens)
    elif inp == 'situatie_2':
        cleans = []
        with open('puntentotnutoe', 'r') as infile:
            tekst = csv.reader(infile)
            for line in tekst:
                if naam1 == line[0]:
                    continue
                else:
                    cleans.append(line)
        with open('puntentotnutoe.csv', 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(cleans)
        with open('puntentotnutoe.csv', 'situatie_1') as outfile:
            gegevens = '{},{},{}\n'.format(naam1, highscore, datum2)
            outfile.write(gegevens)

def INDEX_highscore_van_ALTIJD():
    """
    Het csv bestand wordt geopend en de score wordt toegevoegd op rij 1, vervolgens wordt de index gesorteerd op de hoogte van de scores. Alleen de hoogste score wordt gereturned.
    """
    with open('puntentotnutoe.csv', 'r') as infile:
        tekst = csv.reader(infile)
        scores = []
        for row in tekst:
            scores.append(int(row[1]))
        index = scores.index(max(scores))
        return index

def hoogstescore():
    """
    Als de index uit een andere functie even hoog is als de index van een bepaalde row, dan returned hij de row van de index met dezelfde score.
    :return:
    """
    with open('puntentotnutoe.csv', 'r') as infile:
        tekst = csv.reader(infile)
        i = 0
        for row in tekst:
            if INDEX_highscore_van_ALTIJD() == i:
                return row
            i += 1
        datum = datetime.datetime.now()
        datum2 = datum.strftime('%d %b %Y')
        lst = ['Tester', '-1', datum2]
        return lst

def highscore_vd_dag_DATA():
    """
    Het csv bestand wordt geopend. Als de row dezelfde datum heeft als een andere, worden de gegevens toegevoegd aan rij 2.
    """
    with open('puntentotnutoe.csv', 'r') as infile:
        tekst = csv.reader(infile)
        datum = datetime.datetime.now()
        datum2 = datum.strftime('%d %b %Y')
        gegevens = []
        for row in tekst:
            if row[2] == datum2:
                gegevens.append(row)
        return gegevens

def highscore_vd_dag():
    """
    De score wordt toegevoegd aan de highscore van de dag lijst met daarbij de tijd van de behaalde score.
    """
    scores = []
    for input in highscore_vd_dag_DATA():
        scores.append(input[1])
    if len(scores) > 0:
        index = scores.index(max(scores))
        return highscore_vd_dag_DATA()[index]
    else:
        datum = datetime.datetime.now()
        date = datum.strftime('%d %b %Y')
        lst = ['Tester', '-1', date]
        return lst

def highscore_van_ALTIJD(naam_diewordtgetoond):
    """
    Het csv bestand wordt geopend. De highscore wordt opgeslagen op de hoogste rij. Dit is de rij die wordt getoond op de highscore pagina.
    """
    with open('puntentotnutoe.csv', 'r') as infile:
        tekst = csv.reader(infile)
        for row in tekst:
            if row[0] == naam_diewordtgetoond:
                return row[1]

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

loginbutton = Button(master=loginframe, text='Start', command=lambda:[login(),textweg(),showpoints(), eersteHint(), descripText(), kiesHero()])
loginbutton.pack(side=LEFT, padx=20, pady=20)
loginbutton = Button(master=loginframe, text='View Highscore', command=highscore)
loginbutton.pack(side=RIGHT, padx=20, pady=20)

#Code voor het spelscherm
hoofdframe = Frame(master=root)
answerField = Entry(master=hoofdframe, text='API call hier')
answerField.pack(padx=320, pady=250)
#loginfield.place(relx=1, x=100, y=400, anchor=NE)
hoofdframe.pack(fill="both", expand=True)
hintbutton = Button(master=hoofdframe, text='Nieuwe hint (-3 punten!)', command=lambda:[puntenaftrek(),showpoints(True),checkpoints(points), nieuweHint(), descripText()])
hintbutton.pack(side=LEFT, padx=20, pady=5)
answerButton = Button(master=hoofdframe, text='Antwoord controleren!', command=lambda:[checkAnswer(), checkpoints(points), showpoints(True)])
answerButton.pack(side=RIGHT, padx=20, pady=5)

#Code voor het victoryScreen
#victoryframe = Frame(master=root)
#victoryLabel = Text(master=victoryframe, height=2, width=30)
#victoryLabel.pack()
#victoryLabel.insert(END, 'lekker bezig #doehetvoordiptish')

toonLoginFrame()
root.mainloop()
