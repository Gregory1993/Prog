import json as serializer
from tkinter import *

def situatie(naam1, naam2, highscore):
    """
    Openen van het puntentotnutoe csv bestand en kijken tijdens welke situaties we de score opslaan.
    """
    with open('puntentotnutoe.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            naam2.append(rij[0])
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
