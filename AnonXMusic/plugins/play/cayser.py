import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(filters.command(["زين", "《مطور السورس》"], ""))
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2514530559cc173845e3f.jpg",
caption=f"""[زيـــــــٌن اݪــتأࢪيخ 🚸 الغلبان  مطور السورس ❤️‍🔥](https://t.me/L_HLN)يوزر زين @sourceav ❤️‍🔥✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                    "●━◉⟞⟦ 𝘼𝙑𝘼𝙏𝘼𝙍 ⟧⟝◉━●", url=f"https://t.me/sourceav"
                ),
                ],
                [
                    InlineKeyboardButton(
                        "زيـــــــٌن اݪــتأࢪيخ 🚸", url=f"https://t.me/L_HLN"),
                ],
            ]
        ),
    )
