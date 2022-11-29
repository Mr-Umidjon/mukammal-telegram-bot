import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import CHANNELS
from keyboards.inline.subscription import check_button
from loader import dp, bot
from utils.misc import subscription


@dp.message_handler(CommandStart())
async def show_channels(message: types.Message):
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        logging.info(invite_link)
        channels_format += f"<a href='{invite_link}'>{chat.title}</a>\n"

    await message.answer(f"Bot dan foydalanish uchun quydagi obuna bo'ling\n"
                         f" {channels_format} ",
                         reply_markup=check_button,
                         disable_web_page_preview=True,
                         )


@dp.callback_query_handler(text='check_subs')
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id, channel=channel)

        channel = await bot.get_chat(chat_id=channel)
        if status:
            result += f"{channel.title} ga obunasiz\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"{channel.title} ga obuna emassiz "
                       f"<a href='{invite_link}'>Obuna Bo'ling</a>\n\n")
    await call.message.answer(result, disable_web_page_preview=True)
