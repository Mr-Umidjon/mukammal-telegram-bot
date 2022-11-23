from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

SUPER_USERS = [2007427, 1634251726]
BLACK_LIST = [1234567, 5687981]


@dp.message_handler(filters.IDFilter(chat_id=SUPER_USERS))
# @dp.message_handler(chat_id=SUPER_USERS, text='secret')
@dp.message_handler(chat_id=SUPER_USERS, commands='start')
async def id_filter_handler(msg: types.Message):
    await msg.answer("Xush kelibsiz, Super User!")
