from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.message_handler(Text(equals='assalom alaykum', ignore_case=True))
@dp.message_handler(Text(contains='assalom', ignore_case=True))
async def text_handler(msg: types.Message):
    await msg.answer("Vaalaykum Assalom")
