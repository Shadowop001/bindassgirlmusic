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
        𝙸 𝚊𝚖 **{bn}** !! 𝙸 𝚕𝚎𝚝 𝚢𝚘𝚞 𝚙𝚕𝚊𝚢 𝚖𝚞𝚜𝚒𝚌 𝚒𝚗 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙'𝚜 𝚟𝚘𝚒𝚌𝚎 𝚌𝚑𝚊𝚝 ✨🥀 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍 𝚋𝚢:- **@VenomXowner**
  </b>""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐜𝐡𝐚𝐭", url="https://t.me/COLONY_OF_WEIRDOS_2",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👑 𝐎𝐰𝐧𝐞𝐫", url="https://t.me/VenomXowner"
                    ),
                    InlineKeyboardButton(
                        "🔊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/VenomXbots"
                    ),
                    InlineKeyboardButton(
                        "🍻 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭", url="https://t.me/VENOM_VC"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💫 𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 💫", url="https://t.me/VenomXmusicbot?startgroup=true"
                    ) 
                ]
            ]
        )
    )
