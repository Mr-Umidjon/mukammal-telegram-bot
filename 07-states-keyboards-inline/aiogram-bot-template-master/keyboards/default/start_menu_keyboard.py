from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛍️ Mahsulotlar'),
            KeyboardButton(text='ℹ️Qoʼllanma'),
        ],
    ],
    resize_keyboard=True,
)
