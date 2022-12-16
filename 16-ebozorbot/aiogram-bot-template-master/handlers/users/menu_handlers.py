from typing import Union

from aiogram import types
from aiogram.types import CallbackQuery, Message

from ...keyboards.inline.menu_keyboards import menu_cd, categories_keyboard, subcategories_keyboard, item_keyboard, \
    items_keyboard

from ...loader import dp, db


@dp.message_handler(text='Bosh menu')
async def show_menu(message: Message):
    await list_categories(message)


async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    markup = await categories_keyboard()

    if isinstance(message, Message):
        await message.answer(text="Bo'limni tanlang", reply_markup=markup)

    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup()


async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)
    await callback.message.edit_reply_markup(markup)


async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category=category, subcategory=subcategory)
    await callback.message.edit_text(text='Mahsulot tanlang', reply_markup=markup)


async def show_item(callback: CallbackQuery, category, subcategory, item_id):
    markup = item_keyboard(category, subcategory, item_id)

    item = await db.get_products(item_id)

    if item['photo']:
        text = f"<a href=\"{item['photo']}\"> {item['productname']} </a>\n\n"
    else:
        text = f"{item['productname']}\n\n"

    text += f"Narxi: {item['price']}$\n {item['description']}"

    await callback.message.edit_text(text=text, reply_markup=markup)


@dp.callback_query_handler(menu_cd.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')

    category = callback_data.get('category')

    subcategory = callback_data.get('subcategory')

    item_id = int(callback_data.get('item_id'))

