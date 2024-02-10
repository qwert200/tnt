from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافه البوت لمجموعتك",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ اوامر التشغيل ›",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="‹ الاعدادات ›", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافه البوت لمجموعتك",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ طريقه التفعيل ›", callback_data="help_callback hb6"
            ), 
            InlineKeyboardButton(
                text="‹ اوامر التشغيل ›", callback_data="settings_back_helper"
             )
        ],
        [
            InlineKeyboardButton(
                text="‹ المطور ›", user_id=OWNER
            )
        ],
        [ 
            InlineKeyboardButton(
                text="‹ قـناة الـبوت ›", url=f"https://t.me/ah07v"
            )
        ],
     ]
    return buttons
