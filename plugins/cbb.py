#(©) WeekendsBotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b><blockquote expandable>○ Oᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>Nᴀᴍᴇ Hᴜʜ</a>\n○ Mᴀɪɴ Cʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_StarDust'>Aɴɪᴍᴇ Sᴛᴀʀᴅᴜsᴛ</a>\n○ Mᴏᴠɪᴇs Uᴘᴅᴀᴛᴇs : <a href='https://t.me/Movies_Stardust'>Mᴏᴠɪᴇs Sᴛᴀʀᴅᴜsᴛ</a>\n○ Oᴜʀ Cᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/Sanctuary_Stardust'>Sᴀɴᴄᴛᴜᴀʀʏ</a>\n○ Aɴɪᴍᴇ Cʜᴀᴛ : <a href='https://t.me/+p8yoPpyKCoQxMzE1'>Cʜᴀᴛ Sᴛᴀʀᴅᴜsᴛ</a></blockquote></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡ Cℓσѕє", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
