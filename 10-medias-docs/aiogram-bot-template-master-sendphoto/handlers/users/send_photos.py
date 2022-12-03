from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot
from keyboards.inline.buy_book import book_keys


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
    msg = "Sotildagian do'konlar:\n"
    await message.reply_photo(photo_id, caption="this isn't book")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_id, caption="this isn't book")
    await message.reply_photo(photo_id, caption=msg, reply_markup=book_keys)


@dp.message_handler(Command('courses'))
async def send_courses(message: types.Message):
    album = types.MediaGroup()
    photo1 = "AgACAgIAAxkBAAIECWOKMxdOxLjCKF2aQVUhJ37AdigNAAJVxDEbL_ZRSFtJE1RTDiI5AQADAgADeQADKwQ"
    photo2 = "AgACAgIAAxkBAAIECWOKMxdOxLjCKF2aQVUhJ37AdigNAAJVxDEbL_ZRSFtJE1RTDiI5AQADAgADeQADKwQ"
    photo3 = "AgACAgIAAxkBAAIECWOKMxdOxLjCKF2aQVUhJ37AdigNAAJVxDEbL_ZRSFtJE1RTDiI5AQADAgADeQADKwQ"
    photo4 = "AgACAgIAAxkBAAIECWOKMxdOxLjCKF2aQVUhJ37AdigNAAJVxDEbL_ZRSFtJE1RTDiI5AQADAgADeQADKwQ"
    album.attach_photo(photo4)
    album.attach_photo(photo3)
    album.attach_photo(photo2)
    album.attach_photo(photo1, caption='This is photo')

    await message.answer_media_group(media=album)
