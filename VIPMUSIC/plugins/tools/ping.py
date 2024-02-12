from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils import bot_sys_stats
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.inline import supp_markup
from VIPMUSIC.utils.inline import close_markup
from config import BANNED_USERS
import aiohttp
import asyncio
from io import BytesIO
from PIL import Image, ImageEnhance  # Add these imports

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())

    # Open the image using PIL
    carbon_image = Image.open(image)

    # Increase brightness
    enhancer = ImageEnhance.Brightness(carbon_image)
    bright_image = enhancer.enhance(1.7)  # Adjust the enhancement factor as needed

    # Save the modified image to BytesIO object with increased quality
    output_image = BytesIO()
    bright_image.save(output_image, format='PNG', quality=95)  # Adjust quality as needed
    output_image.name = "carbon.png"
    return output_image

@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    PING_IMG_URL = "https://telegra.ph/file/37b57c6aaaa793bba055a.jpg"
    captionss = "**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ.**"
    response = await message.reply_photo(PING_IMG_URL, caption=(captionss))
    await asyncio.sleep(1)
    await response.edit_caption("**استقيمي ايتها النفس عسى أن يكون الرحيل قريبا ✨🥺💔**")
    await asyncio.sleep(1)
    await response.edit_caption("**استقيمي ايتها النفس عسى أن يكون الرحيل قريبا ✨🥺💔**")
    await asyncio.sleep(1)
    await response.edit_caption("**استقيمي ايتها النفس عسى أن يكون الرحيل قريبا ✨🥺💔**")
    await asyncio.sleep(1.5)
    await response.edit_caption("**استقيمي ايتها النفس عسى أن يكون الرحيل قريبا ✨🥺💔**")
    await asyncio.sleep(2)
    await response.edit_caption("**استقيمي ايتها النفس عسى أن يكون الرحيل قريبا ✨🥺💔**")
    await asyncio.sleep(2)
    await response.edit_caption("**استقيمي ايتها النفس عسى أن يكون الرحيل قريبا ✨🥺💔**")
    start = datetime.now()
    pytgping = await VIP.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    text =  _["ping_2"].format(resp, app.name, UP, RAM, CPU, DISK, pytgping)
    carbon = await make_carbon(text)
    captions = "**صلـوا علـى جمّيـل الوجـه ،و بـدرُ التمـام ،شفيـع الخلـق فـي يـوم الزحـام.
‏اللهـم صلـى وسلـم علـى نبينـا مُحمد ﷺ🤍**"
    await message.reply_photo((carbon), caption=captions,
    reply_markup=InlineKeyboardMarkup(
            [
                [
            InlineKeyboardButton(
                text="✦ المطور ✦", url=f"https://t.me/TG_FRIENDSS",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="✦ قناة الـبوت ✦", url=f"https://t.me/ah07v",
            ),
            InlineKeyboardButton(
                text="✦ اوامر الاشغيل ✦", url=f"https://t.me/{app.username}?start=help"
            )
        ],
    ]
    ),
        )
    await response.delete()

    close_button = InlineKeyboardButton("๏ اغلاق ๏", callback_data="close_data")
    inline_keyboard = InlineKeyboardMarkup([[close_button]])

@app.on_callback_query(filters.regex("^close_data"))
async def close_callback(_, query):
    chat_id = query.message.chat.id
    await query.message.delete()
