import logging
import commentHandler
from flask import Flask, request

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


# data['creator']['id'] айдишник пользователя
@app.route('/tj', methods=["POST"])
def web_hook_tj():
    if request.method == "POST":
        data = request.get_json()['data']
        commentHandler.create_answer(post_id=data["content"]["id"], reply_to=data['id'], text=data["text"], site='tj')
    return "ok"


@app.route('/dtf', methods=["POST"])
def web_hook_dtf():
    if request.method == "POST":
        data = request.get_json()['data']
        commentHandler.create_answer(post_id=data["content"]["id"], reply_to=data['id'], text=data["text"], site='dtf')
    return "ok"


@app.route('/vc', methods=["POST"])
def web_hook_vc():
    if request.method == "POST":
        data = request.get_json()['data']
        commentHandler.create_answer(post_id=data["content"]["id"], reply_to=data['id'], text=data["text"], site='vc')
    return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


