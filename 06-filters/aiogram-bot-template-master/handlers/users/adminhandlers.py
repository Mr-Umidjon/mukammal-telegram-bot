from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


@dp.message_handler(filters.Command("change_photo"), filters.AdminFilter())
@dp.message_handler(commands='change_photo', is_chat_admin=True)
async def chat_admin_example(msg: types.Message):
    await msg.answer('Rasm almashtirasizmi?')
