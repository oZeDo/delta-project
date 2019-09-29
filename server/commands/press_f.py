import commandSystem
import random
from mongo import return_mongo


def press():
    attachment = random.choice(return_mongo(collection='f', id_='id'))
    return None, attachment


press_command = commandSystem.Command()

press_command.keys = ['press f', 'пресс эф', 'press эф', 'пресс f']
press_command.process = press