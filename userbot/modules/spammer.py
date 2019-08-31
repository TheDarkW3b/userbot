# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio
from asyncio import wait

from userbot import BOTLOG_CHATID, BOTLOG, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.spam")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])

        await wait(
            [e.respond(spam_message) for i in range(counter)]
            )

        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#SPAM \n\n"
                "Spam was executed successfully"
                )
        
@register(outgoing=True, pattern="^.tspam")
async def tmeme(e):
    tspam = str(e.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()

@register(outgoing=True, pattern="^.bigspam")
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#BIGSPAM \n\n"
                "Bigspam was executed successfully"
                )

@register(outgoing=True, pattern="^.gangsta$")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("EVERyBOdy")
        await asyncio.sleep(0.3)
        await e.edit("iZ")
        await asyncio.sleep(0.2)
        await e.edit("GangSTur")
        await asyncio.sleep(0.5)
        await e.edit("UNtIL ")
        await asyncio.sleep(0.2)
        await e.edit("I")
        await asyncio.sleep(0.3)
        await e.edit("ArRivE")
        await asyncio.sleep(0.3)
        await e.edit("🔥")
        await asyncio.sleep(0.3)
        await e.edit("EVERyBOdy iZ GangSTur UNtIL I ArRivE 🔥")

        
@register(outgoing=True, pattern="^.nikal$")
async def whoizme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("NikAl")
        await asyncio.sleep(0.3)
        await e.edit("lAwDe")
        await asyncio.sleep(0.2)
        await e.edit("PehLi")
        await asyncio.sleep(0.5)
        await e.edit("FuRsaT")
        await asyncio.sleep(0.2)
        await e.edit("Me")
        await asyncio.sleep(0.3)
        await e.edit("NikAl")
        await asyncio.sleep(0.3)
        await e.edit("<--")
        await asyncio.sleep(0.3)
        await e.edit("NikAl lAwDe PehLi FuRsaT Me NikAL <--")


@register(outgoing=True, pattern="^.repeat")
async def repeat(e):
    message = e.text[10:]
    count = int(e.text[8:10])
    repmessage = message * count
    await e.respond(repmessage)
    await e.delete()
    
    
@register(outgoing=True, pattern="^.repeats")
async def repeats(e):
    message = e.text[10:]
    count = int(e.text[8:10])
    repmessage = message * count
    await wait([e.respond(repmessage)for i in range(count)])
    await e.delete()

@register(outgoing=True, pattern="^.picspam")
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[0])
        link = str(text[2])
        if range(1, counter):
            await e.client.send_file(e.chat_id, link)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#PICSPAM \n\n"
                "PicSpam was executed successfully"
                )
            
@register(outgoing=True, pattern="^.delayspam")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        spamDelay = float(message[11:15])
        counter = int(message[15:19])
        spam_message = str(e.text[19:])
        from userbot.events import register
        for i in range(1, counter):
            await e.respond(spam_message)
            time.sleep(spamDelay)
        await e.delete()
        if BOTLOG:
            await e.client.send_message(
                BOTLOG_CHATID,
                "#DelaySPAM \n\n"
                "DelaySpam was executed successfully"
                )
            
            
            
CMD_HELP.update({
    "spam": ".tspam <text>\
\nUsage: Spam the text letter by letter.\
\n\n.spam <count> <text>\
\nUsage: Your regular spammer stuff :P\
\n\n.bigspam <count> <text>\
\nUsage: .spam on steroids !!\
\n\n.picspam <count> <link>\
\nUsage: As if text spam was not enough !!\
\n\n.delayspam <delay> <count> <text>\
\nUsage: .bigspam but slower.\
\n\n.gangsta\
\nUsage: Gives you Gengster Feeling, btw Spyder is real Gangsta.\
\n\n.nikal\
\nUsage: Prevents Lawda Lassun.\
\n\n\nNOTE : I am not responsible if you get banned for spamming!"
})
