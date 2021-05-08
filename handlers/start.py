import youtube_dl
from youtube_search import YoutubeSearch
import requests

from helpers.filters import command, other_filters2
from helpers.decorators import errors

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Voice

from config import BOT_NAME as {bn}


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
I let you play music in your group's voice chat ✨🥀

Maintained by:- **@VenomXowner**
  </b>""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Support chat", url="https://t.me/COLONY_OF_WEIRDOS_2",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👑 Owner", url="https://t.me/VenomXowner"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/VenomXbots"
                    ),
                    InlineKeyboardButton(
                        "🍻 Assistant", url="https://t.me/VENOM_VC"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/VenomXmusicbot?startgroup=true"
                    ) 
                ]
            ]
        )
    )
