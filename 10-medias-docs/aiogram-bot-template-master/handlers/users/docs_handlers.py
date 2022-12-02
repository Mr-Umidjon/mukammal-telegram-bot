from ...loader import dp, bot
from aiogram.types import ContentType, Message


@dp.message_handler()
async def text_handler(message: Message):
    await message.reply("Siz matn yubordingiz!")


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download()

    await message.reply('Siz hujjat yubordingiz!')
