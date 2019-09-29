import commandSystem
import random


def coinflip():
    if random.randint(1, 2) == 2:
        return 'Орел!', None
    else:
        return 'Решка!', None


coinflip_command = commandSystem.Command()

coinflip_command.keys = ['подкинь монетку', 'бросок монетки', 'coin flip', 'кинь монетку']
coinflip_command.process = coinflip
