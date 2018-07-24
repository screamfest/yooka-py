from __future__ import unicode_literals

import os
import psycopg2
import json
import spacy
import rasa_nlu

from future.utils import with_metaclass
from abc import ABCMeta
from linebot.models import Base

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
from linebot.models.actions import (
    Action,
    PostbackAction,
    MessageAction,
    URIAction,
    DatetimePickerAction,
    Action as TemplateAction,
    PostbackAction as PostbackTemplateAction,
    MessageAction as MessageTemplateAction,
    URIAction as URITemplateAction,
    DatetimePickerAction as DatetimePickerTemplateAction,
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

from linebot import api, exceptions, http_client, utils, webhook
from linebot import models

line_bot_api = LineBotApi('SBPEWYuYoFURRu8csRutLh81hb6/kZKdZJW7/nsKl/ejHOztWSqyocl65dQQ0blqFy/D9VxrVPu7q7pTNqcG2GBaE4WpDlZDCEL6vmNYbzZWS880cmof2VQV+yXzQOGQCdXX3W8FiG6J8KdjI9KxLQdB04t89/1O/w1cDnyilFU=') #channel_access_token
handler = WebhookHandler('8c1db447eeab98cf91ba66189530563b') #channel_secret

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    a = event.message.text
    b = a.lower()
    if(b == "test"):
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
    elif(b=="siapa kamu"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Yooka"))
    elif(b=="question"):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="answer"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Aku ngga ngerti maksud kamu. Coba cek Quick Menu dibawah, mungkin bisa membantu."))