import random
def randomHero():
    'Deze functie werkt met een lijst van 10 heroes afkomstig uit de API. Vervolgens wordt uit deze API 10 heroes gekozen en hiervoor wordt een willekeurige gelecteerd'
    lst_of_heroes = ['Hero 1', 'Hero 2', 'Hero 3', 'Hero 4', 'Hero 5', 'Hero 6', 'Hero 7', 'Hero 8', 'Hero 9', 'Hero 10'] #Deze data moet van de API komen!
    number = random.randint(1,10)
    print(lst_of_heroes[number])