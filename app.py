import os
import psycopg2
#from database import botreply

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

from flask import Flask, request, abort

from linebot import models

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

app = Flask(__name__)

# get channel_secret and channel_access_token dari environment variable
line_bot_api = LineBotApi('SBPEWYuYoFURRu8csRutLh81hb6/kZKdZJW7/nsKl/ejHOztWSqyocl65dQQ0blqFy/D9VxrVPu7q7pTNqcG2GBaE4WpDlZDCEL6vmNYbzZWS880cmof2VQV+yXzQOGQCdXX3W8FiG6J8KdjI9KxLQdB04t89/1O/w1cDnyilFU=') #channel_access_token
handler = WebhookHandler('8c1db447eeab98cf91ba66189530563b') #channel_secret

#webhook handler untuk melakukan koneksi ke LINE
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

from database import botreply

if __name__ == "__main__":
    app.run()
