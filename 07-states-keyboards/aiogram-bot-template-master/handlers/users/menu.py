from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menu_keyboard import menu
from keyboards.default.python_keyboard import menu_python

from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu)


@dp.message_handler(text='Telegram bot')
async def send_link(message: Message):
    await message.answer("Mukammal Telegram bot kursi: https://mohirdev.uz/courses/telegram")


@dp.message_handler(text='Python')
async def send_link(message: Message):
    await message.answer("Mavzu tanlang", reply_markup=menu_python)


@dp.message_handler(text='#00 Kirish')
async def send_link(message: Message):
    await message.answer("https://mohirdev.uz/courses/telegram", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text='Boshiga')
async def send_link(message: Message):
    await message.answer("Mavzu tanlang", reply_markup=menu)
