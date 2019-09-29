import commandSystem
import random
from mongo import return_mongo


def cat():
    text = 'Вот вам котик :) \n В следующий раз я пришлю тебе другого котика'
    attachment = random.choice(return_mongo(collection='cat', id_='id'))
    return text, attachment


cat_command = commandSystem.Command()

cat_command.keys = ['дай котика', 'хочу котика' 'кинь котика',
                    'дай кота', 'хочу кота', 'кинь киску']

cat_command.process = cat