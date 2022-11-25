from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from states.personal_data import PersonalData


@dp.message_handler(CommandHelp(), state=PersonalData.full_name)
async def bot_help(message: types.Message):
    text = 'Ism va Familiyangizni kiriting!'
    await message.answer(text)


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))
