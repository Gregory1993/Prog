import csv
import json
from threading import Timer

while True:

    fieldnames = ['type', 'username', 'score', 'ID']
    username = input("What is your name? ")
    score = int(input("What is your score? "))

    class Structure:
        username = ""
        score = int(0)
        ID = int(0)


    alltime = Structure()
    daily = Structure()


    def getOldScores():
        with open('punten.csv') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["type"] == "alltime":
                    alltime.username = row["username"]
                    alltime.score = int(row["score"])
                elif row["type"] == "daily":
                    daily.username = row["username"]
                    daily.score = int(row["score"])
                    daily.ID = int(row["ID"])



    def checkScores():
        getOldScores()
        if score > alltime.score:
            sendMessage(0)
            alltime.username = username
            alltime.score = score
            daily.username = username
            daily.score = score
            daily.ID = daily.ID + 1
            writeChanges()
            t = Timer(24 * 60 * 60, resetDaily, args=str(daily.ID))
            t.start()
        elif score > daily.score:
            sendMessage(1)
            daily.username = username
            daily.score = score
            daily.ID = daily.ID + 1
            writeChanges()
            t = Timer(24 * 60 * 60, resetDaily, args=str(daily.ID))
            t.start()
        else:
            sendMessage(2)


    def writeChanges():
        with open('punten.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'type': 'alltime', 'username': alltime.username, 'score': alltime.score})
            writer.writerow({'type': 'daily', 'username': daily.username, 'score': daily.score, 'ID': daily.ID})


    def sendMessage(result):
        if result == 0:
            print("New alltime highscore achieved!")
        elif result == 1:
            print("New daily highscore achieved!")
        elif result == 2:
            print("Better luck next time!")

    def resetDaily(dailyID):
        getOldScores()
        if int(dailyID) == int(daily.ID):
            daily.username = "none"
            daily.score = int(0)
            writeChanges()
            print("daily reset")


    checkScores()