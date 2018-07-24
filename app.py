from __future__ import unicode_literals

import os
import psycopg2
import sys
import tempfile
import requests

#from var import *
from re import search
from random import random
from random import choice
from argparse import ArgumentParser
import spacy
import rasa_nlu
import random

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

from flask import (Flask, request, abort)
from linebot import models
from linebot import (
    LineBotApi, WebhookHandler,
)
from linebot.exceptions import (
    InvalidSignatureError
)
#import models from linebot folder untuk aktivasi model message di dalam pengiriman pesan ke user

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, 
    Action, PostbackAction, MessageAction, URIAction, DatetimePickerAction, Action as TemplateAction, PostbackAction as PostbackTemplateAction, MessageAction as MessageTemplateAction, URIAction as URITemplateAction, DatetimePickerAction as DatetimePickerTemplateAction,
    Base, Error, ErrorDetail, 
    Event, FollowEvent, UnfollowEvent, JoinEvent, LeaveEvent, PostbackEvent, AccountLinkEvent, BeaconEvent, Postback, Beacon, Link, 
    Message, TextMessage, ImageMessage, VideoMessage, AudioMessage, LocationMessage, StickerMessage, FileMessage, 
    ImagemapSendMessage, BaseSize, ImagemapAction, URIImagemapAction, MessageImagemapAction, ImagemapArea, 
    Profile, MemberIds, Content, RichMenuResponse, Content as MessageContent, 
    FlexSendMessage, FlexContainer, BubbleContainer, BubbleStyle, BlockStyle, CarouselContainer, FlexComponent, BoxComponent, ButtonComponent, FillerComponent, IconComponent, ImageComponent, SeparatorComponent, SpacerComponent, TextComponent, 
    TemplateSendMessage, Template, ButtonsTemplate, ConfirmTemplate, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn, 
    RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds,
    SendMessage, TextSendMessage, ImageSendMessage, VideoSendMessage, AudioSendMessage, LocationSendMessage, StickerSendMessage, 
    Source, SourceUser, SourceGroup, SourceRoom,
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
    """app.logger.info("Request body: " + body)"""

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
    if(b=="admin say yes"):
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(
                text=a + ", Yooka say no!"))
    #Info PMB-Tier1
    elif(b=="info pmb"):
        line_bot_api.reply_message(
            event.reply_token, 
            TemplateSendMessage(
                alt_text='image carousel text',
                template=ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url='https://example.com/item1.jpg',
                            action=MessageAction(
                                label='Periode Seleksi',
                                text='Periode seleksi mahasiswa baru UNSADA'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://example.com/item2.jpg',
                            action=MessageAction(
                                label='Daftar Fakultas & Jurusan',
                                text='Daftar Fakultas & Jurusan di UNSADA'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://example.com/item2.jpg',
                            action=MessageAction(
                                label='Persyaratan Pendaftaran',
                                text='Persyaratan Ujian'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://example.com/item2.jpg',
                            action=MessageAction(
                                label='Pengumuman Hasil Seleksi',
                                text='Pengumuman Hasil Seleksi Ujian Masuk UNSADA'
                            )
                        )
                ]
            )
        )
        )

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
            )
        )
    elif(b=="konfirmasi"):
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text='Confirm template',
                template=ConfirmTemplate(
                text='Are you sure?',
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
    elif(b=="carousel"):
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
            alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item1.jpg',
                    title='this is menu1',
                    text='description1',
                    actions=[
                        PostbackAction(
                            label='postback1',
                            text='postback text1',
                            data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
                        URIAction(
                            label='uri1',
                            uri='http://example.com/1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item2.jpg',
                    title='this is menu2',
                    text='description2',
                    actions=[
                        PostbackAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        ),
                        MessageAction(
                            label='message2',
                            text='message text2'
                        ),
                        URIAction(
                            label='uri2',
                            uri='http://example.com/2'
                        )
                    ]
                )
            ]
            )
            )
        )
    #Pertanyaan dasar
    elif(b=="siapa kamu"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="Yooka"
                )
            )
    elif(b=="pengumuman hasil seleksi ujian masuk unsada"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(
                text="CONNECTED!"
                )
            )
    # 
    elif(b=="question"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="answer"))

    #kalo semuanya ngga cocok keluarkan fallback message
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Aku ngga ngerti maksud kamu. Coba cek Quick Menu dibawah, mungkin bisa membantu."))


# handle join event
@handler.add(JoinEvent)
def handle_join(event):
    if event.source.type == 'group':
        line_bot_api.reply_message(
            event.reply_token,[
            TextSendMessage(text='Yo, saya Yooka!'),
            TextSendMessage(text='Salam kenal!')
            ])

# handle add event
@handler.add(LeaveEvent)
def handle_leave():
    """app.logger.info("Got leave event")"""

# handle postback event
@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'ping':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='pong'))

# handle beacon event
@handler.add(BeaconEvent)
def handle_beacon(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='Got beacon event. hwid={}, device_message(hex string)={}'.format(
                event.beacon.hwid, event.beacon.dm)))

if __name__ == "__main__":
    app.run()
