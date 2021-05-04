import os

import youtube_dl
from youtube_search import YoutubeSearch
import requests

from helpers.filters import command, other_filters2
from helpers.decorators import errors

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Voice

from config import BOT_NAME as bn


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
I let you play music in your group's voice chat 😉

Maintained by:- **@VenomXowner**

The commands I currently support are:
✨ /play - __Plays the replied audio file or YouTube video through link.__
✨ /dplay - __play song you requested via deezer.__
✨ /splay - __play song you requested via jio saavn.__
✨ /song - __Uploads the searched song in the chat.__
✨ /pause - __Pause Voice Chat Music.__
✨ /resume - __Resume Voice Chat Music.__
✨ /skip - __Skips the current Music Playing In Voice Chat.__
✨ /stop - __Clears The Queue as well as ends Voice Chat Music.__

**Admins only**
✨/player - __open music player settings panel__
✨/pause - __pause song play__
✨/resume - __resume song play__
✨/skip - __play next song__
✨/end - __stop music play__
✨/userbotjoin - __invite assistant to your chat__
✨/userbotleave -__ remove assistant from your chat__
✨/admincache - __Refresh admin list__
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Support Group", url="https://t.me/COLONY_OF_WEIRDOS_2"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "✨ Channel", url="https://t.me/VenomXbots"
                    ),
                    InlineKeyboardButton(
                        "🍻 Assistant", url="https://t.me/VENOM_VC"
                    ),
                    InlineKeyboardButton(
                        "👑 Owner", url="https://t.me/VenomXowner" )
                ],
                [
                    InlineKeyboardButton(
                        text="✨ Add me to your group",
                        url="t.me/{}?startgroup=true".format(
                             context.bot.username
                                )]
        )
    )
