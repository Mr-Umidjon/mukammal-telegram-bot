from aiogram import types

from loader import dp
from utils import photo_link


@dp.message_handler(content_types='photo')
async def photo_handler(message: types.Message):
    photo = message.photo[-1]
    link = await photo_link(photo)
    await message.answer(link)
