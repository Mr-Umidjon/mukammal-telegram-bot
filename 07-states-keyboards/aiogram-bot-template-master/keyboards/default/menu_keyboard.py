from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Python"),
            KeyboardButton(text='Telegram bot'),
        ],
    ],
    resize_keyboard=True
)
