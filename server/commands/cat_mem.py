import commandSystem
import random
from mongo import return_mongo


def cat_mem():
    attachment = random.choice(return_mongo(collection='cat_memes', id_='id'))
    return None, attachment


cat_mem_command = commandSystem.Command()

cat_mem_command.keys = ['дай мем с котиком', 'кинь мем с котиком', 'хочу мем с котиком',
                        'дай мем с котом', 'кинь мем с котом', 'хочу мем с котом',
                        'кинь мем с киской', 'хочу мем с киской', 'дай мем с киской']

cat_mem_command.process = cat_mem