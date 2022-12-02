from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentTypes.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command('book'))
async def send_book(message: types.Message):
    photo_id = 'AgACAgIAAxkBAAIECWOKMxdOxLjCKF2aQVUhJ37AdigNAAJVxDEbL_ZRSFtJE1RTDiI5AQADAgADeQADKwQ'
    # photo_file = InputFile(path_or_bytesio="photo_path")
    await message.reply_photo(photo_id, caption="this isn't book")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_id, caption="this isn't book")
