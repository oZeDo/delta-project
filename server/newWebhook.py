import requests
from variables import urls, headers


def create_webhook(url, header, string):
    requests.post(headers=header, url=url+"/webhooks/add",
                  data={"event": "new_comment", "url": "http://demo13.alpha.vkhackathon.com/"+string})


def delete_webhook(url, header):
    requests.post(headers=header, url=url+"/webhooks/del", data={"event": "all"})


for i in ['tj', 'vc', 'dtf']:
    create_webhook(urls[i], headers[i], i)

