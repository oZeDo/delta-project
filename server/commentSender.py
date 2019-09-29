import vk
import api 
import operator
from variables import urls, headers, ids, vk_token


session = vk.Session(access_token=vk_token)
vk_api = vk.API(session, v=5.101)


def send(var, post_id, text=None, attachment_link=None, reply_to=None):
    text = '' if text == None else text
    comment_data = {
        "subsite_id": ids[var],
        "id": post_id,  # Айдишник статьи
        "reply_to": reply_to,  # Айдишник родительского сообщения
        "text": text,
        "attachments": api.process_attachment(url=urls[var], data_url=attachment_link, header=headers[var])
    }
    api.send_comment(url=urls[var], data=comment_data, header=headers[var])


def check(post_id, var):
    if ids[var] == str(api.get_article(string=str(post_id), header=headers[var], url=urls[var])["subsite"]["id"]):
        return True
    else:
        return False


def get_image_url(url):
    sample = {}
    for i in vk_api.photos.getById(photos=url[5:], extended=0, bool=0)[0]["sizes"]:
        sample[i["url"]] = i["width"] + i["height"]
    sample = sorted(sample.items(), key=operator.itemgetter(1), reverse=True)
    return sample[0][0]
