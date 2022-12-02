from loader import dp, bot
from aiogram.types import ContentType, Message
from pathlib import Path

download_path = Path().joinpath('downloads')
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler()
async def text_handler(message: Message):
    await message.reply("Siz matn yubordingiz!")


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download(destination=download_path)
    doc_id = message.document.file_id
    await message.reply(f'Siz hujjat yubordingiz!\n'
                        f'File id = {doc_id}')


@dp.message_handler(content_types=ContentType.VIDEO)
async def video_handler(message: Message):
    await message.video.download(destination=download_path)
    video_id = message.video.file_id
    await message.reply(f'Siz video yubordingiz!\n'
                        f'File id = {video_id}')


@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message: Message):
    await message.photo[-1].download(destination=download_path)
    photo_id = message.photo[-1].file_id
    await message.reply(f'Siz photo yubordingiz!\n'
                        f'File id = {photo_id}')


@dp.message_handler(content_types=ContentType.ANY)
async def any_handler(message: Message):
    await message.reply(f"{message.content_type} qabul qilindi")
