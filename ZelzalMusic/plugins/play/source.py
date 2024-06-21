import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/a31f8a9d92459aa707b4c.jpg",
        caption=f"""⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩", url=f"https://t.me/{app.username}?startgroup=true"),
                ],[
                    InlineKeyboardButton(
                        "َٰ𝚂𝙾𝚄𝚁𝙲𝙴 𝚃𝙴𝚁𝙱𝙾", url=f"https://t.me/terbo772"),
                    InlineKeyboardButton(
                        "َٰ𝚂𝙾𝚄𝚁𝙲𝙴 𝚃𝙴𝚁𝙱𝙾", url=f"https://t.me/terbo772"),
                ],[
                    InlineKeyboardButton(
                        "𝐃𝐄𝐕", url=f"https://t.me/VP_AB"),
                ],[
                    InlineKeyboardButton(
                        "𝐃𝐄𝐕 ", url=f"https://t.me/VP_AB"),
                ],[
                    InlineKeyboardButton(text="𝐂𝐥𝐨𝐬𝐞", callback_data="close"),   
            ]
        ]
         ),
     )
  
