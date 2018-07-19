import os
import psycopg2
import botbuttons

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
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
def usual_message(event):
    a = event.message.text
    b = a.lower()
    if(b=="test"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=a))
    elif(b=="image carousel"):
        line_bot_api.reply_message(
            event.reply_token, 
            TemplateSendMessage(
            alt_text='Image carousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://example.com/'
                                  'item1.jpg',
                        action=PostbackAction(
                            label='postback1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://example.com'
                                  '/item2.jpg',
                        action=MessageAction(
                            label='message2',
                            text='message text2'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://example.com/'
                                  'item3.jpg',
                        action=URIAction(
                            label='uri1',
                            uri='https://example.com/1'
                        )
                    )
                ]
            )
        )
        )
    elif(b=="lokasi unsada"):
        line_bot_api.reply_message(
            event.reply_token, 
            LocationSendMessage(
                title='Universitas Darma Persada',
                address='Jakarta Timur',
                latitude=35.65910807942215,
                longitude=139.70372892916203
            ))
    elif(b=="confirm message"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                text='Are you sure?',
                actions=[
                    PostbackAction(
                        label='postback', display_text='postback text',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='message', text='message text'
                    )
                ]
            )
            )
    elif(b=="question"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="answer"))
    elif(b=="siapa kamu"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Yooka"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="wah, sorry nih. Tampaknya soal itu aku belum paham. Coba cek Menu bantuan dibawah."))


if __name__ == "__main__":
    app.run()
