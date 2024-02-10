from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from VIPMUSIC import app

def first_page(_):
	controll_button = [InlineKeyboardButton(text="๏ ᴍᴇɴᴜ ๏", callback_data=f"settingsback_helper"), InlineKeyboardButton(text="๏ ɴᴇxᴛ ๏", callback_data=f"dilXaditi")]
	first_page_menu = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="‹ اوامر القنوات ›",
                    callback_data="help_callback hb1",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="‹ اوامر المجموعات ›",
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="‹ اوامر بالانگليزي ›",
                    callback_data="help_callback hb3")],
			controll_button,
		]
	)
	return first_page_menu


def second_page(_):
	controll_button = [InlineKeyboardButton(text="๏ ʙᴀᴄᴋ ๏", callback_data=f"settings_back_helper")]
	second_page_menu = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="‹ اوامر القنوات ›",
                    callback_data="help_callback hb1",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="‹ اوامر المجموعات ›",
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="‹ اوامر بالانگليزي ›",
                    callback_data="help_callback hb3")],
			controll_button,
		]
	)
	return second_page_menu
    

def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
	),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="‹ اوامر القنوات ›",
                    callback_data="help_callback hb1",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="‹ اوامر المجموعات ›",
                    callback_data="help_callback hb2",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="‹ اوامر بالانگليزي ›",
                    callback_data="help_callback hb3",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎭 𝐇𝐄𝐋𝐏 🎭",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
