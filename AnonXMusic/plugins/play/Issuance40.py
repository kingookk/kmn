import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(filters.command(["اختصار","معلومات","✨معلومات"], ""))
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/26b3058026045839af45d.jpg",
        caption=f"""**⋖━━❲𖣂❳━━𝘼𝙑𝘼𝙏𝘼𝙍━━❲𖣂❳━━⋗**\nمرحبا بك عزيزي {message.from_user.mention}\n
♡♕᚜ اسم سورس:-افتار
♡♕᚜ نوعه:-ميوزك
♡♕᚜ للغه برمجه:- بايثون
♡♕᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
♡♕᚜ مجال تشغيل :- تشغيل بوتات الميوزك
♡♕᚜ نظام تشغيل:-انوكس بوت ميوزك
♡♕᚜ الاصدار 4.0.1 pyrogram 
♡♕᚜ تاريخ تاسيس:-10-4-2022

**⋖━━❲𖣂❳━━𝘼𝙑𝘼𝙏𝘼𝙍━━❲𖣂❳━━⋗**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "●━◉⟞⟦ 𝙨𝙤𝙪𝙧𝙘𝙚 𝙨𝙚𝙯𝙖𝙧 ⟧⟝◉━●", url=f"https://t.me/sourceav"), 
                 ],[
                 InlineKeyboardButton(
                        "◁", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )


