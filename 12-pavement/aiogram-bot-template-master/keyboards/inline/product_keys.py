from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build_keyboards(product):
    keys = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Xarid qilish', callback_data=f"product:{product}"),
            ],
        ],
    )
    return keys
