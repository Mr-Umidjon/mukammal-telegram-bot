from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from data.config import ADMINS, CHANNELS
from keyboards.inline.manage_post import post_callback, confirmation_keyboard
from loader import dp, bot
from states.newpost import NewPost


@dp.message_handler(Command('create_post'))
async def create_post(message: Message):
    await message.answer("Chop etish uchun post yuboring")
    await NewPost.NewMessage.set()


@dp.message_handler(state=NewPost.NewMessage, content_types=types.ContentTypes.ANY)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"Postni tekshirish uchun yuborasizmi?", reply_markup=confirmation_keyboard)
    await NewPost.next()


@dp.callback_query_handler(post_callback.filter(action='post'), state=NewPost.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get('text')
        mention = data.get('mention')
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Post adming yuborildi')
    await bot.send_message(ADMINS[0], f"Foydalunuvchi {mention} quydagi postni chop etmoqchi")
    await bot.send_message(ADMINS[0], text, parse_mode="HTML", reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action='cancel'), state=NewPost.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Post rad etildi')


@dp.message_handler(state=NewPost.Confirm)
async def post_unknown(message: Message):
    await message.answer("Chop etish yoki rad etishni tanlang")


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS)
async def approve_post(call: CallbackQuery, data: dict):
    await call.answer("Chop etishga ruhsat berdingiz.", show_alert=False)
    target_channel = CHANNELS[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def decline_post(call: CallbackQuery, data: dict):
    await call.answer("Post rad etildi.", show_alert=False)
    await call.message.edit_reply_markup()
