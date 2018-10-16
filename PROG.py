import random
def randomHero():
    'Deze functie werkt met een lijst van 10 heroes afkomstig uit de API. Vervolgens wordt uit deze API 10 heroes gekozen en hiervoor wordt een willekeurige geselecteerd'
    lst_of_heroes = ['Hero 1', 'Hero 2', 'Hero 3', 'Hero 4', 'Hero 5', 'Hero 6', 'Hero 7', 'Hero 8', 'Hero 9', 'Hero 10'] #Deze data moet van de API komen!
    number = random.randint(1,10)
    print(lst_of_heroes[number])
public_key = 56235b4ce6e75a0b4bb2d844d6c7abf8
private_key = 66072693baa29d8c45e1f117d84b2eeda0fa66a4
