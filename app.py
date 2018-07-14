import os
import psycopg2
import random

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from botresponses import (
    bot_responses
)

app = Flask(__name__)


line_bot_api = LineBotApi('lV5dotbVQarTPp3UnIln+3DtG3L+RpDJOnYwfd4Hh/uFxGK3IPnR1zVSmEvGAiD+Fy/D9VxrVPu7q7pTNqcG2GBaE4WpDlZDCEL6vmNYbzbZnzc2fBpTCuACvjdpKkaYwQKStQX92jK0yUdKqN+FBQdB04t89/1O/w1cDnyilFU=') #channel access token
handler = WebhookHandler('1891eb6bb7a1dc770e8ce73fb9ec22f0') #channel secret


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    a = event.message.text
    b = a.lower()
    if b in user_responses:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=bot_responses))


#handler message yang sudah sukses
"""
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    a = event.message.text
    b =a.lower()
    if(b=="test"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=a))
    elif(b=="assalamualaikum"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Waalaikumsalam"))
    elif(b=="selamat pagi"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Selamat pagi!"))
    elif(b=="selamat siang"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Selamat siang!"))
    elif(b=="selamat sore"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Sore, boss!"))
    elif(b=="hai"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Hai kamu yang disana :)"))
    elif(b=="halo"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Aloha!"))
    elif(b=="ngga ada"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="yaudah kalo ngga ada, bhay!"))
    elif(b=="mau tanya dong tentang unsada"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Kamu bisa cek info lengkapnya disini: www.unsada.ac.id"))
    elif(b=="siapa kamu"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Aku Yooka, anak kampus UNSADA yang paling keren dan berwibawa. Aku bisa kasih kamu bermacam-macam informasi seputar UNSADA."))
    elif(b=="question"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="answer"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Mohon maaf, Yooka belum dapat menjawab pertanyaan kamu. Coba pilih bantuan menu dibawah ya!"))
"""

if __name__ == "__main__":
    app.run()
