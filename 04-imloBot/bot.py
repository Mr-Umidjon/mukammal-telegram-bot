from check_words import check_words
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5649816429:AAH4Ai0vw4t0ztC5iphWWVq3om_1RlekWSc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Uz Imlo Botiga xush kelibsiz!")


@dp.message_handler(commands=['help'])
async def help_user(message: types.Message):
    await message.reply("Botga foydalanish uchun so'z yuboring")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    word = message.text.lower()
    result = check_words(word)

    if result['available']:
        response = f"✅ {word.capitalize()}"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"

    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
