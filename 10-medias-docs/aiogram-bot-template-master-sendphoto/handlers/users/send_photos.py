from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from ...loader import dp, bot


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)
