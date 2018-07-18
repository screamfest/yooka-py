import os
import psycopg2
<<<<<<< HEAD
=======
import botbuttons
>>>>>>> 3b75af30f0813bbb8b993aacbc70f5eb8148add6

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
<<<<<<< HEAD
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
=======
from linebot.models.actions import (
    Action,
    PostbackAction,
    MessageAction,
    URIAction,
    DatetimePickerAction,
    Action as TemplateAction,  # backward compatibility
    PostbackAction as PostbackTemplateAction,  # backward compatibility
    MessageAction as MessageTemplateAction,  # backward compatibility
    URIAction as URITemplateAction,  # backward compatibility
    DatetimePickerAction as DatetimePickerTemplateAction,  # backward compatibility
)
from linebot.models.base import (
    Base,
)
from linebot.models.error import (
    Error,
    ErrorDetail,
)
from linebot.models.events import (
    Event,
    MessageEvent,
    FollowEvent,
    UnfollowEvent,
    JoinEvent,
    LeaveEvent,
    PostbackEvent,
    AccountLinkEvent,
    BeaconEvent,
    Postback,
    Beacon,
    Link,
)
from linebot.models.messages import (
    Message,
    TextMessage,
    ImageMessage,
    VideoMessage,
    AudioMessage,
    LocationMessage,
    StickerMessage,
    FileMessage,
)
from linebot.models.imagemap import (
    ImagemapSendMessage,
    BaseSize,
    ImagemapAction,
    URIImagemapAction,
    MessageImagemapAction,
    ImagemapArea,
)
from linebot.models.responses import (
    Profile,
    MemberIds,
    Content,
    RichMenuResponse,
    Content as MessageContent,
)
from linebot.models.flex_message import (
    FlexSendMessage,
    FlexContainer,
    BubbleContainer,
    BubbleStyle,
    BlockStyle,
    CarouselContainer,
    FlexComponent,
    BoxComponent,
    ButtonComponent,
    FillerComponent,
    IconComponent,
    ImageComponent,
    SeparatorComponent,
    SpacerComponent,
    TextComponent
)
from linebot.models.rich_menu import (
    RichMenu,
    RichMenuSize,
    RichMenuArea,
    RichMenuBounds,
)
from linebot.models.send_messages import (
    SendMessage,
    TextSendMessage,
    ImageSendMessage,
    VideoSendMessage,
    AudioSendMessage,
    LocationSendMessage,
    StickerSendMessage,
)
from linebot.models.sources import (
    Source,
    SourceUser,
    SourceGroup,
    SourceRoom,
)
from linebot.models.template import (
    TemplateSendMessage,
    Template,
    ButtonsTemplate,
    ConfirmTemplate,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
>>>>>>> 3b75af30f0813bbb8b993aacbc70f5eb8148add6
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

<<<<<<< HEAD

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    a = event.message.text
    b =a.lower()
=======
@handler.add(MessageEvent, message=TextMessage)
def usual_message(event):
    a = event.message.text
    b = a.lower()
>>>>>>> 3b75af30f0813bbb8b993aacbc70f5eb8148add6
    if(b=="test"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=a))
<<<<<<< HEAD
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
=======
    elif(b=="info pmb"):
        line_bot_api.reply_message(
            event.reply_token, 
            TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='Informasi Penerimaan Mahasiswa Baru',
        actions=[
            PostbackAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageAction(
                label='message',
                text='message text'
            )
        ]
    )
)
        )
    elif(b=="lokasi unsada"):
        line_bot_api.reply_message(
            event.reply_token, LocationSendMessage(
                title='Universitas Darma Persada',
                address='Jakarta Timur',
                latitude=35.65910807942215,
                longitude=139.70372892916203
            ))
    elif(b=="siapa kamu"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Yooka"))
>>>>>>> 3b75af30f0813bbb8b993aacbc70f5eb8148add6
    elif(b=="question"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="answer"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
<<<<<<< HEAD
            TextSendMessage(text="Yooka blm bisa jawab chat kamu. Coba chat yang lain, mungkin aku bisa jawab hohoho"))
=======
            TextSendMessage(text="wah, sorry nih. Tampaknya soal itu aku belum paham. Coba cek Menu bantuan dibawah."))
>>>>>>> 3b75af30f0813bbb8b993aacbc70f5eb8148add6


if __name__ == "__main__":
    app.run()
