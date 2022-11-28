import asyncio
import datetime
import re

import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup, AdminFilter
from loader import dp, bot


#
@dp.message_handler(IsGroup(), Command('ro', prefixes='!/'), AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r'(!ro|/ro) ?(\d+)? ?([\w+\D]+)?')
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5

    time = int(time)

    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
        await message.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Xatolik {err.args}")
        return

    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} {time} minut yozolmaydi\n"
                         f"Sabab: \n<b>{comment}</b>")

    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command('unro', prefixes='!/'), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False
    )

    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")

    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f'Foydalanuvchi {member.full_name} tiklandi!')
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()
