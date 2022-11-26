import logging

from aiogram.types import Message, CallbackQuery

from keyboards.inline.products_keyboard import category_menu, courses_menu, books_menu

from loader import dp


@dp.message_handler(text_contains='Mahsulotlar')
async def select_category(message: Message):
    await message.answer('Mahsulot tanlang', reply_markup=category_menu)


@dp.callback_query_handler(text='courses')
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    await call.message.answer("Kurs tanlang", reply_markup=courses_menu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains='books')
async def buy_books(call: CallbackQuery):
    await call.message.answer('Kitoblar', reply_markup=books_menu)
    await call.message.delete()
    await call.answer(cache_time=60)
