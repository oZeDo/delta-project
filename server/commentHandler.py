from commentSender import get_image_url
from commandSystem import command_list
from fuzzywuzzy import process
import commentSender
import importlib
import os
import re


def load_modules():
    files = os.listdir("/home/ubuntu/server/commands/")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def get_answer(body):
    if len(body)>4:
        reg = re.compile('\d+')
        for c in command_list:
            string = process.extract(query=reg.sub('', body), choices=c.keys)
            print(string)
            string = string[0]
            if int(string[1]) > 90:
                message, attachment = c.process()
                try:
                    attachment = get_image_url(attachment)
                except TypeError:
                    pass
                return message, attachment
    return None, None


def create_answer(post_id, site, text=None, reply_to=None):
    load_modules()
    if commentSender.check(var=site, post_id=post_id):
        print(site, "полигон")
        text, link = get_answer(text)
        if text or link:
            commentSender.send(post_id=post_id, attachment_link=link, var=site, text=text, reply_to=reply_to)
    else:
        print(site, "не полигон")
