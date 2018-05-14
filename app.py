import os
import psycopg2

DATABASE_URL = os.environ['postgres://tihcftwwysmzoe:f632c3c92714cf4495951b18384558f23d3be9166ec55d1d70506d80229091ab@ec2-174-129-41-64.compute-1.amazonaws.com:5432/d12u54927hlqno']

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

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable


line_bot_api = LineBotApi('lV5dotbVQarTPp3UnIln+3DtG3L+RpDJOnYwfd4Hh/uFxGK3IPnR1zVSmEvGAiD+Fy/D9VxrVPu7q7pTNqcG2GBaE4WpDlZDCEL6vmNYbzbZnzc2fBpTCuACvjdpKkaYwQKStQX92jK0yUdKqN+FBQdB04t89/1O/w1cDnyilFU=')
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
            TextSendMessage(text="Selamat pagi, ada yang bisa Yooka bantu?"))
    elif(b=="selamat siang"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Selamat siang, ada yang bisa Yooka bantu?"))
    elif(b=="selamat sore"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Sore, Boss! Apa yang bisa Yooka bantu?"))
    elif(b=="ngga ada"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="yaudah kalo ngga ada, bhay!"))
    elif(b=="mau tanya dong tentang unsada"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Kamu bisa cek info lengkapnya disini: www.unsada.ac.id"))
    elif(b=="hai"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Hai juga"))
    elif(b=="kamu siapa"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Aku Yooka, anak kampus UNSADA yang paling keren dan berwibawa. Aku bisa kasih kamu bermacam-macam informasi seputar UNSADA."))
    elif(b=="yooka, saya mau tanya di unsada ada jurusan teknik informatika ngga"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Ada dong! Yooka kan anak informatika UNSADA :)"))
    elif(b=="yooka, jadwal masuk kuliah kapan ya"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="coba login dulu di portal.unsada.ac.id nanti kamu bisa cek langsung disitu. Lengkap kok!"))
    elif(b=="yooka angkatan berapa"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="lagi masa-masa kelam mengurus Kerja Praktek sama Skripsi nih. Jangan tanya angkatan berapa ya :)"))
    elif(b=="question"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="answer"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Yooka blm bisa jawab chat kamu. Coba chat yang lain, mungkin aku bisa jawab hohoho"))


if __name__ == "__main__":
    app.run()
