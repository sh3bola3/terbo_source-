from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from ZelzalMusic import app

hmses = {}

# Function to handle the whisper reply in groups
@app.on_message(filters.reply & filters.regex("همسه") & filters.group)
async def reply_with_link(client, message):
    user_id = message.reply_to_message.from_user.id
    my_id = message.from_user.id
    bar_id = message.chat.id
    start_link = f"https://t.me/{(await app.get_me()).username}?start=hms{my_id}to{user_id}in{bar_id}"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📩 اضغط لإرسال الهمسه!", url=start_link)]
        ]
    )
    await message.reply_text("🔔 إضغط لإرسال همسه!", reply_markup=reply_markup, reply_to_message_id=message.id)

waiting_for_hms = False

# Function to start the whisper process
@app.on_message(filters.command("start"), group=473)
async def hms_start(client, message):
    global waiting_for_hms, hms_ids
    if message.text.split(" ", 1)[-1].startswith("hms"):
        hms_ids = message.text
        waiting_for_hms = True
        await message.reply_text(
            "📝 أرسل الهمسه الآن.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("إلغاء ❌", callback_data="hms_cancel")],
                    [InlineKeyboardButton("تأكيد الهمسه ✅", callback_data="hms_confirm")]
                ]
            )
        )

# Function to handle the whisper sending
@app.on_message(filters.private & filters.text & ~filters.command("start"), group=921)
async def send_hms(client, message):
    global waiting_for_hms
    if waiting_for_hms:    
        to_id, from_id, in_id = map(int, [hms_ids.split("hms")[1].split("to")[0], hms_ids.split("to")[1].split("in")[0], hms_ids.split("in")[1]])

        to_url, from_url = f"tg://openmessage?user_id={to_id}", f"tg://openmessage?user_id={from_id}"
        
        hmses[str(to_id)] = {"hms": message.text, "bar": in_id, "from": from_id}
        
        await message.reply_text("✅ تم ارسال الهمسه.")
        
        # Send a notification to the group with mention
        await app.send_message(
            chat_id=in_id,
            text=f"💌 {(await app.get_chat(from_id)).first_name} لديك همسه جديدة من {(await app.get_chat(to_id)).first_name}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("👀 اضغط لرؤية الهمسه", callback_data="hms_answer")]
                ]
            )
        )
        
        waiting_for_hms = False

# Function to display the whisper
@app.on_callback_query(filters.regex("hms_answer"))
async def display_hms(client, callback):
    in_id, who_id = callback.message.chat.id, callback.from_user.id
    
    if hmses.get(str(who_id)) and hmses[str(who_id)]["bar"] == in_id:
        # Show the whisper to the recipient and the sender
        hms_text = hmses[str(who_id)]["hms"]
        from_id = hmses[str(who_id)]["from"]
        await callback.answer(hms_text, show_alert=True)
        if from_id != who_id:
            await app.send_message(chat_id=from_id, text=f"📬 همستك: {hms_text}")
    else:
        await callback.answer("❗️ الامر ليس لك", show_alert=True)

# Function to cancel the whisper
@app.on_callback_query(filters.regex("hms_cancel"))
async def cancel_hms(client, callback):
    global waiting_for_hms
    waiting_for_hms = False
    
    await client.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=callback.message.id,
        text="❌ تم إلغاء الهمسه!"
    )

# Function to confirm the whisper (newly added as per request)
@app.on_callback_query(filters.regex("hms_confirm"))
async def confirm_hms(client, callback):
    await callback.answer("✅ تم تأكيد الهمسه", show_alert=True)

# Function to handle mentions (newly added as per request)
@app.on_message(filters.text & filters.group)
async def handle_mentions(client, message):
    text = message.text
    if "@botusername" in text:  # Replace with your bot's username
        await message.reply_text("😅 انتا بتمنشن للبوت يعبيط اعقل")
    elif f"@{message.from_user.username}" in text:
        await message.reply_text("🤔 انتا بتمنشن لي نفسك ليه؟")
