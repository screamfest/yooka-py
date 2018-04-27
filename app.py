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


line_bot_api = LineBotApi('DWuMGd04tRmRhlAzOnY++fWTy4pud23Ht0tphKJa3a1jddJMRYkrg6wYJkc/0x3vCHtj/R71zRtxJBXEPbpx5VyPsQMfVhf2lftDAON5RODKtsC+PZ+SbzQfTqU4ka67qsghdSZxSViWJPsYbZVEoAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7426f045e38ab7ad11f4b171f1ff0e42')


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
            TextSendMessage(text="Selamat pagi,ada yang bisa saya bantu?"))
    elif(b=="selamat siang"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Selamat siang, ada yang bisa saya bantu?"))
    elif(b=="selamat sore"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Selamat sore"))
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="yang bisa saya bantu?"))
    elif(b=="saya ingin bertanya tentang unsada"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Anda Dapat membukanya di halaman website kami www.unsada.ac.id"))
    elif(b=="hai"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Hai juga"))
    elif(b=="kamu siapa?"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Saya Yooka Petugas PMB Unsada"))
    elif(b=="yooka saya mau tanya di unsada ada jurusan teknik informatika?"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Ya ada Yooka juga anak informatika ko"))
    elif(b=="yooka saya mau tanya jadwal masuk kuliah kapan yah"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="untuk mengetahui tentang jadwal kuliah anda harus login ke SIA Unsada dahulu."))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Yooka blm bisa jawab pertanyaan kamu mohon maaf yah..."))


if __name__ == "__main__":
    app.run()
