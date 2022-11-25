from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_python = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#00 Kirish"),
            KeyboardButton(text="#01 Kerakli dasturlar"),
            KeyboardButton(text='#02 Hello World!'),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),
        ],
    ],
    resize_keyboard=True,
)
