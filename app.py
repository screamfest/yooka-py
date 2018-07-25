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
from linebot import (
    LineBotApi, WebhookHandler,
)
from linebot.exceptions import (
    InvalidSignatureError
)

#import models from linebot folder untuk aktivasi model message di dalam pengiriman pesan ke user
from quickmenu import (
    QuickMenu, QuickMenuManager
)
from linebot import models
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

# Setup RichMenuManager
channel_access_token = "SBPEWYuYoFURRu8csRutLh81hb6/kZKdZJW7/nsKl/ejHOztWSqyocl65dQQ0blqFy/D9VxrVPu7q7pTNqcG2GBaE4WpDlZDCEL6vmNYbzZWS880cmof2VQV+yXzQOGQCdXX3W8FiG6J8KdjI9KxLQdB04t89/1O/w1cDnyilFU="
quickman = QuickMenuManager(channel_access_token)

#####SETUP YOOKA QUICK MENU
# Setup RichMenu to register
quickm = QuickMenu(name="Quick Menu", chat_bar_text="Open this menu")
quickm.add_area(0, 0, 1250, 843, "message", "テキストメッセージ")
quickm.add_area(1250, 0, 1250, 843, "uri", "http://imoutobot.com")
quickm.add_area(0, 843, 1250, 843, "postback", "data1=from_richmenu&data2=as_postback")
quickm.add_area(1250, 843, 1250, 843, "postback", ["data3=from_richmenu_with&data4=message_text", "ポストバックのメッセージ"])

# Register
res = quickman.register(quickm, "https://i.imgur.com/lTT9Axb.png")
richmenu_id = res["richMenuId"]
print("Registered as " + richmenu_id)

# Apply to user
user_id = "LINE_MID_TO_APPLY"
quickman.apply(user_id, richmenu_id)

# Check
res = quickman.get_applied_menu(user_id)
print(user_id  + ":" + res["richMenuId"])

################webhook handler untuk melakukan koneksi ke LINE
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
    ################ tier 1 - testing site
    if(b=="admin say yes"):
        line_bot_api.reply_message(
            event.reply_token, 
            TextSendMessage(
                text=a + ", Yooka say no!"))
    elif(b=="test"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=a))
    ################ tier 2 - info pmb
    elif(b=="info pmb"):
        line_bot_api.reply_message(
            event.reply_token, 
            TemplateSendMessage(
            alt_text='informasi pmb',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://example.com/item1.jpg', #addimagehere
                        action=MessageAction(
                            label='Periode PMB', #label tidak boleh lebih dari 12 character
                            text='periode pmb unsada',
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://example.com/item2.jpg', #addimagehere
                        action=MessageAction(
                            label='Jurusan',
                            text='daftar fakultas dan jurusan di unsada'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://example.com/item3.jpg', #addimagehere
                        action=MessageAction(
                            label='Tata Cara',
                            text='persyaratan seleksi masuk unsada'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://example.com/item4.jpg', #addimagehere
                        action=MessageAction(
                            label='Hasil Ujian',
                            text='pengumuman ujian seleksi masuk unsada'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://example.com/item5.jpg', #addimagehere
                        action=MessageAction(
                            label='Lokasi',
                            text='lokasi unsada'
                        )
                    )
                ]
            )
        )
        )
    ################ tier 2 - info unsada
    elif(b=="info unsada"):
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
            alt_text='Info Unsada',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item1.jpg', #addimagehere
                    title='Jadwal Kuliah',
                    text='Informasi jadwal kuliah untuk Mahasiswa UNSADA',
                    actions=[
                        MessageAction(
                            label='Lihat Jadwal',
                            text='lihat jadwal kuliah'
                        ),
                        URIAction(
                            label='Portal Unsada',
                            uri='http://portal.unsada.ac.id'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item2.jpg', #addimagehere
                    title='UTS',
                    text='Informasi jadwal UTS untuk Mahasiswa UNSADA',
                    actions=[
                        MessageAction(
                            label='Jadwal UTS',
                            text='lihat jadwal UTS'
                        ),
                        MessageAction(
                            label='Nilai UTS',
                            text='lihat nilai UTS'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item2.jpg', #addimagehere
                    title='UAS',
                    text='Informasi jadwal UAS untuk Mahasiswa UNSADA',
                    actions=[
                        MessageAction(
                            label='Jadwal UAS',
                            text='lihat jadwal UAS'
                        ),
                        MessageAction(
                            label='Nilai UAS',
                            text='lihat nilai UAS'
                        )
                    ]
                )
            ]
        )
        )
    )
    ################ tier 2 - info tambahan lainnya - NEXT DEVELOPMENT
    
    ################ tier 3 - feedback
    elif(b=="daftar fakultas dan jurusan di unsada"):
        line_bot_api.reply_message(
            event.reply_token, 
            ImagemapSendMessage(
                base_url='https://example.com/richmenupict.jpg', #addimagehere
                alt_text='daftar fakultas dan jurusan di unsada',
                base_size=BaseSize(height=1040, width=1040),
                actions=[
                    MessageImagemapAction(
                        text='Fakultas Sastra',
                        area=ImagemapArea(
                            x=0, y=0, width=520, height=1040
                        )
                    ),
                    MessageImagemapAction(
                        text='Fakultas Teknik',
                        area=ImagemapArea(
                            x=520, y=0, width=520, height=1040
                        )
                    ),
                    MessageImagemapAction(
                        text='Fakultas Ekonomi',
                        area=ImagemapArea(
                            x=0, y=520, width=520, height=1040
                        )
                    ),
                    MessageImagemapAction(
                        text='Fakultas Teknik Kelautan',
                        area=ImagemapArea(
                            x=520, y=520, width=520, height=1040
                        )
                    )
                ]
            )
        )
    elif(b=="lokasi unsada"):
        line_bot_api.reply_message(
            event.reply_token, 
            LocationSendMessage(
                title='Universitas Darma Persada',
                address='Jakarta Timur',
                latitude=-6.230059,
                longitude=106.924653
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
