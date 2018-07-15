import os
import psycopg2

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
    elif(b=="info pmb"):
        line_bot_api.reply_message(
            event.reply_token,
            {
                "type": "template",
                "altText": "this is a buttons template",
                "template": {
                    "type": "buttons",
                    "actions": [
                    {
                        "type": "message",
                        "label": "Pendaftaran PMB",
                        "text": "Informasi pendaftaran PMB"
                    },
                    {
                        "type": "uri",
                        "label": "Web Unsada",
                        "uri": "https://unsada.ac.id"
                    },
                    {
                        "type": "postback",
                        "label": "Biaya Kuliah",
                        "text": "Biaya Kuliah di Unsada",
                        "data": "data_biaya_kuliah"
                    },
                    {
                        "type": "message",
                        "label": "Daftar Jurusan",
                        "text": "Data Fakultas Unsada"
                    }
                    ],
                    "thumbnailImageUrl": "SPECIFY_YOUR_IMAGE_URL",
                    "title": "Info PMB",
                    "text": "Informasi Penerimaan Mahasiswa Baru"
                    }
            })
    elif(b=="hai"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Hai juga"))
    elif(b=="kamu siapa"):
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
            TextSendMessage(text="Aduh, sorry nih. Kayaknya soal itu aku belum ngerti."))


if __name__ == "__main__":
    app.run()
