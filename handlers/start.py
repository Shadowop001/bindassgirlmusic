from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAx0CS3uSDgACARJglhwHK5VLp6vRfi6nZs1-cwABHZkAAhoBAAL9RrFEtLB2pCHK-wkfBA")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nšø šš {bn} !! šø ššš š¢šš šššš¢ ššššš šš š¢ššš ššššš'š ššššš šššš āØš„ š¼ššššššššš šš¢:- @VenomXowner
\nTo add in your group contact us at @VenomXbots.
\nHit /help list of available commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š Owner", url="https://t.me/aarshy"
                    ),
                    InlineKeyboardButton(
                        "š» šš¬š¬š¢š¬š­šš§š­", url="https://t.me/BINDASS_GIRL_VC"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "š« ššš ššØ ššØš®š« šš«šØš®š© š«", url="https://t.me/Bindass_girl_music_bot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "šš»āāļø Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š Owner", url="https://t.me/aarshy"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "ā Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ā", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š Owner", url="https://t.me/aarshy"
                    )
                ]
            ]
        )
    )
