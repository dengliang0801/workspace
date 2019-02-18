#!/usr/bin/python
# -*- coding=utf-8 -*-
# wxRobot-v1 version: without groupchat/MPchat functions


import itchat, time, requests
from itchat.content import *

def reply_from_robot(msg):
    api = 'http://www.tuling123.com/openapi/api'
    req = {
        'userid': 'wxRobot',
        'key'   : '559eb94752194c4dbe8d120c02f09d44',
        'info'  : msg.text,
    }
    try:
        rsp = requests.post(api, req).json()
        return rsp.get('text')
    except:
        return '抱歉，我没理解您的意思，烦请再说一次～'

def reply_from_thank(msg):
    try:
        rtn = msg.download(msg.fileName)
        return '谢谢，我已接收您的信息，稍后我会处理～'
    except:
        return '抱歉，没能收到您的信息，请重发一次吧～'

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_class_reply(msg):
    print('[%s:%s]' % (msg.type, msg.text))
    return reply_from_robot(msg)

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def file_class_reply(msg):
    print('[%s:%s]' % (msg.type, msg.fileName))
    return reply_from_thank(msg) 

itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.run()
