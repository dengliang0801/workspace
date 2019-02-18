#!/usr/bin/python

import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return u'Hi, 我是K歌之狂主人编写的个人助理机器人～ 主人现在休息中，不方便查看微信。如有急事，还请直接拨打主人手机：18613139686，谢谢啦！～'

itchat.auto_login(hotReload=True)
itchat.run()
