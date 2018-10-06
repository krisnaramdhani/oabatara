import errno#
import os#
import sys#
import tempfile#

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('3Lrey1+mjYoUAKXJdAkh6IrmGsD3mkTmIrisa/uIxU9d5y8YwRO4aZer/ikaMlcGzi/0tRvaUufGzY4G+bPT4ExfYKCD5kTCch2pQuqFo7Y+fkEBnKzcpSjSCaXVQRh0n6Dfli0HZii1gUjMvlvvcgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('1848fe15d6cb9f97258a7d0b8103395a')


#===========[ NOTE SAVER ]=======================
notes = {}

# Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(JoinEvent)#
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Ktik [Batara help] utk command :D\nKtik [Batara bye] utk Pergi :D\n\nCreator by Kris => \n{https://line.me/ti/p/~krissthea} \nor => \n{https://line.me/ti/p/~batara_dewa}')) 


@handler.add(MessageEvent, message=TextMessage)#
def handle_text_message(event):
    text = event.message.text

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get user_id
    gid = event.source.sender_id #get group_id
#=====[ LEAVE GROUP OR ROOM ]==========
    if text == 'Me' or text == 'me':
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Display name: ' + profile.display_name),
                    TextSendMessage(text='Status message: ' + profile.status_message)
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't use profile in group chat"))
            
    if text == 'aku' or text == 'Aku':
        if isinstance(event.source, SourceGroup):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Display name: ' + profile.display_name),
                    TextSendMessage(text='Status message: ' + profile.status_message)
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't use profile in group chat"))

    if text == 'Batara bye' or text == 'batara bye':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Bye..(-_-), Aim Pamit, Jangan Lupa Bahagia Ya..(-_-)...!!!'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Bye..(-_-), Aim Pamit, Jangan Lupa Bahagia Ya..(-_-)...!!!'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
                
    if text == 'pagi' or text == 'Pagi' or text == 'Met pagi' or text == 'Selamat pagi':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Pagi juga Kak, Met sarapan dan selamat beraktivitas ya..(-_-)...!!!'))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Pagi juga Kak, Met sarapan dan selamat beraktivitas ya..(-_-)...!!!'))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
                
    if text == 'Siang' or text == 'siang' or text == 'Met siang' or text == 'Selamat siang':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Siang juga Kak, Met makan siang dan selamat Istirahat ya..(-_-)...!!!'))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Siang juga Kak, Met makan siang dan selamat Istirahat ya..(-_-)...!!!'))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
                
    if text == 'Sore' or text == 'sore' or text == 'Met sore' or text == 'Selamat sore':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Sore juga Kak, Moga lelahmu menjadi masa depanmu yang cerah ya..(-_-)...!!!'))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Sore juga Kak, Moga lelahmu menjadi masa depanmu yang cerah ya..(-_-)...!!!'))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
                
    if text == 'Malam' or text == 'Mlm' or text == 'Met mlm' or text == 'Selamat mlm' or text == 'Selamat malam' or text == 'Met malam':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Malam juga Kak, Selamat Tidur kak, moga mimpi indah..(-_-)...!!!'))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='MAlam juga Kak, Selamat Tidur kak, moga mimpi indah..(-_-)...!!!'))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
                
    if text == 'KepFJS123fjs':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║☛FAMILY JAVANESE SMULE☚'
╠═════════════
║OWNER :
║KRIS
║
║FOUNDER:
║KRIS
║
║CO. FOUNDER:
║CINTA
║
║SEKRETARIS
║TIENA
║
║BENDAHARA:
║TRIA
║
║LEADER:
║HAJIR
║
║CO. LEADER:
║LORENZO
║
║ADMIN1:
║KWENI
║
║ADMIN2:
║ALYN
║
║ADMIN3:
║-
║
║ADMIN4:
║-
╠═════════════
║☛FAMILY JAVANESE SMULE☚
╚═════════════
'''))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║☛FAMILY JAVANESE SMULE☚'
╠═════════════
║OWNER :
║KRIS
║
║FOUNDER:
║KRIS
║
║CO. FOUNDER:
║CINTA
║
║SEKRETARIS
║TIENA
║
║BENDAHARA:
║TRIA
║
║LEADER:
║HAJIR
║
║CO. LEADER:
║LORENZO
║
║ADMIN1:
║KWENI
║
║ADMIN2:
║ALYN
║
║ADMIN3:
║-
║
║ADMIN4:
║-
╠═════════════
║☛FAMILY JAVANESE SMULE☚
╚═════════════
'''))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
                
    if text == 'Bigsticker123fjs':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║☛Big Sticker☚'
