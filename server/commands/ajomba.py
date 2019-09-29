import commandSystem
import random
from mongo import return_mongo


def ajomba():
    attachment = random.choice(return_mongo(collection='ajomba', id_='id'))
    return None, attachment


ajomba_command = commandSystem.Command()

ajomba_command.keys = ['кинь антиржомбу', 'дай антиржомбу', 'хочу антиржомбу']
ajomba_command.process = ajomba
