from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("https://telegra.ph/file/f474ba584530f5786a489.mp4")
    await message.reply_text(
        f"""I am **{bn}** !!
I let you play music in your group's voice chat ✨🥀

Maintained by:- **@VenomXowner**
     """,
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
