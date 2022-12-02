from loader import dp, bot
from aiogram.types import ContentType, Message


@dp.message_handler()
async def text_handler(message: Message):
    await message.reply("Siz matn yubordingiz!")


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download()
    doc_id = message.document.file_id
    await message.reply(f'Siz hujjat yubordingiz!\n'
                        f'File id = {doc_id}')


@dp.message_handler(content_types=ContentType.VIDEO)
async def video_handler(message: Message):
    await message.video.download()
    doc_id = message.video.file_id
    await message.reply(f'Siz video yubordingiz!\n'
                        f'File id = {doc_id}')
