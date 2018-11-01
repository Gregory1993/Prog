import csv
import json
from threading import Timer

points = 12
playerName = 'randomname'

score = points


    fieldnames = ['type', 'playerName', 'score', 'ID']

    class Structure:
        playerName = ""
        score = int(0)
        ID = int(0)


    alltime = Structure()
    daily = Structure()


    def getOldScores():
        with open('punten.csv', 'r+') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["type"] == "alltime":
                    alltime.playerName = row["playerName"]
                    alltime.score = int(row["score"])
                elif row["type"] == "daily":
                    daily.playerName = row["playerName"]
                    daily.score = int(row["score"])
                    daily.ID = int(row["ID"])



    def checkScores():
        getOldScores()
        if score > alltime.score:
            sendMessage(0)
            alltime.playerName = playerName
            alltime.score = score
            daily.playerName = playerName
            daily.score = score
            daily.ID = daily.ID + 1
            writeChanges()
            t = Timer(24 * 60 * 60, resetDaily, args=str(daily.ID))
            t.start()
        elif score > daily.score:
            sendMessage(1)
            daily.playerName = playerName
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
            writer.writerow({'type': 'alltime', 'playerName': alltime.playerName, 'score': alltime.score})
            writer.writerow({'type': 'daily', 'playerName': daily.playerName, 'score': daily.score, 'ID': daily.ID})


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
            daily.playerName = "none"
            daily.score = int(0)
            writeChanges()
            print("daily reset")


    checkScores()