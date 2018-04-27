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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=a))


if __name__ == "__main__":
    app.run()
