"""Emoji

Available Commands:

.dark"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("dark"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 5)
    await event.edit("dark")
    animation_chars = [
            "അയ്യേ ഉളുപ്പ് ഉണ്ടോ നിനക്ക് ",
            "എന്ത് പ്രഹസനം ആണ് സജി ",
            "പോടാ കിളവ ",
            "വിട്ടുകളയണം ",
            "ഒന്നു നന്നായിക്കൂടെ",
            "എന്താ മോനുസേ ജാട ആണോ",
            "എന്താ മോളുസേ ജാടയാണോ",
            "വെല്ലുവിളികൾ ആകാം പക്ഷെ അതു നിന്നെക്കാൾ കൂടുതൽ ഓണം ഉണ്ടവനോട് ആകരുത്",
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %8 ])
