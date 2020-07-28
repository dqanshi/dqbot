"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@borg.on(admin_cmd(outgoing=True, pattern="alme$"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("┈┈┈┈╱▔▔▔▔▔▔╲┈╭━━━╮┈┈┈ \n"
                     "┈┈┈▕┈╭━╮╭━╮┈▏┃BOO…┃┈┈┈ \n"
                     "┈┈┈▕┈┃╭╯╰╮┃┈▏╰┳━━╯┈┈┈ \n"
                     "┈┈┈▕┈╰╯╭╮╰╯┈▏┈┃┈┈┈┈┈┈ \n"
                     "┈┈┈▕┈┈┈┃┃┈┈┈▏━╯┈┈┈┈┈┈ \n"
                     "┈┈┈▕┈┈┈╰╯┈┈┈▏┈┈┈┈┈┈┈┈ \n"
                     "┈┈┈▕╱╲╱╲╱╲╱╲▏┈┈┈┈┈┈┈┈ \n\n"
                     "♠️ ♠️A N S H I DQ h e r e♠️ ♠️ \n"
                     "= = == = = == = == = = == = = \n"
                     "▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ ▲ \n"
                     "🄸   🄰🄼   🄰🄻🄸🅅🄴 \n"
                    "▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ \n"
                     "== === == == === === == \n"
                     "▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️◾️◽️◾️◽️◾️◽️◽️◾️◽️ \n"
                     "----------------- --------\n"
                     "--------------------------\n️")
