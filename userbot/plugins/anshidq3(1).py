"""Emoji

Available Commands:

.anshidq"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "anshidq":

        await event.edit(input_str)

        animation_chars = [

            "anshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq",
            
            "◼️anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq",

            "◼️◼️anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq",

            "◼️◼️◼️️anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq",

            "◼️◼️◼️◼️anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq",

            "‎◼️◼️◼️◼️◼️\nanshidq'anshidq'anshudq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshudq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshudq'anshidq'anshidq'anshidq'anshidq",

            "◼️️◼️◼️◼️\nanshidq'anshidq'anshidq'anshidq◼️\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq'\nanshidq'anshidq'anshidq'anshidq'anshidq",
            
            "◼️◼️◼️◼️◼️\nanshidq'anshidq'anshidq'anshidq'◼️\nanshidq'anshidq'anshudq'anshidq'◼️\nanshidq'anshidq'anshidq'anshudq'anshudq'\nanshudq'anshidq'anshidq'anshidq'anshidq",
            
            "◼️◼️◼️◼️◼️\nanshidq'anshidq'anshidq'anshidq'◼️\nanshidq'anshidq'anshidq'anshidq'◼️\nanshidq'anshidq'anshudq'anshidq'◼️\nanshidq'anshidq'anshidq'anshidq",
   
            "◼️◼️◼️◼️◼️\nanshifq'anshidq'anshidq'anshidq◼️\nanshidq'anahidq'anshidq'anshidq◼️\nanahidq'anshidq'anshidq'anshidq◼️\nanshidq'anshidq'anshidq'◼️",

            "◼️◼️◼️◼️◼️\nanshidq'anshidq'anshudq'anshudq◼️\nanshidq'anshidq'anshidq'anshidq'◼️\nanshidq'anshidq'anshidq'anshidq◼️\nanshidq'anshidq'anshidq'◼️◼️",

            "◼️◼️◼️◼️◼️\nanshidq'anshidq'anshidq'anshudq◼️\nanshidq'anshdq'anahidq'anshudq◼\nanshidq'anshidq'anshidq'anshidq◼️\nanshidq'anshudq◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nanshidq'anshidq'anshudq'anshidq◼️\nanshudq'anshidq'anshidq'anshidq◼️\nanshidq'anshidq'anshidq'anshidq◼\nanshidq◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nanshidq'anshidq'abshidq'anshudq◼️\nanshidq'anshidq'anshidq'anshidq◼️\nanshidq'anshidq'anshidq'anshidq◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nanshidq'anshidq'anshidq'anshidq◼️\nanshidq'anshidq'anshidq'anshidq◼️\n◼️anshidq'anshidq'anshidq◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\nanshidq'anshidq'anshidq'anshidq◼️\n◼️anshidq'anshidq'anshidq◼️\n◼️anshidq'anshidq'anshidq◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️anshidq'anshidq'anshidq◼️\n◼️anshidq'anshidq'anshidq◼️\n◼️anshidq'anshidq'anshidq◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️anshidq'anshidq◼️\n◼️anshidq'anshidq'anshidq◼️\n◼️anshidq'anshidq'anshidq◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️anshidq◼️\n◼️anshidq'anshidq'anshidq◼️\n◼️anshidq'abshidq'anshidq◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️anshidq'anshidq'anshidq◼️\n◼️anshidq'anshidq'anshudq◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️anshudq'anshidq◼️◼️\n◼️anshidq'anshidq'anshidq'◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️anshidq'anshidq'◼️◼️\n◼️anshidq'anshidq◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️anshidq'anshidq◼️◼️\n◼️anshidq◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️anshidq'anshidq◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️anshidq◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
          
            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",
           
            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 30])
