from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="‹ اوامر التشغيل ›", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="‹ قـناة الـبوت ›", url=f"https://t.me/ah07v"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="‹ اوامر التشغيل ›", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="‹ طريقه التفعيل ›", callback_data="help_callback hb6"),
        ],
        [
            InlineKeyboardButton(text="‹ المطور ›", user_id=OWNER)
        ],
    ]
    return buttons
