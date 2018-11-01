import csv
import time

playerName = 'agagsaf'
score = 23
def HighscoreFileAanmaken():
    'Maakt de bestanden aan als deze nog niet bestaan.'
    try:
        myfile = open('HighscoreAlltime.csv', 'r')
        myfile.close()

    except FileNotFoundError:
        with open('HighscoreAlltime.csv', 'w') as myfile:
            myfile.write('\'Name\', \'Score\', \'Date\'\n')
    try:
        myfile = open('HighscoreDaily.csv', 'r')
        myfile.close()

    except FileNotFoundError:
        with open('HighscoreDaily.csv', 'w') as myfile:
            myfile.write('\'Name\', \'Score\', \'Date\'\n')
    try:
        myfile = open('DateCheck.txt', 'r')
        myfile.close()
    except FileNotFoundError:
        with open('DateCheck.txt', 'w') as myfile:
            myfile.write(time.strftime('%A'))





def writeScoreNameDate():
    'Eerst wordt er gekeken of de Daily highscore gereset moet worden. Daarna shrijft de naam, score, en datum naar beide Highscore csv files. '
    global playerName, score, day
    # kijkt of de dag vandaag overeen komt met de dag van de meest recente score. Als de dagen verschillen leegt het de dailhighscore file.
    with open('DateCheck.txt', 'r') as myfile:
        dagcheck = myfile.readline()
        if dagcheck == '':
            myfile.write(time.strftime('%A'))
        if time.strftime('%A') != dagcheck:
            with open('HighscoreDaily.csv', 'w') as myfile:
                myfile.write('\'Name\', \'Score\', \'Date\'\n')
    date = time.strftime('%A %d %B %Y %H:%M:%S')
    # De playername, score en datum worden in beide files geschreven.
    with open('HighscoreAlltime.csv', 'a') as myfile:
        myfile.write(playerName)
        myfile.write(',')
        myfile.write(str(score))
        myfile.write(',')
        myfile.write(date)
        myfile.write('\n')
    with open('HighscoreDaily.csv', 'a') as myfile:
        myfile.write(playerName)
        myfile.write(',')
        myfile.write(str(score))
        myfile.write(',')
        myfile.write(date)
        myfile.write('\n')
    with open('DateCheck.txt', 'w') as myfile:
        myfile.write(time.strftime('%A'))


def HighestScoreAlltime():
    'Zoekt de hoogste Score met de bijbehoorende naam en datum en slaat deze op in HighscoreAlltime.csv'
    with open('HighscoreAlltime.csv', 'r') as myfile:
        reader = csv.reader(myfile, delimiter=',')
        next(reader,None)
        hoogesteScoreAlltime = 0
        highscorenameAlltime = ''
        highscoredateAlltime = ''
        for row in reader:
            # Als er een hogere score dan de vorige voorbij komt overschrijft hij de score met de hogere score
            if int(row[1]) >= int(hoogesteScoreAlltime):
                hoogesteScoreAlltime = row[1]
                highscorenameAlltime = row[0]
                highscoredateAlltime = row[2]
        print('De hoogste alltime score is behaald door {} met {} punten op {}'.format(highscorenameAlltime, hoogesteScoreAlltime, highscoredateAlltime))
        HighScoreAlltime = 'De hoogste alltime score is behaald door {} met {} punten op {}'.format(highscorenameAlltime, hoogesteScoreAlltime, highscoredateAlltime)

def HighestScoreDaily():
    'Zoekt de hoogste Score met de bijbehoorende naam en datum en slaat deze op in HighscoreDaily.csv'
    with open('HighscoreDaily.csv', 'r') as myfile:
        reader = csv.reader(myfile, delimiter=',')
        next(reader,None)
        hoogesteScoreDaily = 0
        highscorenameDaily = ''
        highscoredateDaily = ''
        for row in reader:
            # Als er een hogere score dan de vorige voorbij komt overschrijft hij de score met de hogere score
            if int(row[1]) >= int(hoogesteScoreDaily):
                hoogesteScoreDaily = row[1]
                highscorenameDaily = row[0]
                highscoredateDaily = row[2]
        print('De hoogste score vandaag is behaald door {} met {} punten op {}'.format(highscorenameDaily, hoogesteScoreDaily, highscoredateDaily))
        HighscoreDaily = 'De hoogste score vandaag is behaald door {} met {} punten op {}'.format(highscorenameDaily, hoogesteScoreDaily, highscoredateDaily)

def highscore():
    HighscoreFileAanmaken()
    writeScoreNameDate()
    HighestScoreDaily()
    HighestScoreAlltime()

highscore()
playerName = 'test'
score = 342
highscore()
playerName = 'qwert'
score = 43
highscore()
playerName = 'higtorlcnvubiuaerldbh'
score = 9876
highscore()
day = 'Saturday'
playerName = 'byuhbuigiigerfvbdfjhgufdhuihgf'
score = 21
highscore()