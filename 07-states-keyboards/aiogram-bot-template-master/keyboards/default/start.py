from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Contact", request_contact=True),
            KeyboardButton(text='Location', request_location=True),
        ],
    ],
    resize_keyboard=True
)
