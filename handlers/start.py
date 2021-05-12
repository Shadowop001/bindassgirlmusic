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
\n𝙸 𝚊𝚖 {bn} !! 𝙸 𝚕𝚎𝚝 𝚢𝚘𝚞 𝚙𝚕𝚊𝚢 𝚖𝚞𝚜𝚒𝚌 𝚒𝚗 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙'𝚜 𝚟𝚘𝚒𝚌𝚎 𝚌𝚑𝚊𝚝 ✨🥀 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍 𝚋𝚢:- @VenomXowner
\nTo add in your group contact us at @VenomXbots.
\nHit /help list of available commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Support group", url="https://t.me/VenomXowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👑 Owner", url="https://t.me/VenomXowner"
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
                        "💫 𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 💫", url="https://t.me/VCPlayBot?startgroup=true"
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
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/VenomXbots"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
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
                        "🔊 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/VenomXbots"
                    )
                ]
            ]
        )
    )
