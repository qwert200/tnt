from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/ba9d2c3c527ae4d01709a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

@app.on_message(
   filters.command(["قناتي"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
            
    & filters.group) 
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/ba9d2c3c527ae4d01709a.jpg",
        caption=f"""‏"يّارب قلبًا لا يبالي بعابرٍ لم يُحسن العبور ، قلبًا نقيًا يكتم الغيظ ، يعفو عن الناس ويصبر على الأذى ، قلبًا سليمًا وممتلىء بك 🌸🤍.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♚...« مـكـنـوناتي 𝙷𝙼𝙳 »... ♚", url=f"https://t.me/ah07v")
                ]
            ]
        ),
    )

@app.on_message(
   filters.command(["قناتي"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""‏"يّارب قلبًا لا يبالي بعابرٍ لم يُحسن العبور ، قلبًا نقيًا يكتم الغيظ ، يعفو عن الناس ويصبر على الأذى ، قلبًا سليمًا وممتلىء بك 🌸🤍.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♚...« مـكـنـوناتي 𝙷𝙼𝙳 »... ♚", url=f"https://t.me/ah07v")
                ]
            ]
        ),
    )
