import asyncio
import os
import time
import requests
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from asyncio import gather
from pyrogram.errors import FloodWait




@app.on_message(command(["اسمي", "اسمي ايه"]) & filters.group )
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""- ايه الاسم الجميل ده 🫧 : ❲ {message.from_user.mention()} ❳""") 
