import requests
import json


def send_comment(url, data, header):
    print(url)
    print(header)
    print(json.dumps(data, indent=4, ensure_ascii=False))
    request = requests.post(headers=header,  data=data, url=url+"/comment/add")
#    print(request.status_code)
#    print(json.dumps(request.json(), indent=4, ensure_ascii=False))


def send_article(url, data, header):
    resp = requests.post(headers=header, url=url+"/entry/create", data=data)
    print(resp.status_code, resp.json())


def get_article(url, header, string):
    resp = requests.get(headers=header, url=url+"/entry/"+string).json()
    try:
        return resp["result"]
    except KeyError:
        print(resp)

def get_public_sections(url, header):
    request = requests.get(headers=header, url=url+"/subsites_list/sections")
    print(request.status_code)
    print(json.dumps(request.json(), indent=4, ensure_ascii=False))


def process_attachment(url, data_url, header):
    if data_url:
        request = requests.post(headers=header,
                                url=url+"/uploader/extract",
                                data={"url": data_url})
        print("extract картинки: ", request.status_code)
        return str(json.dumps(request.json()["result"], indent=4, ensure_ascii=False))
    else:
        return None


