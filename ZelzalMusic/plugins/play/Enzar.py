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

mazen = {}
tom_max = 3

@app.on_message(filters.command("انذار", ""))
async def tom(client, message):
    me = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    if chat_id not in mazen:
        mazen[chat_id] = {}
    if user_id not in mazen[chat_id]:
        mazen[chat_id][user_id] = 1
    else:
        mazen[chat_id][user_id] += 1
    await message.reply_text(f"{mazen[chat_id][user_id]}")
    if mazen[chat_id][user_id] >= tom_max:
        try:
        	del mazen[chat_id][user_id]
        	await client.ban_chat_member(chat_id, user_id)
        	await message.reply("تم طرد العضو .")   	
        except:
        	await message.reply("↢ لم يتم حظر العضو .")
        
        



#ZeMusic
