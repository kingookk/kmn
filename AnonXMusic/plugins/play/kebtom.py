import asyncio
import platform
from sys import version as pyver
from datetime import datetime
import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from pytgcalls.__version__ import __version__ as pytgver
from pyromod import *
import config
from config import BANNED_USERS, MUSIC_BOT_NAME
from strings import get_command
from AnonXMusic import YouTube, app
from AnonXMusic import app as Client
from AnonXMusic.core.userbot import assistants
from AnonXMusic.misc import SUDOERS, pymongodb
from strings.filters import command
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import (get_global_tops,
                                       get_particulars, get_queries,
                                       get_served_chats,
                                       get_served_users, get_sudoers,
                                       get_top_chats, get_topp_users, get_client)
from AnonXMusic.utils.decorators.language import language, languageCB
from AnonXMusic.utils.inline.stats import (back_stats_buttons,
                                           back_stats_markup,
                                           get_stats_markup,
                                           overallback_stats_markup,
                                           stats_buttons,
                                           top_ten_stats_markup)



###$##Toooooooom##################£££££
@app.on_message(command(["/sz", "• رجوع •"]) & SUDOERS & filters.private)
async def kep(client, message):
  kep = ReplyKeyboardMarkup([["قسم الاذاعه"], ["قسم الحساب المساعد"], ["اخفاء الكيبورد"]], resize_keyboard=True)
  await message.reply_text("★مرحبا بك عزيزي المطور في سورس سيزر", reply_markup=kep)



@Client.on_message(filters.command("اخفاء الكيبورد", "") & SUDOERS)
async def ahmed(client, message):
	await message.reply("• تم اخفاء الكيبورد ارسل /sz لعرضه مره اخري",reply_markup=ReplyKeyboardRemove(selective=True), quote=True) 


@Client.on_message(filters.command("قسم الحساب المساعد", "") & SUDOERS)
async def helpercn(client, message):
   #userbot = await get_client(1)
  # me = await userbot.get_me()
 #  i = f"@{me.username} : {me.id}" if me.username else me.id
  # b = await client.get_chat(me.id)
  # b = b.bio if b.bio else "لا يوجد بايو"
   kep = ReplyKeyboardMarkup([["• فحص المساعد •"], ["• تغير الاسم الاول •", "• تغير الاسم التاني •"], ["• تغير البايو •"], ["• تغير اسم المستخدم •"], ["• اضافه صوره •", "• ازالة الصور •"], ["• رجوع •"]], resize_keyboard=True)
   await message.reply_text(f"**أهلا بك عزيزي المطور **\n**هنا قسم الحساب المساعد**", reply_markup=kep)
   
@Client.on_message(filters.command(["قسم الاذاعه"], "") & SUDOERS)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["ذيع للمستخدمين"], ["ذيع بالمساعد"], ["ذيع فوق"],["ذيع لابوت"], ["ذيع"], ["• رجوع •"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)






@Client.on_message(filters.command("• فحص المساعد •", "") & SUDOERS)
async def userrrrr(client: Client, message):
    mm = await message.reply_text("Collecting stats")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    client = await get_client(1)
    Meh=await client.get_me()
    usere = Meh.username
    group = ["supergroup", "group"]
    async for dialog in client.iter_dialogs():
        if dialog.chat.type == "private":
            u += 1
        elif dialog.chat.type == "bot":
            b += 1
        elif dialog.chat.type == "group":
            g += 1
        elif dialog.chat.type == "supergroup":
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status in ("creator", "administrator"):
                a_chat += 1
        elif dialog.chat.type == "channel":
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await mm.edit_text(
        """**ꜱᴛᴀᴛꜱ ꜰᴇᴀᴛᴄʜᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ ✅**
✅**ʏᴏᴜ ʜᴀᴠᴇ {} ᴘʀɪᴠᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ᴄʜᴀɴɴᴇʟꜱ.**
🏷️**ʏᴏᴜ ᴀʀᴇ ᴀᴅᴍɪɴꜱ ɪɴ {} ᴄʜᴀᴛꜱ.**
🏷️**ʙᴏᴛꜱ ɪɴ ʏᴏᴜʀ ᴘʀɪᴠᴀᴛᴇ = {}**
⚠️**ꜰᴇᴀᴛᴄʜᴇᴅ ʙʏ ᴜꜱɪɴɢ @{} **""".format(
            ms, u, g, sg, c, a_chat, b, usere
        )
    )
    
@Client.on_message(filters.command(["• تغير الاسم الاول •", "الاسم الاول"], "") & SUDOERS)
async def changefisrt(client: Client, message):
   try:
    if message.text == "• تغير الاسم الاول •":
      return await message.reply_text("• الان قم بالرد علي الاسم الجديد باستخدام كلمه الاسم الاول •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(first_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم")


@Client.on_message(filters.command(["• تغير الاسم التاني •", "الاسم التاني"], "") & SUDOERS)
async def changelast(client: Client, message):
   try:
    if message.text == "• تغير الاسم التاني •":
      return await message.reply_text("• الان قم بالرد علي الاسم الجديد باستخدام كلمه الاسم التاني •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(last_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم ")


@Client.on_message(filters.command(["• تغير البايو •", "البايو الجديد"], "") & SUDOERS)
async def changebio(client: Client, message):
   try:
    if message.text == "• تغير البايو •":
      return await message.reply_text("• الان قم بالرد علي البايو الجديد باستخدام كلمة البايو الجديد •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(bio=name)
    await message.reply_text("**تم تغير البايو بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير البايو ")


@Client.on_message(filters.command(["• تغير اسم المستخدم •", "اليوزر"], "") & SUDOERS)
async def changeusername(client: Client, message):
   try:
    if message.text == "• تغير اسم المستخدم •":
      return await message.reply_text("• الان قم بالرد علي اليوزر الجديد بدون علامة @ باستخدام كلمه اليوزر •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.set_username(name)
    await message.reply_text("**تم تغير اسم المستخدم بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير اسم المستخدم")


@Client.on_message(filters.command(["• اضافه صوره •", "صوره جديده"], "") & SUDOERS)
async def changephoto(client: Client, message):
   try:
    if message.text == "• اضافه صوره •":
      return await message.reply_text("• الان قم بالرد علي الصورة الجديدة بكلمه صوره جديده •")
    m = message.reply_to_message
    photo = await m.download()
    client = await get_client(1)
    await client.set_profile_photo(photo=photo)
    await message.reply_text("**تم تغير صوره الحساب المساعد بنجاح .✅**") 
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الصوره")

@Client.on_message(filters.command(["• ازاله صوره •"], "") & SUDOERS)
async def changephotos(client: Client, message):
       try:
        client = await get_client(1)
        photos = await client.get_profile_photos("me")
        await client.delete_profile_photos([p.file_id for p in photos[1:]])
        await message.reply_text("**تم ازاله صوره بنجاح .✅**")
       except Exception as es:
         await message.reply_text(f" حدث خطأ أثناء ازاله الصوره")


