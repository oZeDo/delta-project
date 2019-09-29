import commandSystem
import random
from mongo import return_mongo


def rjomba():
    message = ''
    attachment = random.choice(return_mongo(collection='rjomba', id_='id'))
    return message, attachment


rjomba_command = commandSystem.Command()

rjomba_command.keys = ['кинь ржомбу', 'дай ржомбу', 'хочу ржомбу']
rjomba_command.process = rjomba
