from pyrogram import filters, emoji
from Code_X_Mania.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message



@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply(f'Hi {m.from_user.mention(style="md")}, Send me a file to get an instant stream link.', quote=True)