╠═════════════
║makasih
║helo/halo
║hai
║sabar
║wkwk
║hihi
║siap
║ok/oke
║malam/mlm
║knp/kenapa
║tikung
║waw/wow
║hhh
║sun/sun dong
║kiss
║haha
║marah/ngambek
║sst/diam
║sepi
║gendeng/koplak woy
║otw/pergi
║bye
║joget/joged
║goyang/goyang bro
║wasyik/goyang bool
║cipok
║kojom.mojok
║tipok
║pentung
║tabok
║galau/sedih/nangis
╚═════════════
'''))
            #line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='''
╔═════════════
║☛Big Sticker☚'
╠═════════════
║makasih
║helo/halo
║hai
║sabar
║wkwk
║hihi
║siap
║ok/oke
║malam/mlm
║knp/kenapa
║tikung
║waw/wow
║hhh
║sun/sun dong
║kiss
║haha
║marah/ngambek
║sst/diam
║sepi
║gendeng/koplak woy
║otw/pergi
║bye
║joget/joged
║goyang/goyang bro
║wasyik/goyang bool
║cipok
║kojom.mojok
║tipok
║pentung
║tabok
║galau/sedih/nangis
╚═════════════
'''))
            #line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
#=====[ TEMPLATE MESSAGE ]=============
    elif "Idline: " in event.message.text:
        skss = event.message.text.replace('Idline: ', '')
        sasa = "http://line.me/R/ti/p/~" + skss
        text_message = TextSendMessage(text=sasa)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "Apakah " in event.message.text:
        quo = ('Iya','Tidak','Gak tau','Bisa jadi','Mungkin iya','Mungkin tidak')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif (text == 'Bot') or (text == 'bot'):
        message = TextSendMessage(text='Aqu bukan bot..!!! Kebotan Lho..!!!')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Tes') or (text == 'tes') or (text == 'Test') or (text == 'test'):
        message = TextSendMessage(text='Testing Satu Tetes Bunting..Lol..(-_-)')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Bah') or (text == 'bah'):
        message = TextSendMessage(text='Lul')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Nah') or (text == 'nah'):
        message = TextSendMessage(text='Kan')
        line_bot_api.reply_message(event.reply_token, message)
#===========================================================
    elif text == 'Batara help':#template
        buttons_template = TemplateSendMessage(
            alt_text='Kris',
            template=ButtonsTemplate(
                title='[ FAMILY JAVANESE SMULE ]',
                text= 'Cyber Army Bot => Owner : Kris',
                actions=[
                    MessageTemplateAction(
                        label='FJS',
                        text='Fjs123fjs'
                    ),
                    MessageTemplateAction(
                        label='Big Sticker',
                        text='Bigsticker123fjs'
                    ),
                    MessageTemplateAction(
                        label='Kepengurusan FJS',
                        text='KepFJS123fjs'
                    ),
                    MessageTemplateAction(
                        label='Owner Bot',
                        text='OwnerCyberArmyBot'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
        
    elif text == 'Fjs123fjs':#template
        buttons_template = TemplateSendMessage(
            alt_text='Kris',
            template=ButtonsTemplate(
                title='[ FAMILY JAVANESE SMULE ]',
                text= 'Klik pilihan colum dibawah',
                actions=[
                    MessageTemplateAction(
                        label='List FJS',
                        text='Fjs123fjs123'
                    ),
                    MessageTemplateAction(
                        label='Rules FJS',
                        text='Rulesfjs123fjs'
                    ),
                    MessageTemplateAction(
                        label='Logo/Cover FJS',
                        text='Logofjs123fjs'
                    ),
                    MessageTemplateAction(
                        label='Struktur FJS',
                        text='StrukturKepengurusanFJS'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif text == 'Fjs123fjs123':#template
        buttons_template = TemplateSendMessage(
            alt_text='Kris',
            template=ButtonsTemplate(
                title='[ FAMILY JAVANESE SMULE ]',
                text= 'Klik pilihan colum dibawah',
                actions=[
                    MessageTemplateAction(
                        label='FJS 1',
                        text='Kepengurusanfjs123fjs'
                    ),
                    MessageTemplateAction(
                        label='FJS 2',
                        text='Kepengurusanfjs123fjs2'
                    ),
                    MessageTemplateAction(
                        label='FJS 3',
                        text='Kepengurusanfjs123fjs3'
                    ),
                    MessageTemplateAction(
                        label='Angota FJS',
                        text='Anggotafjs123fjs'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
#=====[ CAROUSEL MESSAGE ]==========
    elif text == 'Kepengurusanfjs123fjs':#carousel
        message = TemplateSendMessage(
            alt_text='Krisna',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='Own/Founder FJS',
                        text='Kris',
                        actions=[
                            URITemplateAction(
                                label='>Kris<',
                                uri='https://line.me/ti/p/~batara_dewa'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Co. Founder FJS',
                        text='Cinta',
                        actions=[
                            URITemplateAction(
                                label='>Cinta<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Sekretaris FJS',
                        text='Tiena',
                        actions=[
                            URITemplateAction(
                                label='>Tiena<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Bendahara FJS',
                        text='Tria',
                        actions=[
                            URITemplateAction(
                                label='>Tria<',
                                uri='https://line.me/ti/p/~triatienz'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'Kepengurusanfjs123fjs2':#carousel
        message = TemplateSendMessage(
            alt_text='Krisna',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='Leader FJS',
                        text='Hajir',
                        actions=[
                            URITemplateAction(
                                label='>Hajir<',
                                uri='https://line.me/ti/p/~hajirlove'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Co. Leader FJS',
                        text='Lorenzo',
                        actions=[
                            URITemplateAction(
                                label='>Lorenzo<',
                                uri='https://line.me/ti/p/~kriansby'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Admin1 FJS',
                        text='Kweni',
                        actions=[
                            URITemplateAction(
                                label='>Kweni<',
                                uri='https://line.me/ti/p/~ulinnik'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Admin2 FJS',
                        text='Alyn',
                        actions=[
                            URITemplateAction(
                                label='>Alyn<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'Kepengurusanfjs123fjs3':#carousel
        message = TemplateSendMessage(
            alt_text='Krisna',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='Admin3 FJS',
                        text='Kosong',
                        actions=[
                            URITemplateAction(
                                label='>Kosong<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Admin4 FJS',
                        text='Kosong',
                        actions=[
                            URITemplateAction(
                                label='>Kosong<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'Anggotafjs123fjs':#carousel
        message = TemplateSendMessage(
            alt_text='Krisna',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='Anggota FJS',
                        text='Uchil',
                        actions=[
                            URITemplateAction(
                                label='>Uchil<',
                                uri='https://line.me/ti/p/~roni161196'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Anggota FJS',
                        text='Ary',
                        actions=[
                            URITemplateAction(
                                label='>Ary<',
                                uri='https://line.me/ti/p/~ari_skatepunk'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Anggota FJS',
                        text='Kosong',
                        actions=[
                            URITemplateAction(
                                label='>Kosong<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Anggota FJS',
                        text='Kosong',
                        actions=[
                            URITemplateAction(
                                label='>Kosong<',
                                uri='https://line.me/ti/p/~'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=====[ FLEX MESSAGE ]==========
        
    elif (text == 'makasih') or (text == 'Makasih'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/--gxZM-3_8xk/WFasL3Y55gI/AAAAAAAFd14/tu2DK-ITFfcOjZHAnq3ynEyQR7TEAStRQCLcB/s1600/AW352983_07.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'helo') or (text == 'Helo') or (text == 'halo') or (text == 'Halo'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://thumbs.gfycat.com/AdeptIdioticIchidna-max-1mb.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'hai') or (text == 'Hai'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-TS3IrlyRK18/WE_QlVbh1KI/AAAAAAAFMuM/mcEPg4f4MV4KJgfNWc-IMb8MmU4IpRk6ACLcB/s1600/AW293929_05.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'sabar') or (text == 'Sabar'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-d2s2TZWQL3M/WRxIlxH2wmI/AAAAAAAHlYE/vmDRTrJR3C461hEsMFZL28qRCglREM7bQCLcB/s1600/AW429484_04.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'wkwk') or (text == 'Wkwk'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-OVigsYHr2n0/WymMu2gJipI/AAAAAAAgaIo/rW6lhc_8y1k7La3QYpq67YOORu64jyuxgCLcBGAs/s1600/AW1238316_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'hihi') or (text == 'Hihi'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-wk4iPzjOYoQ/WFvyR-NDP0I/AAAAAAAFLwo/Yuh40_TQLP0cDCHwtqeN5VmNfGN0LnxQgCLcB/s1600/AW355622_04.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'siap') or (text == 'Siap'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-ipl1HRIeSOM/WRMvRhMGU1I/AAAAAAAPEH0/ea9RXLFj1sQWKL-Zs0YgthUqJGGQo3QwgCLcB/s1600/AW424038_00.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'ok') or (text == 'oke') or (text == 'Ok') or (text == 'Oke'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.pinimg.com/originals/0e/91/e3/0e91e3422c0c765ce74601ccecace5cf.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'ga') or (text == 'gak') or (text == 'gamau') or (text == 'Gamau') or (text == 'Ga') or (text == 'Gak'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bott',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/8683557/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Malam') or (text == 'Met mlm') or (text == 'Met malam') or (text == 'Selamat malam') or (text == 'Mlm'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bott',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.pinimg.com/originals/cd/13/79/cd1379986667309c892717c2c0017b90.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Knp') or (text == 'knp') or (text == 'Kenapa') or (text == 'Apa') or (text == '?'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-qRlbAaTzSsI/WE_QldvuKPI/AAAAAAAFMuI/0tGUHoqtvgYOH97ftYe4WlKDtLuaK7V_ACLcB/s1600/AW293929_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Krisna') or (text == 'Tikung') or (text == 'Manis'):
        message = TemplateSendMessage(
            alt_text='Krisna',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-yDkq-cfuZJw/W7Nhypg8WAI/AAAAAAAAA4k/mb76_dr8Veo9ryWnBS70dF5TT5Fg7C3HQCJoC/w795-h801-n-rw/807838.jpg',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#    elif (text == 'Krisna') or (text == 'Tikung') or (text == 'Manis'):
#        message = ImagemapSendMessage(
#            base_url='https://lh3.googleusercontent.com/-yDkq-cfuZJw/W7Nhypg8WAI/AAAAAAAAA4k/mb76_dr8Veo9ryWnBS70dF5TT5Fg7C3HQCJoC/w795-h801-n-rw/807838.jpg',
#            alt_text='Kris',
#            base_size=BaseSize(height=1040, width=1040),
#            actions=[
#                URIImagemapAction(
#                    link_uri='https://line.me/ti/p/~batara_dewa',
#                    area=ImagemapArea(
#                        x=0, y=0, width=1040, height=1040
#                    )
#                ),
#                MessageImagemapAction(
#                    text='Kris Manis',
#                    area=ImagemapArea(
#                        x=520, y=0, width=520, height=1040
#                    )
#                )
#            ]
#        )
#        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'waw') or (text == 'Waw') or (text == 'wow') or (text == 'Wow'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://1.bp.blogspot.com/--PyKKdhyjbo/WMlfB-9gfUI/AAAAAAAOBaM/1XAFQtTAxyoQTxFGjm4UOCzVckJq3GiTgCLcB/s1600/AW392366_01.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'hhh') or (text == 'Hhh'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-OcsIXDFKcnA/WRxI6NIil1I/AAAAAAAHldE/BHP9ijh88eYZROMWHdPcHH3-kPWXiCd4QCLcB/s1600/AW429514_00.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Sun') or (text == 'Sun dong'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-GpEExd0b9-A/WyheSQrPFPI/AAAAAAANJXM/M5YBhnT_vcofTJZ9Xw2fX2lQrRbFmKV7wCLcBGAs/s1600/AW1238614_07.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Kiss') or (text == 'kiss'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-J9W5u3_TxbQ/WmS8qVYvGCI/AAAAAAAA1iE/LgxLU0g3WZUalKIdjNS-L3DNbocSiZDXwCJoC/w800-h800/0DjyylSLOtvLxegotklwyVCg02N.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Haha') or (text == 'haha'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://s.kaskus.id/images/2018/07/04/2216544_20180704015520.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Marah') or (text == 'Ngambek'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-W5WaLvaUoyU/WMQX7uAyHpI/AAAAAAAN_M0/xHgXrqlJwmczxIbB3R73_13vXpgnDAPkACLcB/s1600/AW391031_03.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Sst') or (text == 'Diam'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-zMbjVh62jpk/WS2EH_K-j2I/AAAAAAAH0ks/7M3o_hMbfk8TDAiR9stehYVH6DjTOBr4QCLcB/s1600/AW438063_04.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Sepi') or (text == 'sepi'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-JwgXAXNVG2w/WykhtxpIJqI/AAAAAAAgYNY/W_uh6gn5uoYrx0aA6Q0GvQbPsfzLMTtYgCLcBGAs/s1600/AW1237931_00.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Gendeng') or (text == 'Koplak woy') or (text == 'Somplak woy'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-USupKtE-__s/WM1eaBaDuII/AAAAAAAOIV8/voYdrf_YWUEqj2boITcjGY5dwgrB8283ACLcB/s1600/AW395051_03.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Kabur') or (text == 'kabur') or (text == 'Lari'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-qqBCTr7ZpI4/WM1eau1_q1I/AAAAAAAOIWE/Fa5C3zL28esKZmN6vsRPcBHFmVgRs3FIgCLcB/s1600/AW395051_07.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Otw') or (text == 'Pergi'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-MbJFVYtQ4n0/WM1eaywyfjI/AAAAAAAOIWI/y0DTio3zSAoaXbt9QsgH4L_G7XxaA0jYQCLcB/s1600/AW395051_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Bye') or (text == 'bye'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.pinimg.com/originals/74/f7/31/74f73145230b0a5e54a8e579d27ca1a7.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Joged') or (text == 'Joget') or (text == 'Joged bro'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-Cgdf-zL8OF4/WymMaaO2QBI/AAAAAAAgaGo/hIVovpbQTvA8xFsm9kA17Js6A5_1bIGLQCLcBGAs/s1600/AW1238310_01.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Goyang') or (text == 'Goyang bro'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-buFHNCEXtdI/WetfJvdCCWI/AAAAAAALsJE/p2xMIVFuu6cJRmFkf9ZomligmbClPXLtwCLcBGAs/s1600/AW586900_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Wasyik') or (text == 'Goyang bool'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-YkMj7-lrhkY/WetfJHV4nLI/AAAAAAALsJA/_5x8w9hw9kQrSsUS_oz8VigjZmTawSlAACLcBGAs/s1600/AW586900_05.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Kojom') or (text == 'Mojok'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-RCN2F5_sW8s/WETV3aiPh8I/AAAAAAALxnM/UnmNbtuVCkEZ_bbqlq2t5mHf49EmgvndwCLcB/s1600/AW324437_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'cipok') or (text == 'Cipok'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-yoMHiOR17Bg/WETVuzbvyBI/AAAAAAALxm4/od4pFuukfH40cuMn2c08wqtkGOX3HuNSACLcB/s1600/AW324437_01.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Tipok') or (text == 'tipok'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-e3cFsWiKLdA/WTAH1EByiRI/AAAAAAAIMvM/dUvAXujr4cIwsjn5DPEvRfCYZVp3DWvSQCLcB/s1600/AW439317_13.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Pentung') or (text == 'pentung'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://1.bp.blogspot.com/-uqvJKBeQORI/WD6hrAEpeOI/AAAAAAALo9g/6QmAHA53bI039Gv1Brt5RA-E0av-tueJACLcB/s1600/AS002044_01.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Tabok') or (text == 'tabok'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-CXej0VEJkps/WDv1XSwipPI/AAAAAAALlNU/UjrTOos8KF86vkw05SE25bUkAQc86b2pwCLcB/s1600/AS001630_08.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Galau') or (text == 'galau'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-oB7VOXVL0FI/WUMi8gN7FdI/AAAAAAAPwaM/GO0TjY65hvEP5GsBPELtoTJJ3WFm6vGDgCLcBGAs/s1600/AW448914_06.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Goyang brow') or (text == 'goyang brow'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://2.bp.blogspot.com/-3i31UNhuF-Q/Wkhcq7CdO1I/AAAAAAAQgw4/RHaLNrmlw1MhNRD9lmf1sJIS66eLa53wgCLcBGAs/s1600/AW709937_05.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Asem') or (text == 'Aseem'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-Yc0J49r3g0Q/WEjmHvYf8vI/AAAAAAAL54w/XKP9sFitJGshWkEpS8kWQ0Bxay0vT3qUgCLcB/s1600/AW337107_08.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Rasakno') or (text == 'Puas'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://3.bp.blogspot.com/-VE3Pt6nU6qs/WymMsufN77I/AAAAAAAgaIY/49zgf3ECVGY0cX048uaI6OhrZaXRZi-owCLcBGAs/s1600/AW1238316_03.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Udud Brow') or (text == 'Udud bro') or (text == 'Sambil udud brow'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-qp6-x_MJOTo/W7duhg5hl3I/AAAAAAAABBo/chEKABTP3Js-CfVBirxusHndsySBkVToQCJoC/w150-h150-n-rw/krisukuran%2Bkecil.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Terlena') or (text == 'Terpana') or (text == 'Wasyik'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-52tG0dvdonQ/W7f-FzffIsI/AAAAAAAABCo/RgyVkr4FEoMEipW7neM4gv3J_62jvPKKACJoC/w105-h105-n-rw/krissssssssssssssssss.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Mantap') or (text == 'Tikung') or (text == 'Nikung'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-5LPIi-A0A4w/W7gAYivP9TI/AAAAAAAABDo/txLEFe8KYwwsQrTfbT8V-rEHH-NtvdRbQCJoC/w135-h135-n-rw/krkrkrrrrrrrrrrrrrrrrrrr.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Mimi uu brow') or (text == 'Mimi uu bro') or (text == 'Mimi uu'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-Dy0fzicTJRA/W7gDbez9UxI/AAAAAAAABEc/l8csTiCUCWMAktPPb7VxQaT-M5VSP9a5gCJoC/w87-h87-n-rw/bromadddddddddddddd.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Sambil kopi brow') or (text == 'Sambil kopi bro') or (text == 'Kopi brow'):
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://lh3.googleusercontent.com/-aube9cV9EM0/W7gEx95GzkI/AAAAAAAABFY/NGHTz8JWGW0TwiQmivNZfMPStX1crW0iACJoC/w795-h773-n-rw/979086.jpg',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#==================================================
    elif text == 'Oh' or text == 'Ooh':
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-sQ-7Vzo76f4/WyhdsXue8qI/AAAAAAANJPk/VYxa7abxAWMVjhNxcURfVKta5NVc9qJNwCLcBGAs/s1600/AW1238589_05.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'Kemeng' or text == 'kemeng':
        message = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://4.bp.blogspot.com/-3MXW9EujSPs/W3gDYSTMU1I/AAAAAAAZBCM/VAaceV7Xc8IOcTEpkkeS-hAs66PKVFtSgCLcBGAs/s1600/AW1575124_01.gif',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#======================================================================
    elif text == 'Batara naga1' or text == 'Naga1':
        message1 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510674/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        message2 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510675/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        message3 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510676/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        message4 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510677/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        #line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.reply_message(
                event.reply_token, [
                    message1,
                    message2,
                    message3,
                    message4
                ]
            )
    elif text == 'Batara naga2' or text == 'Naga2':
        message5 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510678/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        message6 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510679/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        message7 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510680/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        message8 = TemplateSendMessage(
            alt_text='Cyber Army Bot',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16510681/ANDROID/sticker.png',
                        action=URIAction(uri='https://line.me/ti/p/~batara_dewa')
                    )
                ]
            )
        )
        #line_bot_api.reply_message(event.reply_token, message)
        line_bot_api.reply_message(
                event.reply_token, [
                    message5,
                    message6,
                    message7,
                    message8
                ]
            )
#=====================================================================================================================
    elif text == 'Apakah':
        #rep = text.replace("Apakah ","")
        txt = ["Ya","Tidak","Bisa Jadi","Mungkin","Hoax"]
        line_bot_api.reply_message(
            event.reply_token,[
            TextSendMessage(text=random.choice(txt))
            ]
        )
            
    elif text == 'Carivideo':
        separate = text.split(" ")
        search = text.replace(separate[0] + " ","")
        params = {"search_query": search}
        source = requests.get("https://www.youtube.com/results", params = params)
        bsoup = BeautifulSoup(source.content, "html5lib")
        ret_ = "[ RESULT ]"
        datas = []
        num = 0
        for data in soup.select(".yt-lockup-title > a[title]"):
            if "&lists" not in data["href"]:
                datas.append(data)
        num += 1
        for data in datas:
            ret_ += "\n\n{}. Judul: {}".format(num, data["title"])
            ret_ += "\n    Link: https://www.youtube.com{}".format(data["href"])
        ret_ += "\n\n[ TOTAL: {} VIDEO ]".format(len(datas))
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=ret_))
                
    elif text == 'Carigambar':
        separate = text.split(" ")
        search = text.replace(separate[0] + " ","")
        r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
        data = r.text
        data = json.loads(data)

        if data["result"] != []:
            items = data["result"]
            path = random.choice(items)
            a = items.index(path)
            b = len(items)

        image_message = ImageSendMessage(
            original_content_url=path,
            preview_image_url=path
        )

        line_bot_api.reply_message(
            event.reply_token,
            image_message
        )
#======================================================================================================================
    elif text == 'confirm':
        confirm_template = ConfirmTemplate(text='Do it?', actions=[
            MessageAction(label='Yes', text='Yes!'),
            MessageAction(label='No', text='No!'),
        ])
        template_message = TemplateSendMessage(
            alt_text='Confirm alt text', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif text == 'buttons':
        buttons_template = ButtonsTemplate(
            title='My buttons sample', text='Hello, my buttons', actions=[
                URIAction(label='Go to line.me', uri='https://line.me'),
                PostbackAction(label='ping', data='ping'),
                PostbackAction(label='ping with text', data='ping', text='ping'),
                MessageAction(label='Translate Rice', text='米')
            ])
        template_message = TemplateSendMessage(
            alt_text='Buttons alt text', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
#======================================================================================================================
    elif text == 'StrukturKepengurusanFJS':#template
        buttons_template = TemplateSendMessage(
            alt_text='FJS',
            template=ButtonsTemplate(
                title='[ FAMILY JAVANESE SMULE ]',
                text= 'Klik pilihan colum dibawah',
                actions=[
                    MessageTemplateAction(
                        label='Owner FJS',
                        text='StrukturOwnerFJS'
                    ),
                    MessageTemplateAction(
                        label='Founder FJS',
                        text='StrukturFounderFJS'
                    ),
                    MessageTemplateAction(
                        label='Co.Founder FJS',
                        text='StrukturCo.FounderFJS'
                    ),
                    MessageTemplateAction(
                        label='Next FJS',
                        text='NextStrukturFJS'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif text == 'NextStrukturFJS':#template
        buttons_template = TemplateSendMessage(
            alt_text='FJS',
            template=ButtonsTemplate(
                title='[ FAMILY JAVANESE SMULE ]',
                text= 'Klik pilihan colum dibawah',
                actions=[
                    MessageTemplateAction(
                        label='Sekretaris FJS',
                        text='StrukturSekretarisFJS'
                    ),
                    MessageTemplateAction(
                        label='Bendahara FJS',
                        text='StrukturBendaharaFJS'
                    ),
                    MessageTemplateAction(
                        label='Leader FJS',
                        text='StrukturLeaderFJS'
                    ),
                    MessageTemplateAction(
                        label='Next FJS',
                        text='NextStrukturFJS2'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif text == 'NextStrukturFJS2':#template
        buttons_template = TemplateSendMessage(
            alt_text='FJS',
            template=ButtonsTemplate(
                title='[ FAMILY JAVANESE SMULE ]',
                text= 'Klik pilihan colum dibawah',
                actions=[
                    MessageTemplateAction(
                        label='Co.Leader FJS',
                        text='StrukturCo.LeaderFJS'
                    ),
                    MessageTemplateAction(
                        label='Admin1 FJS',
                        text='StrukturAdmin1FJS'
                    ),
                    MessageTemplateAction(
                        label='Admin2 FJS',
                        text='StrukturAdmin2FJS'
                    ),
                    MessageTemplateAction(
                        label='Next FJS',
                        text='NextStrukturFJS3'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
#================================================================================= 
    elif text == 'OwnerCyberArmyBot':
        confirm_template = ConfirmTemplate(text='Owner Cyber Army Bot', actions=[
            MessageAction(label='Kris1', text='Kris!1!'),
            MessageAction(label='Kris2', text='Kris!2!'),
        ])
        template_message = TemplateSendMessage(
            alt_text='Owner Kris', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)
#=======================================================================================================================
    elif text == 'Kris!1!':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh3.googleusercontent.com/-MEw1WMfTu7g/W5ddlho3_VI/AAAAAAAAAog/--xncjxwxZIHEfjEnfRedHIYdHL2jPMpACJoC/w795-h795-n-rw/q%2Bcyber.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://line.me/ti/p/~krissthea', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Kris', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='Owner: Kris', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Order',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Self Bot, Bot Protect, Anti JS',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Edit',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Cover, Logo, Logo Video",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Kris', uri="https://line.me/ti/p/~krissthea")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak1 kris", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
        
    elif text == 'Kris!2!':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh3.googleusercontent.com/-yDkq-cfuZJw/W7Nhypg8WAI/AAAAAAAAA40/nmlcboW7bAwE4GahGtRm8Z_tPxmEa3uZgCJoC/w795-h801-n-rw/807838.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://line.me/ti/p/~batara_dewa', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Kris', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='Owner: Kris', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Order',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Self Bot, Bot Protect, Anti JS',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Edit',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Cover, Logo, Logo Video",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Kris', uri="https://line.me/ti/p/~batara_dewa")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak2 kris", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
#=====================================[owner]======================================
    elif text == 'StrukturOwnerFJS':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh3.googleusercontent.com/-fdANmMKC_mI/W7aWCaVspwI/AAAAAAAAA_I/_rwMZ4cfWaIra7BpStMpJfjlkicwO_aTQCJoC/w795-h692-n-rw/697672.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://lh3.googleusercontent.com/-fdANmMKC_mI/W7aWCaVspwI/AAAAAAAAA_I/_rwMZ4cfWaIra7BpStMpJfjlkicwO_aTQCJoC/w795-h692-n-rw/697672.jpg', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Kris', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='FJS', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Name',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Kris',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Job',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Owner FJS",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Contact Kris', uri="https://line.me/ti/p/~krissthea")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak Owner", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
#=====================================[Founder]======================================
    elif text == 'StrukturFounderFJS':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh3.googleusercontent.com/-yDkq-cfuZJw/W7Nhypg8WAI/AAAAAAAAA40/nmlcboW7bAwE4GahGtRm8Z_tPxmEa3uZgCJoC/w795-h801-n-rw/807838.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://lh3.googleusercontent.com/-yDkq-cfuZJw/W7Nhypg8WAI/AAAAAAAAA40/nmlcboW7bAwE4GahGtRm8Z_tPxmEa3uZgCJoC/w795-h801-n-rw/807838.jpg', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Kris', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='FJS', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Name',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Kris',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Job',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Founder FJS",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Contact Kris', uri="https://line.me/ti/p/~batara_dewa")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak Founder", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )    
#=====================================[Co.Founder]======================================
    elif text == 'StrukturCo.FounderFJS':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh3.googleusercontent.com/-GX30aymSTMY/W7aLcEb8RgI/AAAAAAAAA6Y/C_SBV8ajIIgaXoLniQgBG_3IOP7MhukagCJoC/w795-h914-n-rw/cinta.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://lh3.googleusercontent.com/-GX30aymSTMY/W7aLcEb8RgI/AAAAAAAAA6Y/C_SBV8ajIIgaXoLniQgBG_3IOP7MhukagCJoC/w795-h914-n-rw/cinta.jpg', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Cinta', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='FJS', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Name',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Cinta',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Job',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Co.Founder FJS",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Contact Cinta', uri="https://line.me/ti/p/~atyq789")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak Co.Founder", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )  
#=====================================[Sekretaris]======================================
    elif text == 'StrukturSekretarisFJS':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh3.googleusercontent.com/-vg_ZIdVtc_8/W7aMjdpjAOI/AAAAAAAAA7A/-lvMpmjzUXM5C_Gb5U8ATLpYseUGNeY2QCJoC/w795-h795-n-rw/tiena.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://lh3.googleusercontent.com/-vg_ZIdVtc_8/W7aMjdpjAOI/AAAAAAAAA7A/-lvMpmjzUXM5C_Gb5U8ATLpYseUGNeY2QCJoC/w795-h795-n-rw/tiena.jpg', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Tiena', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='FJS', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Name',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Tiena',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Job',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Sekretaris FJS",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Contact Tiena', uri="https://line.me/ti/p/~")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak Sekretaris", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )  
#=====================================[Bendahara]======================================
    elif text == 'StrukturBendaharaFJS':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh3.googleusercontent.com/-p35k719YHKg/W7aNVo6PAxI/AAAAAAAAA7g/T7ccf0UlImknMT5aj5H_HVxQKDaFfZ_NQCL0BGAs/w795-d-h1061-n-rw/tria.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://lh3.googleusercontent.com/-p35k719YHKg/W7aNVo6PAxI/AAAAAAAAA7g/T7ccf0UlImknMT5aj5H_HVxQKDaFfZ_NQCL0BGAs/w795-d-h1061-n-rw/tria.jpg', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Tria', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='FJS', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Name',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Tria',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Job',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Bendahara FJS",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Contact Tria', uri="https://line.me/ti/p/~triatienz")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak Bendahara", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )  
#=====================================[Leader]======================================
    elif text == 'StrukturLeaderFJS':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh3.googleusercontent.com/-NpkCPATtJPs/W7aOA7f13OI/AAAAAAAAA8g/JZw-VgEjr4MQnmQMqFLzeHtv9-o6qFEywCJoC/w795-h690-n-rw/hajir.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://lh3.googleusercontent.com/-NpkCPATtJPs/W7aOA7f13OI/AAAAAAAAA8g/JZw-VgEjr4MQnmQMqFLzeHtv9-o6qFEywCJoC/w795-h690-n-rw/hajir.jpg', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Hajir', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='FJS', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Name',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Hajir',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Job',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Leader FJS",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Contact Hajir', uri="https://line.me/ti/p/~hajirlove")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak Leader", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        ) 
#=====================================[Co.Leader]======================================
    elif text == 'StrukturCo.LeaderFJS':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh3.googleusercontent.com/-yR0evhUxE9k/W7aO6LQ6rYI/AAAAAAAAA9M/MnsRmwES7t0CIKsHi0O55coX6H3IRtlpgCJoC/w795-h795-n-rw/bromad.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://lh3.googleusercontent.com/-yR0evhUxE9k/W7aO6LQ6rYI/AAAAAAAAA9M/MnsRmwES7t0CIKsHi0O55coX6H3IRtlpgCJoC/w795-h795-n-rw/bromad.jpg', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Leonardo', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='FJS', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Name',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Leonardo',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Job',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Co.Leader FJS",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Contact Leonardo', uri="https://line.me/ti/p/~kriansby")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak Co.Leader", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        ) 
#=====================================[Admin1]======================================
    elif text == 'StrukturAdmin1FJS':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh3.googleusercontent.com/-4PjSWA-Rk4M/W7aTSTpLXuI/AAAAAAAAA-Y/EIJeXzs4JaUVlizCXwRjmvwooAkfnqn-QCJoC/w398-h530-n-rw/kweni.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://lh3.googleusercontent.com/-4PjSWA-Rk4M/W7aTSTpLXuI/AAAAAAAAA-Y/EIJeXzs4JaUVlizCXwRjmvwooAkfnqn-QCJoC/w398-h530-n-rw/kweni.jpg', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Kweni', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='FJS', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Name',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Kweni',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Job',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Admin1 FJS",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Contact Kweni', uri="https://line.me/ti/p/~ulinnik")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak Admin1", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        ) 
#=====================================[Admin2]======================================
    elif text == 'StrukturAdmin2FJS':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh3.googleusercontent.com/-hMd__-LU2l4/W7aTSXLPMlI/AAAAAAAAA-Y/FOoFDWNWk18aYOTQrT6qEsjLNQ5oAR1KQCJoC/w398-h530-n-rw/alyn.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='https://lh3.googleusercontent.com/-hMd__-LU2l4/W7aTSXLPMlI/AAAAAAAAA-Y/FOoFDWNWk18aYOTQrT6qEsjLNQ5oAR1KQCJoC/w398-h530-n-rw/alyn.jpg', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Alyn', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            IconComponent(size='sm', url='https://www.thespaatlittleriver.com/wp-content/uploads/2013/07/gold-star.jpg'),
                            TextComponent(text='FJS', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Name',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Alyn',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Job',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="Admin2 FJS",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Contact Alyn', uri="https://line.me/ti/p/~alyndybala")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="Kontak Admin2", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        ) 
#===============================================================================================
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
