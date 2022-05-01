import re
from flask import Flask, render_template, send_from_directory, redirect, request
import requests
import json


app = Flask(__name__, template_folder=".")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/styles/<path:path>")
def styles(path):
    return send_from_directory("./styles", path)

@app.route("/img/<path:path>")
def img(path):
    return send_from_directory("./img", path)

@app.route("/sent-contact-form", methods=["POST"])
def contact_form():
    name = request.form.get("name")
    phone = request.form.get("phone")

    bot_send_message = "https://api.telegram.org/bot5354006189:AAGZuON0rsvCC9oyvEcpM89XP9VxdV9xKdA/sendMessage"
    chat_id = "-608069909"
    text = " *Новый перебезчик на темную сторону\!* \n" + \
               "Его имя:      ***{0}*** \n" + \
               "Его телефон:  ***{1}***"

    headers = {
        "Content-Type": "application/json"
    }
    body = json.dumps({
        "text": text.format(name, phone),
        "parse_mode": "MarkdownV2",
        "chat_id": chat_id
    })

    r = requests.post(url=bot_send_message, headers=headers, data=body)

    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8077", debug=True)